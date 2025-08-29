#!/usr/bin/env python3
"""
Configuration module for OpenAI GPT Chat Agents

This module provides unified configuration management for all GPT model variants.
"""

from dataclasses import dataclass, asdict
from typing import Optional
from datetime import datetime


@dataclass
class AgentConfig:
    """Unified configuration settings for OpenAI GPT Chat Agents"""
    model: str = "gpt-5"
    temperature: float = 1.0
    reasoning_effort: str = "medium"  # low, medium, high
    reasoning_summary: str = "auto"   # auto, detailed, none
    max_output_tokens: Optional[int] = None
    max_history_size: int = 1000
    stream: bool = True
    system_prompt: Optional[str] = None
    store: bool = True
    text_format: str = "text"
    text_verbosity: str = "medium"  # low, medium, high
    top_p: float = 1.0
    parallel_tool_calls: bool = True
    tool_choice: str = "auto"
    created_at: str = ""
    updated_at: str = ""

    def __post_init__(self):
        if not self.created_at:
            self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()


# Model definitions with specifications
SUPPORTED_MODELS = {
    "gpt-5": {
        "name": "GPT-5",
        "description": "Full-featured GPT-5 model with advanced reasoning capabilities",
        "reasoning_timeout": {"low": 180, "medium": 360, "high": 720}  # 3, 6, 12 minutes
    },
    "gpt-5-mini": {
        "name": "GPT-5 Mini", 
        "description": "Compact GPT-5 model balancing performance and efficiency",
        "reasoning_timeout": {"low": 90, "medium": 180, "high": 360}   # 1.5, 3, 6 minutes
    },
    "gpt-5-nano": {
        "name": "GPT-5 Nano",
        "description": "Lightweight GPT-5 model optimized for speed",
        "reasoning_timeout": {"low": 60, "medium": 120, "high": 240}   # 1, 2, 4 minutes
    }
}

# Programming and common file extensions supported for file inclusion
SUPPORTED_EXTENSIONS = {
    # Programming languages
    '.py', '.r', '.js', '.ts', '.jsx', '.tsx', '.java', '.c', '.cpp', '.cc', '.cxx',
    '.h', '.hpp', '.cs', '.php', '.rb', '.go', '.rs', '.swift', '.kt', '.scala',
    '.clj', '.hs', '.ml', '.fs', '.vb', '.pl', '.pm', '.sh', '.bash', '.zsh', '.fish',
    '.ps1', '.bat', '.cmd', '.sql', '.html', '.htm', '.css', '.scss', '.sass', '.less',
    '.xml', '.xsl', '.xslt', '.json', '.yaml', '.yml', '.toml', '.ini', '.cfg', '.conf',
    '.properties', '.env', '.dockerfile', '.docker', '.makefile', '.cmake', '.gradle',
    '.sbt', '.pom', '.lock', '.mod', '.sum',
    
    # Data and markup
    '.md', '.markdown', '.rst', '.tex', '.latex', '.csv', '.tsv', '.jsonl', '.ndjson',
    '.xml', '.svg', '.rss', '.atom', '.plist',
    
    # Configuration and infrastructure
    '.tf', '.tfvars', '.hcl', '.nomad', '.consul', '.vault', '.k8s', '.kubectl',
    '.helm', '.kustomize', '.ansible', '.inventory', '.playbook',
    
    # Documentation and text
    '.txt', '.log', '.out', '.err', '.trace', '.debug', '.info', '.warn', '.error',
    '.readme', '.license', '.changelog', '.authors', '.contributors', '.todo',
    
    # Notebooks and scripts
    '.ipynb', '.rmd', '.qmd', '.jl', '.m', '.octave', '.R', '.Rmd',
    
    # Web and API
    '.graphql', '.gql', '.rest', '.http', '.api', '.postman', '.insomnia',
    
    # Other useful formats
    '.editorconfig', '.gitignore', '.gitattributes', '.dockerignore', '.eslintrc',
    '.prettierrc', '.babelrc', '.webpack', '.rollup', '.vite', '.parcel'
}