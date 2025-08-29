#!/usr/bin/env python3
"""
OpenAI GPT Unified Chat Agent - Advanced Production-Ready Chat Interface

This is the main unified program that combines all OpenAI GPT agent implementations
into a single, professional CLI application with enhanced user experience.

Features:
- Support for all GPT-5 model variants (GPT-5, GPT-5-mini, GPT-5-nano)
- Enhanced CLI with legendary user experience
- Persistent conversation history with rolling backups
- Streaming and non-streaming response support
- File inclusion in messages via {filename} syntax
- Advanced configuration management
- Comprehensive logging and statistics
- Export capabilities (JSON, TXT, MD, HTML)
- Secure API key management
- Interactive CLI with beautiful colored output

Example Usage:
    # Start interactive chat with GPT-5
    python main.py --agent-id my-agent --model gpt-5

    # Use GPT-5 Mini for faster responses
    python main.py --agent-id my-agent --model gpt-5-mini

    # List all agents
    python main.py --list

    # Export conversation
    python main.py --agent-id my-agent --export html

    # Configure agent settings
    python main.py --agent-id my-agent --config
"""

import sys
import json
import yaml
import argparse
from pathlib import Path
from datetime import datetime
from dataclasses import asdict

from config import AgentConfig, SUPPORTED_MODELS
from agent import OpenAIGPTChatAgent
from export import export_conversation

try:
    from colorama import Fore, Style, init as colorama_init
    colorama_init(autoreset=True)
except ImportError:
    # Fallback if colorama is not available
    class Fore:
        RED = GREEN = YELLOW = BLUE = MAGENTA = CYAN = WHITE = RESET = ""
    class Style:
        BRIGHT = DIM = RESET_ALL = ""


def print_banner():
    """Display beautiful ASCII banner"""
    banner = f"""
{Fore.CYAN}╔════════════════════════════════════════════════════════════════════════════════╗
║                                                                                ║
║   {Fore.WHITE}🤖 {Style.BRIGHT}OpenAI GPT Unified Chat Agent{Style.RESET_ALL}{Fore.CYAN}                                      ║
║                                                                                ║
║   {Fore.GREEN}✨ Professional AI Chat Experience with Multiple GPT Models{Fore.CYAN}              ║
║                                                                                ║
║   {Fore.YELLOW}Supported Models:{Fore.CYAN}                                                           ║
║   {Fore.WHITE}• GPT-5{Fore.CYAN}       - Full-featured with advanced reasoning                     ║
║   {Fore.WHITE}• GPT-5 Mini{Fore.CYAN}  - Balanced performance and efficiency                       ║
║   {Fore.WHITE}• GPT-5 Nano{Fore.CYAN}  - Lightweight and optimized for speed                      ║
║                                                                                ║
╚════════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
"""
    print(banner)


