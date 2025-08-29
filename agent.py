#!/usr/bin/env python3
"""
OpenAI GPT Chat Agent Core Implementation

This module provides the main ChatAgent class that handles all OpenAI GPT model variants
with unified functionality.
"""

import json
import yaml
import time
import requests
from pathlib import Path
from datetime import datetime
from dataclasses import asdict
from typing import Optional, Generator, List, Dict, Any
from requests.exceptions import RequestException, HTTPError, Timeout

from config import AgentConfig, SUPPORTED_MODELS
from utils import (
    setup_directories, setup_logging, create_backup, process_file_inclusions,
    get_api_key, list_available_files
)


class OpenAIGPTChatAgent:
    """Unified OpenAI GPT Chat Agent supporting all model variants"""
    
    def __init__(self, agent_id: str, model: str = "gpt-5"):
        self.agent_id = agent_id
        self.base_dir = Path(f"agents/{agent_id}")
        self.api_url = "https://api.openai.com/v1/chat/completions"
        
        # Validate model
        if model not in SUPPORTED_MODELS:
            raise ValueError(f"Unsupported model: {model}. Supported models: {list(SUPPORTED_MODELS.keys())}")
        
        # Create directory structure
        setup_directories(self.base_dir)
        
        # Setup logging
        self.logger = setup_logging(agent_id, self.base_dir)
        
        # Load or create config
        self.config = self._load_config(model)
        
        # Load conversation history
        self.messages = self._load_history()
        
        # Setup API key
        self.api_key = get_api_key(self.config.model, self.base_dir, self.logger)
        
        model_display = SUPPORTED_MODELS[self.config.model]["name"]
        self.logger.info(f"Initialized OpenAI {model_display} Chat Agent: {agent_id} with model: {self.config.model}")

    def _load_config(self, model: str) -> AgentConfig:
        """Load agent configuration from config.yaml"""
        config_file = self.base_dir / "config.yaml"
        
        if config_file.exists():
            try:
                with open(config_file, 'r', encoding='utf-8') as f:
                    config_data = yaml.safe_load(f)
                    # Ensure model is set correctly
                    config_data['model'] = model
                    return AgentConfig(**config_data)
            except Exception as e:
                self.logger.error(f"Error loading config: {e}")
                config = AgentConfig(model=model)
                self._save_config(config)
                return config
        else:
            config = AgentConfig(model=model)
            self._save_config(config)
            return config

    def _save_config(self, config: Optional[AgentConfig] = None):
        """Save agent configuration to config.yaml"""
        if config is None:
            config = self.config
            
        config.updated_at = datetime.now().isoformat()
        config_file = self.base_dir / "config.yaml"
        
        try:
            with open(config_file, 'w', encoding='utf-8') as f:
                yaml.dump(asdict(config), f, default_flow_style=False, allow_unicode=True)
        except Exception as e:
            self.logger.error(f"Error saving config: {e}")

    def _load_history(self) -> List[Dict[str, Any]]:
        """Load conversation history from history.json"""
        history_file = self.base_dir / "history.json"
        
        if history_file.exists():
            try:
                with open(history_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                self.logger.error(f"Error loading history: {e}")
                return []
        return []

    def _save_history(self):
        """Save conversation history to history.json with backup"""
        history_file = self.base_dir / "history.json"
        
        # Create backup if history exists
        if history_file.exists():
            create_backup(history_file, self.base_dir / "backups", self.logger)
        
        try:
            with open(history_file, 'w', encoding='utf-8') as f:
                json.dump(self.messages, f, indent=2, ensure_ascii=False)
        except Exception as e:
            self.logger.error(f"Error saving history: {e}")

    def add_message(self, role: str, content: str, metadata: Optional[Dict[str, Any]] = None):
        """Add a message to conversation history"""
        message = {
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat(),
            "metadata": metadata or {}
        }
        
        self.messages.append(message)
        
        # Truncate history if needed
        if len(self.messages) > self.config.max_history_size:
            removed = self.messages[:-self.config.max_history_size]
            self.messages = self.messages[-self.config.max_history_size:]
            self.logger.info(f"Truncated history: removed {len(removed)} old messages")
        
        self._save_history()

    def _build_api_payload(self, new_message: str, override_config: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Build the API request payload"""
        # Process file inclusions
        processed_message = process_file_inclusions(new_message, self.base_dir, self.logger)
        
        # Build messages in the API format
        messages = []
        
        # Add system prompt as developer role if configured
        if self.config.system_prompt:
            messages.append({
                "role": "developer",
                "content": [
                    {"type": "text", "text": self.config.system_prompt}
                ]
            })
        
        # Add conversation history
        for msg in self.messages:
            if msg["role"] in ["user", "assistant"]:
                messages.append({
                    "role": msg["role"],
                    "content": [
                        {"type": "text", "text": msg["content"]}
                    ]
                })
        
        # Add new user message
        messages.append({
            "role": "user",
            "content": [
                {"type": "text", "text": processed_message}
            ]
        })
        
        # Apply config overrides
        config = asdict(self.config)
        if override_config:
            config.update(override_config)
        
        # Build payload
        payload = {
            "model": config["model"],
            "messages": messages,
            "response_format": {"type": "text"},
            "verbosity": config["text_verbosity"],
            "reasoning_effort": config["reasoning_effort"]
        }
        
        # Add streaming if enabled
        if config["stream"]:
            payload["stream"] = True
        
        # Add optional parameters
        if config.get("max_output_tokens"):
            payload["max_completion_tokens"] = config["max_output_tokens"]
            
        if config.get("temperature") != 1.0:
            payload["temperature"] = config["temperature"]
            
        if config.get("top_p") != 1.0:
            payload["top_p"] = config["top_p"]
            
        return payload

    def _get_timeout_for_reasoning(self, model: str = None, reasoning_effort: str = "medium") -> int:
        """Get appropriate timeout based on model and reasoning effort"""
        if model is None:
            model = self.config.model
            
        model_info = SUPPORTED_MODELS.get(model)
        if not model_info:
            # Fallback to default timeout
            return 300
            
        return model_info["reasoning_timeout"].get(reasoning_effort, 300)

    def _make_api_request(self, payload: Dict[str, Any]) -> requests.Response:
        """Make API request with retries and error handling"""
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        
        # Get appropriate timeout
        model = payload.get("model", self.config.model)
        reasoning_effort = payload.get("reasoning_effort", "medium")
        timeout = self._get_timeout_for_reasoning(model, reasoning_effort)
        
        model_display = SUPPORTED_MODELS.get(model, {}).get('name', model)
        self.logger.info(f"Using timeout of {timeout}s for {model_display} with reasoning effort: {reasoning_effort}")
        
        max_retries = 3
        base_delay = 1
        
        for attempt in range(max_retries):
            try:
                self.logger.info(f"Making API request to {model_display} (attempt {attempt + 1}/{max_retries}) with {timeout}s timeout...")
                
                response = requests.post(
                    self.api_url,
                    headers=headers,
                    json=payload,
                    stream=payload.get("stream", True),
                    timeout=timeout
                )
                
                if response.status_code == 200:
                    self.logger.info("API request successful")
                    return response
                elif response.status_code == 401:
                    raise ValueError("Invalid API key")
                elif response.status_code == 403:
                    raise ValueError("API access forbidden")
                elif response.status_code == 429:
                    # Rate limited - wait and retry
                    delay = base_delay * (2 ** attempt)
                    self.logger.warning(f"Rate limited, retrying in {delay}s...")
                    time.sleep(delay)
                    continue
                elif response.status_code >= 500:
                    # Server error - retry
                    delay = base_delay * (2 ** attempt)
                    self.logger.warning(f"Server error {response.status_code}, retrying in {delay}s...")
                    time.sleep(delay)
                    continue
                else:
                    response.raise_for_status()
                    
            except Timeout as e:
                self.logger.warning(f"Request timed out after {timeout}s (attempt {attempt + 1}/{max_retries})")
                if attempt == max_retries - 1:
                    raise Exception(f"Request timed out after {timeout}s. Try reducing reasoning effort.")
                delay = base_delay * (2 ** attempt)
                self.logger.warning(f"Retrying in {delay}s...")
                time.sleep(delay)
            except RequestException as e:
                if attempt == max_retries - 1:
                    raise
                delay = base_delay * (2 ** attempt)
                self.logger.warning(f"Request failed ({e}), retrying in {delay}s...")
                time.sleep(delay)
        
        raise Exception(f"Failed to complete API request after {max_retries} attempts")

    def _parse_streaming_response(self, response: requests.Response) -> Generator[str, None, None]:
        """Parse streaming Server-Sent Events response"""
        assistant_message = ""
        
        try:
            for line in response.iter_lines(decode_unicode=True):
                if not line or line.strip() == "":
                    continue
                
                try:
                    # Handle Server-Sent Events format
                    if line.startswith("data: "):
                        data_str = line[5:].strip()
                        
                        if data_str == "[DONE]":
                            break
                            
                        data = json.loads(data_str)
                        
                        # Handle streaming format
                        choices = data.get("choices", [])
                        if choices:
                            choice = choices[0]
                            delta = choice.get("delta", {})
                            content = delta.get("content", "")
                            
                            if content:
                                assistant_message += content
                                yield content
                                
                            # Check for completion
                            finish_reason = choice.get("finish_reason")
                            if finish_reason == "stop":
                                break
                            
                except json.JSONDecodeError as e:
                    self.logger.warning(f"Invalid JSON in stream: {e}")
                    continue
                except Exception as e:
                    self.logger.warning(f"Error processing stream line: {e}")
                    continue
                    
        except Exception as e:
            self.logger.error(f"Error parsing streaming response: {e}")
            
        # Add assistant message to history if we got content
        if assistant_message.strip():
            self.add_message("assistant", assistant_message)

    def _parse_non_streaming_response(self, response: requests.Response) -> str:
        """Parse non-streaming response"""
        try:
            data = response.json()
            
            # Extract message content
            choices = data.get("choices", [])
            if choices:
                message = choices[0].get("message", {})
                # Handle structured content format
                content_array = message.get("content", [])
                if isinstance(content_array, list) and content_array:
                    content = content_array[0].get("text", "")
                else:
                    content = message.get("content", "")
                    
                if content:
                    self.add_message("assistant", content)
                    return content
                                
            return "No response content received"
            
        except Exception as e:
            self.logger.error(f"Error parsing non-streaming response: {e}")
            return f"Error parsing response: {e}"

    def call_api(self, new_message: str, override_config: Optional[Dict[str, Any]] = None) -> Generator[str, None, None]:
        """Call OpenAI API with the new message"""
        try:
            # Add user message to history
            self.add_message("user", new_message)
            
            # Build API payload
            payload = self._build_api_payload(new_message, override_config)
            
            self.logger.info(f"Making API call to {self.api_url}")
            self.logger.debug(f"Payload: {json.dumps(payload, indent=2)}")
            
            # Show model and reasoning info to user
            model = payload.get("model", self.config.model)
            reasoning_effort = payload.get("reasoning_effort", "medium")
            model_display = SUPPORTED_MODELS.get(model, {}).get('name', model)
            
            if reasoning_effort in ["medium", "high"]:
                try:
                    from colorama import Fore, Style
                except ImportError:
                    class Fore:
                        YELLOW = RESET_ALL = ""
                    class Style:
                        RESET_ALL = ""
                
                timeout = self._get_timeout_for_reasoning(model, reasoning_effort)
                print(f"{Fore.YELLOW}🤖 Using {model_display} with {reasoning_effort.upper()} reasoning (timeout: {timeout//60}min {timeout%60}s)...{Style.RESET_ALL}")
            
            # Make request
            response = self._make_api_request(payload)
            
            # Handle streaming vs non-streaming
            if payload.get("stream", True):
                yield from self._parse_streaming_response(response)
            else:
                result = self._parse_non_streaming_response(response)
                yield result
                
        except Exception as e:
            error_msg = f"API call failed: {e}"
            self.logger.error(error_msg)
            yield error_msg

    def clear_history(self):
        """Clear conversation history"""
        create_backup(self.base_dir / "history.json", self.base_dir / "backups", self.logger)
        self.messages.clear()
        self._save_history()
        self.logger.info("Conversation history cleared")

    def get_statistics(self) -> Dict[str, Any]:
        """Get conversation statistics"""
        if not self.messages:
            return {
                "total_messages": 0,
                "user_messages": 0,
                "assistant_messages": 0,
                "total_characters": 0,
                "average_message_length": 0,
                "first_message": None,
                "last_message": None,
                "conversation_duration": None
            }
            
        user_msgs = [m for m in self.messages if m["role"] == "user"]
        assistant_msgs = [m for m in self.messages if m["role"] == "assistant"]
        
        total_chars = sum(len(m["content"]) for m in self.messages)
        avg_length = total_chars // len(self.messages) if self.messages else 0
        
        first_time = datetime.fromisoformat(self.messages[0]["timestamp"])
        last_time = datetime.fromisoformat(self.messages[-1]["timestamp"])
        duration = last_time - first_time
        
        return {
            "total_messages": len(self.messages),
            "user_messages": len(user_msgs),
            "assistant_messages": len(assistant_msgs),
            "total_characters": total_chars,
            "average_message_length": avg_length,
            "first_message": first_time.strftime("%Y-%m-%d %H:%M:%S"),
            "last_message": last_time.strftime("%Y-%m-%d %H:%M:%S"),
            "conversation_duration": str(duration).split('.')[0] if duration.total_seconds() > 0 else "0:00:00"
        }

    def search_history(self, term: str, limit: int = 10) -> List[Dict[str, Any]]:
        """Search conversation history for a term"""
        results = []
        term_lower = term.lower()
        
        for i, msg in enumerate(self.messages):
            if term_lower in msg["content"].lower():
                results.append({
                    "index": i,
                    "message": msg,
                    "preview": msg["content"][:100] + "..." if len(msg["content"]) > 100 else msg["content"]
                })
                
            if len(results) >= limit:
                break
                
        return results

    def list_files(self) -> List[str]:
        """List available files for inclusion"""
        return list_available_files(self.base_dir)