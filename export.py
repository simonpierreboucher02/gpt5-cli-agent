#!/usr/bin/env python3
"""
Export functionality for OpenAI GPT Chat Agents

This module provides conversation export capabilities in multiple formats.
"""

import json
import html
from pathlib import Path
from datetime import datetime
from dataclasses import asdict
from typing import Dict, Any, List

from config import SUPPORTED_MODELS


def export_conversation(agent, format_type: str) -> str:
    """Export conversation to specified format"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    export_dir = agent.base_dir / "exports"
    
    if format_type == "json":
        return _export_json(agent, export_dir, timestamp)
    elif format_type == "txt":
        return _export_txt(agent, export_dir, timestamp)
    elif format_type == "md":
        return _export_md(agent, export_dir, timestamp)
    elif format_type == "html":
        return _export_html(agent, export_dir, timestamp)
    else:
        raise ValueError(f"Unsupported export format: {format_type}")


def _export_json(agent, export_dir: Path, timestamp: str) -> str:
    """Export conversation to JSON format"""
    filename = f"conversation_{timestamp}.json"
    filepath = export_dir / filename
    
    export_data = {
        "agent_id": agent.agent_id,
        "exported_at": datetime.now().isoformat(),
        "config": asdict(agent.config),
        "messages": agent.messages,
        "statistics": agent.get_statistics()
    }
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(export_data, f, indent=2, ensure_ascii=False)
    
    agent.logger.info(f"Exported conversation to {filepath}")
    return str(filepath)


def _export_txt(agent, export_dir: Path, timestamp: str) -> str:
    """Export conversation to TXT format"""
    filename = f"conversation_{timestamp}.txt"
    filepath = export_dir / filename
    
    model_display = SUPPORTED_MODELS.get(agent.config.model, {}).get('name', agent.config.model)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(f"OpenAI {model_display} Chat Agent Conversation Export\n")
        f.write(f"Agent ID: {agent.agent_id}\n")
        f.write(f"Model: {agent.config.model}\n")
        f.write(f"Exported: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 50 + "\n\n")
        
        for msg in agent.messages:
            timestamp_str = datetime.fromisoformat(msg["timestamp"]).strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"[{timestamp_str}] {msg['role'].upper()}:\n")
            f.write(f"{msg['content']}\n\n")
    
    agent.logger.info(f"Exported conversation to {filepath}")
    return str(filepath)


def _export_md(agent, export_dir: Path, timestamp: str) -> str:
    """Export conversation to Markdown format"""
    filename = f"conversation_{timestamp}.md"
    filepath = export_dir / filename
    
    model_display = SUPPORTED_MODELS.get(agent.config.model, {}).get('name', agent.config.model)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(f"# OpenAI {model_display} Chat Agent Conversation\n\n")
        f.write(f"**Agent ID:** {agent.agent_id}  \n")
        f.write(f"**Model:** {agent.config.model}  \n")
        f.write(f"**Exported:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  \n\n")
        
        for msg in agent.messages:
            timestamp_str = datetime.fromisoformat(msg["timestamp"]).strftime("%Y-%m-%d %H:%M:%S")
            role_emoji = "🧑" if msg["role"] == "user" else "🤖"
            f.write(f"## {role_emoji} {msg['role'].title()} - {timestamp_str}\n\n")
            f.write(f"{msg['content']}\n\n")
    
    agent.logger.info(f"Exported conversation to {filepath}")
    return str(filepath)


def _export_html(agent, export_dir: Path, timestamp: str) -> str:
    """Export conversation to HTML format"""
    filename = f"conversation_{timestamp}.html"
    filepath = export_dir / filename
    
    stats = agent.get_statistics()
    model_display = SUPPORTED_MODELS.get(agent.config.model, {}).get('name', agent.config.model)
    
    # HTML template with modern styling
    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OpenAI {model_display} Conversation - {agent.agent_id}</title>
    <style>
        :root {{
            --primary-color: #2563eb;
            --secondary-color: #f1f5f9;
            --text-color: #1e293b;
            --border-color: #e2e8f0;
            --user-bg: #3b82f6;
            --assistant-bg: #10b981;
            --code-bg: #f8fafc;
        }}
        
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            color: var(--text-color);
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 2rem;
        }}
        
        .container {{
            max-width: 4xl;
            margin: 0 auto;
            background: white;
            border-radius: 1rem;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
            overflow: hidden;
        }}
        
        .header {{
            background: var(--primary-color);
            color: white;
            padding: 2rem;
            text-align: center;
        }}
        
        .header h1 {{
            font-size: 2rem;
            margin-bottom: 0.5rem;
        }}
        
        .header-info {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin-top: 2rem;
            font-size: 0.9rem;
        }}
        
        .stats {{
            background: var(--secondary-color);
            padding: 1.5rem;
            border-bottom: 1px solid var(--border-color);
        }}
        
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 1rem;
        }}
        
        .stat-item {{
            text-align: center;
            padding: 1rem;
            background: white;
            border-radius: 0.5rem;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
        }}
        
        .stat-value {{
            font-size: 1.5rem;
            font-weight: bold;
            color: var(--primary-color);
        }}
        
        .stat-label {{
            font-size: 0.8rem;
            color: #64748b;
            margin-top: 0.25rem;
        }}
        
        .messages {{
            padding: 2rem;
            max-height: 70vh;
            overflow-y: auto;
        }}
        
        .message {{
            margin-bottom: 2rem;
            display: flex;
            align-items: flex-start;
            gap: 1rem;
        }}
        
        .message.user {{
            flex-direction: row-reverse;
        }}
        
        .message-avatar {{
            width: 3rem;
            height: 3rem;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.2rem;
            font-weight: bold;
            color: white;
            flex-shrink: 0;
        }}
        
        .message.user .message-avatar {{
            background: var(--user-bg);
        }}
        
        .message.assistant .message-avatar {{
            background: var(--assistant-bg);
        }}
        
        .message-content {{
            flex: 1;
            background: white;
            border: 1px solid var(--border-color);
            border-radius: 1rem;
            padding: 1.5rem;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
            position: relative;
        }}
        
        .message.user .message-content {{
            background: #eff6ff;
            border-color: var(--user-bg);
        }}
        
        .message.assistant .message-content {{
            background: #f0fdf4;
            border-color: var(--assistant-bg);
        }}
        
        .message-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1rem;
            padding-bottom: 0.5rem;
            border-bottom: 1px solid var(--border-color);
        }}
        
        .message-role {{
            font-weight: 600;
            text-transform: capitalize;
        }}
        
        .message-time {{
            font-size: 0.8rem;
            color: #64748b;
        }}
        
        .message-text {{
            white-space: pre-wrap;
            word-wrap: break-word;
        }}
        
        .code-block {{
            background: var(--code-bg);
            border: 1px solid var(--border-color);
            border-radius: 0.5rem;
            padding: 1rem;
            margin: 1rem 0;
            overflow-x: auto;
            font-family: 'Monaco', 'Menlo', monospace;
            font-size: 0.9rem;
        }}
        
        .footer {{
            background: var(--secondary-color);
            padding: 1rem 2rem;
            text-align: center;
            font-size: 0.8rem;
            color: #64748b;
            border-top: 1px solid var(--border-color);
        }}
        
        @media (max-width: 768px) {{
            body {{
                padding: 1rem;
            }}
            
            .header {{
                padding: 1.5rem;
            }}
            
            .header h1 {{
                font-size: 1.5rem;
            }}
            
            .header-info {{
                grid-template-columns: 1fr;
            }}
            
            .messages {{
                padding: 1rem;
            }}
            
            .message-content {{
                padding: 1rem;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🤖 OpenAI {model_display} Chat Agent</h1>
            <p>Conversation Export</p>
            <div class="header-info">
                <div><strong>Agent ID:</strong> {agent.agent_id}</div>
                <div><strong>Model:</strong> {agent.config.model}</div>
                <div><strong>Exported:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</div>
                <div><strong>Temperature:</strong> {agent.config.temperature}</div>
            </div>
        </div>
        
        <div class="stats">
            <div class="stats-grid">
                <div class="stat-item">
                    <div class="stat-value">{stats['total_messages']}</div>
                    <div class="stat-label">Total Messages</div>
                </div>
                <div class="stat-item">
                    <div class="stat-value">{stats['user_messages']}</div>
                    <div class="stat-label">User Messages</div>
                </div>
                <div class="stat-item">
                    <div class="stat-value">{stats['assistant_messages']}</div>
                    <div class="stat-label">Assistant Messages</div>
                </div>
                <div class="stat-item">
                    <div class="stat-value">{stats['total_characters']:,}</div>
                    <div class="stat-label">Total Characters</div>
                </div>
                <div class="stat-item">
                    <div class="stat-value">{stats['average_message_length']:,}</div>
                    <div class="stat-label">Avg Message Length</div>
                </div>
                <div class="stat-item">
                    <div class="stat-value">{stats.get('conversation_duration', 'N/A')}</div>
                    <div class="stat-label">Duration</div>
                </div>
            </div>
        </div>
        
        <div class="messages">"""
        
    # Add messages
    for msg in agent.messages:
        timestamp_str = datetime.fromisoformat(msg["timestamp"]).strftime("%Y-%m-%d %H:%M:%S")
        role = msg["role"]
        content = msg["content"]
        
        # Escape HTML and preserve formatting
        content_escaped = html.escape(content)
        
        # Simple code block detection
        if '```' in content_escaped:
            parts = content_escaped.split('```')
            formatted_content = ""
            for i, part in enumerate(parts):
                if i % 2 == 1:  # Code block
                    formatted_content += f'<div class="code-block">{part}</div>'
                else:  # Regular text
                    formatted_content += part
            content_escaped = formatted_content
        
        avatar_text = "U" if role == "user" else "AI"
        
        html_template += f"""
        <div class="message {role}">
            <div class="message-avatar">{avatar_text}</div>
            <div class="message-content">
                <div class="message-header">
                    <span class="message-role">{role}</span>
                    <span class="message-time">{timestamp_str}</span>
                </div>
                <div class="message-text">{content_escaped}</div>
            </div>
        </div>"""
    
    # Close HTML
    html_template += f"""
        </div>
        
        <div class="footer">
            Generated by OpenAI {model_display} Chat Agent • Agent ID: {agent.agent_id} • {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        </div>
    </div>
</body>
</html>"""
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html_template)
    
    agent.logger.info(f"Exported conversation to {filepath}")
    return str(filepath)