def list_agents():
    """List all available agents with enhanced formatting"""
    agents_dir = Path("agents")
    agents = []
    
    if not agents_dir.exists():
        print(f"\n{Fore.YELLOW}📂 No agents directory found. Create your first agent to get started!{Style.RESET_ALL}\n")
        return
        
    for agent_dir in agents_dir.iterdir():
        if agent_dir.is_dir():
            config_file = agent_dir / "config.yaml"
            history_file = agent_dir / "history.json"
            
            # Get basic info
            agent_info = {
                "id": agent_dir.name,
                "path": str(agent_dir),
                "exists": True
            }
            
            # Get config info
            if config_file.exists():
                try:
                    with open(config_file) as f:
                        config = yaml.safe_load(f)
                        agent_info["model"] = config.get("model", "gpt-5")
                        agent_info["created_at"] = config.get("created_at")
                        agent_info["updated_at"] = config.get("updated_at")
                        agent_info["temperature"] = config.get("temperature", 1.0)
                        agent_info["reasoning_effort"] = config.get("reasoning_effort", "medium")
                except:
                    agent_info["model"] = "gpt-5"
                    agent_info["created_at"] = "Unknown"
                    agent_info["updated_at"] = "Unknown"
                    agent_info["temperature"] = 1.0
                    agent_info["reasoning_effort"] = "medium"
            else:
                agent_info["model"] = "gpt-5"
                agent_info["created_at"] = "Unknown"
                agent_info["updated_at"] = "Unknown"
                agent_info["temperature"] = 1.0
                agent_info["reasoning_effort"] = "medium"
                
            # Get history size
            if history_file.exists():
                try:
                    with open(history_file) as f:
                        history = json.load(f)
                        agent_info["message_count"] = len(history)
                        agent_info["history_size"] = history_file.stat().st_size
                except:
                    agent_info["message_count"] = 0
                    agent_info["history_size"] = 0
            else:
                agent_info["message_count"] = 0
                agent_info["history_size"] = 0
                
            agents.append(agent_info)
    
    if not agents:
        print(f"\n{Fore.YELLOW}📂 No agents found. Create your first agent to get started!{Style.RESET_ALL}\n")
        return
        
    # Sort by last updated
    agents = sorted(agents, key=lambda x: x.get("updated_at", ""), reverse=True)
    
    print(f"\n{Fore.CYAN}🤖 Available AI Agents:{Style.RESET_ALL}\n")
    print(f"{Fore.WHITE}{Style.BRIGHT}{'Agent ID':<20} {'Model':<15} {'Messages':<10} {'Size':<10} {'Last Updated':<20}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'─' * 85}{Style.RESET_ALL}")
    
    for agent in agents:
        updated = agent.get("updated_at", "Unknown")
        if updated != "Unknown":
            try:
                updated = datetime.fromisoformat(updated).strftime("%Y-%m-%d %H:%M")
            except:
                pass
        
        model = agent.get('model', 'gpt-5')
        model_display = SUPPORTED_MODELS.get(model, {}).get('name', model)
        
        # Format file size
        size = agent.get('history_size', 0)
        size_str = f"{size:,}B" if size < 1024 else f"{size/1024:.1f}K"
        
        # Color code by model
        model_color = Fore.GREEN if model == 'gpt-5' else Fore.BLUE if model == 'gpt-5-mini' else Fore.YELLOW
        
        print(f"{Fore.WHITE}{agent['id']:<20} {model_color}{model_display:<15} {Fore.WHITE}{agent.get('message_count', 0):<10} {size_str:<10} {updated:<20}{Style.RESET_ALL}")
    
    print(f"\n{Fore.GREEN}💡 Tip: Use --agent-id <id> --model <model> to start a chat session{Style.RESET_ALL}\n")


