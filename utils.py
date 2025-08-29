#!/usr/bin/env python3
"""
Utility functions for OpenAI GPT Chat Agents

This module provides common utilities for file handling, logging, and other shared functionality.
"""

import os
import json
import logging
import shutil
import re
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any, Optional
from config import SUPPORTED_EXTENSIONS


def setup_directories(base_dir: Path) -> None:
    """Create necessary directory structure"""
    directories = [
        base_dir,
        base_dir / "backups",
        base_dir / "logs",
        base_dir / "exports",
        base_dir / "uploads"
    ]
    
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)


def setup_logging(agent_id: str, base_dir: Path) -> logging.Logger:
    """Configure logging to file and console"""
    log_file = base_dir / "logs" / f"{datetime.now().strftime('%Y-%m-%d')}.log"
    
    # Create logger
    logger = logging.getLogger(f"OpenAIGPTAgent_{agent_id}")
    logger.setLevel(logging.INFO)
    
    # Remove existing handlers
    logger.handlers.clear()
    
    # File handler
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    file_handler.setFormatter(file_formatter)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_formatter = logging.Formatter('%(levelname)s: %(message)s')
    console_handler.setFormatter(console_formatter)
    console_handler.setLevel(logging.WARNING)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger


def create_backup(history_file: Path, backup_dir: Path, logger: logging.Logger) -> None:
    """Create rolling backup of history"""
    if not history_file.exists():
        return
        
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = backup_dir / f"history_{timestamp}.json"
    
    try:
        shutil.copy2(history_file, backup_file)
        
        # Keep only last 10 backups
        backups = sorted(backup_dir.glob("history_*.json"))
        while len(backups) > 10:
            oldest = backups.pop(0)
            oldest.unlink()
            
    except Exception as e:
        logger.error(f"Error creating backup: {e}")


def is_supported_file(file_path: Path) -> bool:
    """Check if file extension is supported for inclusion"""
    if file_path.suffix.lower() in SUPPORTED_EXTENSIONS:
        return True
    
    # Check for files without extensions but with known names
    known_files = {
        'makefile', 'dockerfile', 'rakefile', 'gemfile', 'podfile',
        'readme', 'license', 'changelog', 'authors', 'contributors',
        'todo', 'manifest', 'requirements', 'pipfile', 'poetry'
    }
    
    return file_path.name.lower() in known_files


def process_file_inclusions(content: str, base_dir: Path, logger: logging.Logger) -> str:
    """Replace {filename} patterns with file contents"""
    def replace_file(match):
        filename = match.group(1)
        
        # Search paths
        search_paths = [
            Path('.'),
            Path('src'),
            Path('lib'),
            Path('scripts'),
            Path('data'),
            Path('documents'),
            Path('files'),
            Path('config'),
            Path('configs'),
            base_dir / 'uploads'
        ]
        
        for search_path in search_paths:
            file_path = search_path / filename
            if file_path.exists() and file_path.is_file():
                
                # Check if file is supported
                if not is_supported_file(file_path):
                    logger.warning(f"Unsupported file type: {filename}")
                    return f"[WARNING: Unsupported file type {filename}]"
                
                try:
                    # Check file size (limit to 2MB for programming files)
                    max_size = 2 * 1024 * 1024  # 2MB
                    if file_path.stat().st_size > max_size:
                        logger.error(f"File {filename} too large (>2MB)")
                        return f"[ERROR: File {filename} too large (max 2MB)]"
                    
                    # Try multiple encodings for robust file reading
                    file_content = None
                    encodings_to_try = ['utf-8', 'utf-8-sig', 'latin-1', 'cp1252', 'iso-8859-1']
                    
                    for encoding in encodings_to_try:
                        try:
                            with open(file_path, 'r', encoding=encoding) as f:
                                file_content = f.read()
                                break
                        except (UnicodeDecodeError, UnicodeError):
                            continue
                    
                    if file_content is None:
                        # Final fallback - read as binary and decode with errors='replace'
                        try:
                            with open(file_path, 'rb') as f:
                                raw_content = f.read()
                                file_content = raw_content.decode('utf-8', errors='replace')
                                logger.warning(f"File {filename} contained non-standard encoding, some characters may be garbled")
                        except Exception as e:
                            logger.error(f"Could not read file {filename} with any encoding: {e}")
                            return f"[ERROR: Could not decode file {filename}]"
                    
                    # Add file info header for programming files
                    file_info = f"// File: {filename} ({file_path.suffix})\n"
                    if file_path.suffix.lower() in ['.py', '.r']:
                        file_info = f"# File: {filename} ({file_path.suffix})\n"
                    elif file_path.suffix.lower() in ['.html', '.xml']:
                        file_info = f"<!-- File: {filename} ({file_path.suffix}) -->\n"
                    elif file_path.suffix.lower() in ['.css', '.scss', '.sass']:
                        file_info = f"/* File: {filename} ({file_path.suffix}) */\n"
                    elif file_path.suffix.lower() in ['.sql']:
                        file_info = f"-- File: {filename} ({file_path.suffix})\n"
                    
                    full_content = file_info + file_content
                    
                    logger.info(f"Included file: {filename} ({len(file_content)} chars, {file_path.suffix})")
                    return full_content
                    
                except Exception as e:
                    logger.error(f"Error reading file {filename}: {e}")
                    return f"[ERROR: Could not read {filename}: {e}]"
        
        logger.warning(f"File not found: {filename}")
        return f"[ERROR: File {filename} not found]"
    
    return re.sub(r'\{([^}]+)\}', replace_file, content)