def show_agent_info(agent_id: str):
    """Display detailed agent information with enhanced formatting"""
    agent_dir = Path(f"agents/{agent_id}")
    
    if not agent_dir.exists():
        print(f"\n{Fore.RED}❌ Agent '{agent_id}' not found{Style.RESET_ALL}\n")
        return
        
    print(f"\n{Fore.CYAN}╔════════════════════════════════════════════════════════════════╗")
    print(f"║  {Fore.WHITE}{Style.BRIGHT}🤖 Agent Information: {Fore.YELLOW}{agent_id:<35}{Style.RESET_ALL}{Fore.CYAN} ║")
    print(f"╚════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}")
    
    # Load and display config
    config_file = agent_dir / "config.yaml"
    if config_file.exists():
        try:
            with open(config_file) as f:
                config = yaml.safe_load(f)
                
            model = config.get('model', 'gpt-5')
            model_info = SUPPORTED_MODELS.get(model, {})
            model_display = model_info.get('name', model)
            
            print(f"\n{Fore.GREEN}⚙️  Configuration:")
            print(f"   {Fore.WHITE}Model: {Fore.CYAN}{model} ({model_display})")
            print(f"   {Fore.WHITE}Description: {Fore.YELLOW}{model_info.get('description', 'N/A')}")
            print(f"   {Fore.WHITE}Temperature: {Fore.CYAN}{config.get('temperature', 1.0)}")
            print(f"   {Fore.WHITE}Reasoning Effort: {Fore.CYAN}{config.get('reasoning_effort', 'medium')}")
            
            # Show timeout for current config
            timeouts = model_info.get('reasoning_timeout', {})
            current_timeout = timeouts.get(config.get('reasoning_effort', 'medium'), 300)
            print(f"   {Fore.WHITE}Reasoning Timeout: {Fore.CYAN}{current_timeout}s ({current_timeout//60}min {current_timeout%60}s)")
            
            print(f"   {Fore.WHITE}Streaming: {Fore.CYAN}{config.get('stream', True)}")
            print(f"   {Fore.WHITE}Created: {Fore.CYAN}{config.get('created_at', 'Unknown')}")
            print(f"   {Fore.WHITE}Updated: {Fore.CYAN}{config.get('updated_at', 'Unknown')}")
                
        except Exception as e:
            print(f"   {Fore.RED}Error loading config: {e}")
    
    # Display history stats
    history_file = agent_dir / "history.json"
    if history_file.exists():
        try:
            with open(history_file) as f:
                history = json.load(f)
                    
            user_msgs = len([m for m in history if m.get("role") == "user"])
            assistant_msgs = len([m for m in history if m.get("role") == "assistant"])
            total_chars = sum(len(m.get("content", "")) for m in history)
            
            print(f"\n{Fore.GREEN}💬 Conversation History:")
            print(f"   {Fore.WHITE}Total Messages: {Fore.CYAN}{len(history):,}")
            print(f"   {Fore.WHITE}User Messages: {Fore.CYAN}{user_msgs:,}")
            print(f"   {Fore.WHITE}Assistant Messages: {Fore.CYAN}{assistant_msgs:,}")
            print(f"   {Fore.WHITE}Total Characters: {Fore.CYAN}{total_chars:,}")
            print(f"   {Fore.WHITE}File Size: {Fore.CYAN}{history_file.stat().st_size:,} bytes")
                
            if history:
                first_msg = datetime.fromisoformat(history[0]["timestamp"])
                last_msg = datetime.fromisoformat(history[-1]["timestamp"])
                duration = last_msg - first_msg
                print(f"   {Fore.WHITE}First Message: {Fore.CYAN}{first_msg.strftime('%Y-%m-%d %H:%M:%S')}")
                print(f"   {Fore.WHITE}Last Message: {Fore.CYAN}{last_msg.strftime('%Y-%m-%d %H:%M:%S')}")
                print(f"   {Fore.WHITE}Duration: {Fore.CYAN}{str(duration).split('.')[0]}")
                    
        except Exception as e:
            print(f"   {Fore.RED}Error loading history: {e}")
    else:
        print(f"\n{Fore.YELLOW}📝 No conversation history found")
        
    # Display directory structure
    print(f"\n{Fore.GREEN}📁 Directory Structure:")
    for item in sorted(agent_dir.rglob("*")):
        if item.is_file():
            size = item.stat().st_size
            size_str = f"{size:,}B" if size < 1024 else f"{size/1024:.1f}K" if size < 1024*1024 else f"{size/(1024*1024):.1f}M"
            rel_path = item.relative_to(agent_dir)
            print(f"   {Fore.WHITE}{rel_path} {Fore.CYAN}({size_str})")
    
    print()


def create_agent_config_interactive(model: str) -> AgentConfig:
    """Interactive configuration creation with enhanced UI"""
    print(f"\n{Fore.CYAN}╔════════════════════════════════════════════════════════════════╗")
    print(f"║  {Fore.WHITE}{Style.BRIGHT}⚙️  Creating Agent Configuration{Style.RESET_ALL}{Fore.CYAN}                             ║")
    print(f"╚════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}💡 Press Enter to use default values{Style.RESET_ALL}\n")
    
    config = AgentConfig(model=model)
    
    # Display selected model info
    model_info = SUPPORTED_MODELS.get(model, {})
    print(f"{Fore.GREEN}🤖 Selected Model: {Fore.CYAN}{model_info.get('name', model)}")
    print(f"   {Fore.WHITE}Description: {Fore.YELLOW}{model_info.get('description', 'N/A')}")
    
    timeouts = model_info.get("reasoning_timeout", {})
    print(f"   {Fore.WHITE}Reasoning Timeouts:")
    print(f"     {Fore.WHITE}• Low: {Fore.CYAN}{timeouts.get('low', 60)}s")
    print(f"     {Fore.WHITE}• Medium: {Fore.CYAN}{timeouts.get('medium', 120)}s") 
    print(f"     {Fore.WHITE}• High: {Fore.CYAN}{timeouts.get('high', 240)}s")
    print()
    
    # Temperature
    temp_input = input(f"{Fore.WHITE}🌡️  Temperature (0.0-2.0) [{Fore.CYAN}{config.temperature}{Fore.WHITE}]: {Style.RESET_ALL}").strip()
    if temp_input:
        try:
            temp_val = float(temp_input)
            if 0.0 <= temp_val <= 2.0:
                config.temperature = temp_val
            else:
                print(f"   {Fore.RED}⚠️  Temperature must be between 0.0 and 2.0, using default{Style.RESET_ALL}")
        except ValueError:
            print(f"   {Fore.RED}⚠️  Invalid temperature, using default{Style.RESET_ALL}")
    
    # Reasoning effort
    effort_input = input(f"{Fore.WHITE}🧠 Reasoning effort (low/medium/high) [{Fore.CYAN}{config.reasoning_effort}{Fore.WHITE}]: {Style.RESET_ALL}").strip()
    if effort_input and effort_input in ["low", "medium", "high"]:
        config.reasoning_effort = effort_input
        
        # Show timeout for selected effort
        timeout = timeouts.get(config.reasoning_effort, 300)
        print(f"   {Fore.GREEN}✅ Timeout for {config.reasoning_effort} effort: {timeout}s ({timeout//60}min {timeout%60}s){Style.RESET_ALL}")
    
    # Reasoning summary
    summary_input = input(f"{Fore.WHITE}📋 Reasoning summary (auto/detailed/none) [{Fore.CYAN}{config.reasoning_summary}{Fore.WHITE}]: {Style.RESET_ALL}").strip()
    if summary_input and summary_input in ["auto", "detailed", "none"]:
        config.reasoning_summary = summary_input
    
    # System prompt
    system_prompt = input(f"{Fore.WHITE}💬 System prompt (optional): {Style.RESET_ALL}").strip()
    if system_prompt:
        config.system_prompt = system_prompt
    
    # Max output tokens
    tokens_input = input(f"{Fore.WHITE}🎯 Max output tokens (optional): {Style.RESET_ALL}").strip()
    if tokens_input:
        try:
            config.max_output_tokens = int(tokens_input)
        except ValueError:
            print(f"   {Fore.RED}⚠️  Invalid token count, leaving unset{Style.RESET_ALL}")
    
    # Streaming
    stream_input = input(f"{Fore.WHITE}🌊 Enable streaming (y/n) [{Fore.CYAN}{'y' if config.stream else 'n'}{Fore.WHITE}]: {Style.RESET_ALL}").strip().lower()
    if stream_input in ['n', 'no', 'false']:
        config.stream = False
    elif stream_input in ['y', 'yes', 'true']:
        config.stream = True
    
    print(f"\n{Fore.GREEN}✅ Configuration created successfully!{Style.RESET_ALL}\n")
    return config