def get_api_key(model: str, base_dir: Path, logger: logging.Logger) -> str:
    """Get API key from environment or secrets file, prompt if needed"""
    try:
        from colorama import Fore, Style
    except ImportError:
        class Fore:
            RED = GREEN = YELLOW = BLUE = MAGENTA = CYAN = WHITE = RESET = ""
        class Style:
            BRIGHT = DIM = RESET_ALL = ""
    
    # First try environment variable
    api_key = os.getenv('OPENAI_API_KEY')
    if api_key:
        logger.info("Using API key from environment variable")
        return api_key
        
    # Try secrets file
    secrets_file = base_dir / "secrets.json"
    if secrets_file.exists():
        try:
            with open(secrets_file, 'r') as f:
                secrets = json.load(f)
                keys = secrets.get('keys', {})
                # Use model-specific key or default
                api_key = keys.get(model) or keys.get('default')
                if api_key:
                    logger.info("Using API key from secrets file")
                    return api_key
        except Exception as e:
            logger.error(f"Error reading secrets file: {e}")
    
    # Prompt user for API key
    from config import SUPPORTED_MODELS
    model_display = SUPPORTED_MODELS.get(model, {}).get('name', model)
    print(f"{Fore.YELLOW}API key not found for OpenAI {model_display} model.")
    print(f"You can set the OPENAI_API_KEY environment variable or enter it now.{Style.RESET_ALL}")
    
    api_key = input(f"{Fore.CYAN}Enter API key for OpenAI {model_display}: {Style.RESET_ALL}").strip()
    
    if not api_key:
        raise ValueError("API key is required")
        
    # Save to secrets file
    secrets = {
        "provider": "openai",
        "keys": {
            "default": api_key,
            model: api_key
        }
    }
    
    try:
        with open(secrets_file, 'w') as f:
            json.dump(secrets, f, indent=2)
        
        # Add to .gitignore
        gitignore_file = Path('.gitignore')
        gitignore_content = ""
        if gitignore_file.exists():
            gitignore_content = gitignore_file.read_text()
        
        if 'secrets.json' not in gitignore_content:
            with open(gitignore_file, 'a') as f:
                f.write('\n# API Keys\n**/secrets.json\nsecrets.json\n')
                
        masked_key = f"{api_key[:4]}...{api_key[-2:]}" if len(api_key) > 6 else "***"
        print(f"{Fore.GREEN}API key saved ({masked_key}){Style.RESET_ALL}")
        logger.info(f"API key saved for user (length: {len(api_key)})")
        
    except Exception as e:
        logger.error(f"Error saving API key: {e}")
        print(f"{Fore.RED}Warning: Could not save API key to file{Style.RESET_ALL}")
        
    return api_key


def list_available_files(base_dir: Path) -> List[str]:
    """List available files for inclusion"""
    files = []
    search_paths = [
        Path('.'),
        Path('src'),
        Path('lib'),
        Path('scripts'),
        Path('data'),
        Path('documents'),
        Path('files'),
        Path('config'),
        Path('configs'),
        base_dir / 'uploads'
    ]
    
    for search_path in search_paths:
        if search_path.exists():
            for file_path in search_path.rglob("*"):
                if (file_path.is_file() and
                    not file_path.name.startswith('.') and
                    is_supported_file(file_path)):
                    
                    size = file_path.stat().st_size
                    size_str = f"{size:,} bytes" if size < 1024*1024 else f"{size/(1024*1024):.1f} MB"
                    files.append(f"{file_path} ({size_str}) [{file_path.suffix}]")
                    
    return sorted(files)