def interactive_chat(agent: OpenAIGPTChatAgent):
    """Enhanced interactive chat session with beautiful UI"""
    model_info = SUPPORTED_MODELS.get(agent.config.model, {})
    model_display = model_info.get('name', agent.config.model)
    
    # Chat header
    print(f"\n{Fore.CYAN}╔════════════════════════════════════════════════════════════════╗")
    print(f"║  {Fore.WHITE}{Style.BRIGHT}💬 Interactive Chat Session{Style.RESET_ALL}{Fore.CYAN}                                  ║")
    print(f"╚════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}")
    print(f"{Fore.GREEN}🤖 Model: {Fore.CYAN}{model_display}")
    print(f"{Fore.GREEN}👤 Agent: {Fore.YELLOW}{agent.agent_id}")
    print(f"{Fore.GREEN}🌡️  Temperature: {Fore.CYAN}{agent.config.temperature}")
    print(f"{Fore.GREEN}🧠 Reasoning: {Fore.CYAN}{agent.config.reasoning_effort}")
    print(f"\n{Fore.YELLOW}💡 Type '/help' for commands, '/quit' to exit{Style.RESET_ALL}\n")
    
    while True:
        try:
            user_input = input(f"{Fore.CYAN}{Style.BRIGHT}You: {Style.RESET_ALL}").strip()
            
            if not user_input:
                continue
                
            # Handle commands
            if user_input.startswith('/'):
                command_parts = user_input[1:].split()
                command = command_parts[0].lower()
                
                if command == 'help':
                    print(f"\n{Fore.YELLOW}📋 Available Commands:")
                    print(f"{Fore.WHITE}/help{Fore.CYAN} - Show this help message")
                    print(f"{Fore.WHITE}/history [n]{Fore.CYAN} - Show last n messages (default 5)")
                    print(f"{Fore.WHITE}/search <term>{Fore.CYAN} - Search conversation history")
                    print(f"{Fore.WHITE}/stats{Fore.CYAN} - Show conversation statistics")
                    print(f"{Fore.WHITE}/config{Fore.CYAN} - Show current configuration")
                    print(f"{Fore.WHITE}/export <json|txt|md|html>{Fore.CYAN} - Export conversation")
                    print(f"{Fore.WHITE}/clear{Fore.CYAN} - Clear conversation history")
                    print(f"{Fore.WHITE}/files{Fore.CYAN} - List available files for inclusion")
                    print(f"{Fore.WHITE}/info{Fore.CYAN} - Show agent information")
                    print(f"{Fore.WHITE}/quit{Fore.CYAN} - Exit chat{Style.RESET_ALL}\n")
                    print(f"{Fore.GREEN}📁 File Inclusion: {Fore.WHITE}Use {{filename}} in messages to include file contents")
                    print(f"{Fore.GREEN}🎯 Supported: {Fore.WHITE}Programming files (.py, .js, etc.), config files, documentation{Style.RESET_ALL}\n")
                    
                    # Show model info
                    print(f"{Fore.YELLOW}⚡ Current Model Details:")
                    print(f"   {Fore.WHITE}🤖 {model_display} ({agent.config.model})")
                    print(f"   {Fore.WHITE}📝 {model_info.get('description', 'N/A')}")
                    timeouts = model_info.get("reasoning_timeout", {})
                    print(f"   {Fore.WHITE}⏱️  Timeouts: Low={timeouts.get('low', 60)}s, Medium={timeouts.get('medium', 120)}s, High={timeouts.get('high', 240)}s")
                    print()
                    
                elif command == 'history':
                    limit = 5
                    if len(command_parts) > 1:
                        try:
                            limit = int(command_parts[1])
                        except ValueError:
                            print(f"{Fore.RED}❌ Invalid number{Style.RESET_ALL}")
                            continue
                    
                    recent_messages = agent.messages[-limit:]
                    if not recent_messages:
                        print(f"{Fore.YELLOW}📝 No messages in history{Style.RESET_ALL}")
                    else:
                        print(f"\n{Fore.YELLOW}📜 Last {len(recent_messages)} messages:")
                        for msg in recent_messages:
                            timestamp = datetime.fromisoformat(msg["timestamp"]).strftime("%H:%M:%S")
                            role_color = Fore.CYAN if msg["role"] == "user" else Fore.GREEN
                            role_icon = "👤" if msg["role"] == "user" else "🤖"
                            content_preview = msg['content'][:100] + "..." if len(msg['content']) > 100 else msg['content']
                            print(f"   {Fore.WHITE}[{timestamp}] {role_color}{role_icon} {msg['role']}: {content_preview}{Style.RESET_ALL}")
                    print()
                    
                elif command == 'search':
                    if len(command_parts) < 2:
                        print(f"{Fore.RED}❌ Usage: /search <term>{Style.RESET_ALL}")
                        continue
                    
                    search_term = ' '.join(command_parts[1:])
                    results = agent.search_history(search_term)
                    
                    if not results:
                        print(f"{Fore.YELLOW}🔍 No matches found for '{search_term}'{Style.RESET_ALL}")
                    else:
                        print(f"\n{Fore.GREEN}🔍 Found {len(results)} matches for '{search_term}':")
                        for result in results:
                            msg = result["message"]
                            timestamp = datetime.fromisoformat(msg["timestamp"]).strftime("%H:%M:%S")
                            role_color = Fore.CYAN if msg["role"] == "user" else Fore.GREEN
                            role_icon = "👤" if msg["role"] == "user" else "🤖"
                            print(f"   {Fore.WHITE}[{timestamp}] {role_color}{role_icon} {msg['role']}: {result['preview']}{Style.RESET_ALL}")
                    print()
                    
                elif command == 'stats':
                    stats = agent.get_statistics()
                    print(f"\n{Fore.YELLOW}📊 Conversation Statistics:")
                    print(f"   {Fore.WHITE}🤖 Model: {Fore.CYAN}{agent.config.model} ({model_display})")
                    print(f"   {Fore.WHITE}💬 Total Messages: {Fore.CYAN}{stats['total_messages']:,}")
                    print(f"   {Fore.WHITE}👤 User Messages: {Fore.CYAN}{stats['user_messages']:,}")
                    print(f"   {Fore.WHITE}🤖 Assistant Messages: {Fore.CYAN}{stats['assistant_messages']:,}")
                    print(f"   {Fore.WHITE}📝 Total Characters: {Fore.CYAN}{stats['total_characters']:,}")
                    print(f"   {Fore.WHITE}📏 Avg Message Length: {Fore.CYAN}{stats['average_message_length']:,}")
                    if stats['first_message']:
                        print(f"   {Fore.WHITE}⏰ First Message: {Fore.CYAN}{stats['first_message']}")
                        print(f"   {Fore.WHITE}🕐 Last Message: {Fore.CYAN}{stats['last_message']}")
                        print(f"   {Fore.WHITE}⏱️  Duration: {Fore.CYAN}{stats['conversation_duration']}")
                    print()
                    
                elif command == 'config':
                    print(f"\n{Fore.YELLOW}⚙️  Current Configuration:")
                    config_dict = asdict(agent.config)
                    for key, value in config_dict.items():
                        if key not in ['created_at', 'updated_at']:
                            if key == 'model':
                                model_name = SUPPORTED_MODELS.get(str(value), {}).get('name', value)
                                print(f"   {Fore.WHITE}{key}: {Fore.CYAN}{value} ({model_name})")
                            elif key == 'reasoning_effort':
                                timeout = agent._get_timeout_for_reasoning(agent.config.model, str(value))
                                print(f"   {Fore.WHITE}{key}: {Fore.CYAN}{value} (timeout: {timeout}s)")
                            else:
                                print(f"   {Fore.WHITE}{key}: {Fore.CYAN}{value}")
                    print()
                    
                elif command == 'export':
                    if len(command_parts) < 2:
                        print(f"{Fore.RED}❌ Usage: /export <json|txt|md|html>{Style.RESET_ALL}")
                        continue
                    
                    format_type = command_parts[1].lower()
                    if format_type not in ['json', 'txt', 'md', 'html']:
                        print(f"{Fore.RED}❌ Invalid format. Use: json, txt, md, or html{Style.RESET_ALL}")
                        continue
                    
                    try:
                        filepath = export_conversation(agent, format_type)
                        print(f"{Fore.GREEN}✅ Exported to: {Fore.CYAN}{filepath}{Style.RESET_ALL}")
                    except Exception as e:
                        print(f"{Fore.RED}❌ Export failed: {e}{Style.RESET_ALL}")
                    
                elif command == 'clear':
                    confirm = input(f"{Fore.YELLOW}⚠️  Clear conversation history? (y/N): {Style.RESET_ALL}").strip().lower()
                    if confirm in ['y', 'yes']:
                        agent.clear_history()
                        print(f"{Fore.GREEN}✅ Conversation history cleared{Style.RESET_ALL}")
                    
                elif command == 'files':
                    files = agent.list_files()
                    if not files:
                        print(f"{Fore.YELLOW}📁 No supported files found for inclusion{Style.RESET_ALL}")
                    else:
                        print(f"\n{Fore.GREEN}📁 Available files for inclusion:")
                        for file_info in files[:20]:  # Limit to 20 files
                            print(f"   {Fore.WHITE}{file_info}")
                        if len(files) > 20:
                            print(f"   {Fore.YELLOW}... and {len(files) - 20} more files")
                    print(f"{Fore.GREEN}💡 Use {{filename}} in your message to include file contents{Style.RESET_ALL}\n")
                    
                elif command == 'info':
                    show_agent_info(agent.agent_id)
                    
                elif command in ['quit', 'exit', 'q']:
                    print(f"{Fore.GREEN}👋 Goodbye! Chat session ended.{Style.RESET_ALL}")
                    break
                    
                else:
                    print(f"{Fore.RED}❌ Unknown command: {command}")
                    print(f"{Fore.YELLOW}💡 Type '/help' for available commands{Style.RESET_ALL}")
                    
                continue
            
            # Regular message - send to API
            print(f"\n{Fore.GREEN}{Style.BRIGHT}🤖 Assistant: {Style.RESET_ALL}", end="", flush=True)
            
            response_text = ""
            for chunk in agent.call_api(user_input):
                print(chunk, end="", flush=True)
                response_text += chunk
            
            print("\n")
            
        except KeyboardInterrupt:
            print(f"\n{Fore.YELLOW}⚠️  Use '/quit' to exit gracefully{Style.RESET_ALL}")
        except Exception as e:
            print(f"\n{Fore.RED}❌ Error: {e}{Style.RESET_ALL}")


def main():
    """Main CLI interface with enhanced user experience"""
    # Print banner
    print_banner()
    
    parser = argparse.ArgumentParser(
        description="OpenAI GPT Unified Chat Agent - Professional AI Chat Interface",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"""
{Fore.YELLOW}Examples:{Style.RESET_ALL}
  {Fore.CYAN}%(prog)s --agent-id my-agent --model gpt-5{Style.RESET_ALL}
    Start interactive chat with GPT-5
    
  {Fore.CYAN}%(prog)s --agent-id my-agent --model gpt-5-mini{Style.RESET_ALL}
    Use GPT-5 Mini for faster responses
    
  {Fore.CYAN}%(prog)s --list{Style.RESET_ALL}
    List all available agents
    
  {Fore.CYAN}%(prog)s --agent-id my-agent --export html{Style.RESET_ALL}
    Export conversation as HTML
    
  {Fore.CYAN}%(prog)s --agent-id my-agent --config{Style.RESET_ALL}
    Configure agent interactively
        """
    )
    
    parser.add_argument("--agent-id", help="Agent ID for the chat session")
    parser.add_argument("--model", choices=list(SUPPORTED_MODELS.keys()), default="gpt-5",
                       help="GPT model to use (default: gpt-5)")
    parser.add_argument("--list", action="store_true", help="List all available agents")
    parser.add_argument("--info", metavar="ID", help="Show detailed information for agent")
    parser.add_argument("--config", action="store_true", help="Configure agent interactively")
    parser.add_argument("--effort", choices=["low", "medium", "high"], help="Override reasoning effort")
    parser.add_argument("--temperature", type=float, help="Override temperature (0.0-2.0)")
    parser.add_argument("--no-stream", action="store_true", help="Disable streaming")
    parser.add_argument("--export", choices=["json", "txt", "md", "html"], help="Export conversation format")
    
    args = parser.parse_args()
    
    # Handle list command
    if args.list:
        list_agents()
        return
    
    # Handle info command
    if args.info:
        show_agent_info(args.info)
        return
    
    # Require agent-id for other operations
    if not args.agent_id:
        print(f"{Fore.RED}❌ Error: --agent-id is required for chat operations{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}💡 Use --list to see available agents or create a new one{Style.RESET_ALL}")
        parser.print_help()
        return
    
    try:
        # Initialize agent
        print(f"{Fore.YELLOW}🚀 Initializing {SUPPORTED_MODELS[args.model]['name']} agent...{Style.RESET_ALL}")
        agent = OpenAIGPTChatAgent(args.agent_id, args.model)
        
        # Handle config command
        if args.config:
            new_config = create_agent_config_interactive(args.model)
            agent.config = new_config
            agent._save_config()
            print(f"{Fore.GREEN}✅ Configuration saved successfully{Style.RESET_ALL}")
            return
        
        # Handle export command
        if args.export:
            filepath = export_conversation(agent, args.export)
            print(f"{Fore.GREEN}✅ Exported to: {Fore.CYAN}{filepath}{Style.RESET_ALL}")
            return
        
        # Apply command line overrides
        overrides = {}
        if args.effort:
            overrides["reasoning_effort"] = args.effort
        if args.temperature is not None:
            if 0.0 <= args.temperature <= 2.0:
                overrides["temperature"] = args.temperature
            else:
                print(f"{Fore.RED}⚠️  Temperature must be between 0.0 and 2.0{Style.RESET_ALL}")
        if args.no_stream:
            overrides["stream"] = False
        
        # Start interactive chat
        if overrides:
            for key, value in overrides.items():
                setattr(agent.config, key, value)
            agent._save_config()
        
        interactive_chat(agent)
        
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}👋 Chat session interrupted by user{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}❌ Error: {e}{Style.RESET_ALL}")
        sys.exit(1)


if __name__ == "__main__":
    main()