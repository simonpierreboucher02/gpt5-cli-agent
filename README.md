# OpenAI GPT-5 Unified Chat Agent
**Author:** Simon-Pierre Boucher

A professional, unified command-line interface for all OpenAI GPT model variants with an enhanced user experience designed to be legendary.

## 🚀 Features

### Multi-Model Support
- **GPT-5** - Full-featured model with advanced reasoning capabilities (3-12 min timeouts)
- **GPT-5 Mini** - Compact model balancing performance and efficiency (1.5-6 min timeouts)  
- **GPT-5 Nano** - Lightweight model optimized for speed (1-4 min timeouts)

### Professional Features
- ✨ **Enhanced CLI** with beautiful colored output and intuitive interface
- 💬 **Persistent Conversation History** with rolling backups
- 🌊 **Streaming & Non-streaming** response support
- 📁 **File Inclusion** via `{filename}` syntax for programming files
- ⚙️ **Advanced Configuration Management** per agent
- 📊 **Comprehensive Statistics** and analytics
- 📤 **Export Capabilities** (JSON, TXT, Markdown, HTML)
- 🔐 **Secure API Key Management** with environment and file support
- 🔍 **Conversation Search** and history navigation
- 🎯 **Model-specific Timeouts** based on reasoning effort

## 📦 Installation

1. Clone or download the project files
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set your OpenAI API key (one of the following):
```bash
# Environment variable (recommended)
export OPENAI_API_KEY="your-api-key-here"

# Or the program will prompt you and save it securely
```

## 🎯 Quick Start

### Start a chat session with GPT-5
```bash
python main.py --agent-id my-agent --model gpt-5
```

### Use GPT-5 Mini for faster responses
```bash
python main.py --agent-id my-agent --model gpt-5-mini
```

### Use GPT-5 Nano for speed-optimized responses
```bash
python main.py --agent-id my-agent --model gpt-5-nano
```

### List all your agents
```bash
python main.py --list
```

### Configure an agent interactively
```bash
python main.py --agent-id my-agent --config
```

### View detailed agent information
```bash
python main.py --info my-agent
```

### Export conversation
```bash
python main.py --agent-id my-agent --export html
```

## 💻 Interactive Commands

Once in a chat session, use these commands:

- `/help` - Show all available commands
- `/history [n]` - Show last n messages (default 5)
- `/search <term>` - Search conversation history
- `/stats` - Show conversation statistics
- `/config` - Show current configuration
- `/export <format>` - Export conversation (json|txt|md|html)
- `/clear` - Clear conversation history
- `/files` - List available files for inclusion
- `/info` - Show agent information
- `/quit` - Exit chat session

## 📁 File Inclusion

Include file contents in your messages using `{filename}` syntax:

```
Can you review this code? {main.py}

Please analyze these configs: {config.yaml} and {settings.json}
```

### Supported File Types
- Programming languages (.py, .js, .ts, .java, .c, .cpp, .go, .rs, etc.)
- Configuration files (.yaml, .json, .toml, .ini, .env, etc.)
- Documentation (.md, .rst, .txt, etc.)
- Web files (.html, .css, .scss, etc.)
- And many more...

## ⚙️ Configuration

Each agent maintains its own configuration including:

- **Model**: GPT variant to use
- **Temperature**: Response creativity (0.0-2.0)
- **Reasoning Effort**: Low/Medium/High (affects timeout)
- **Reasoning Summary**: Auto/Detailed/None
- **System Prompt**: Custom instructions for the AI
- **Streaming**: Enable/disable response streaming
- **Max Output Tokens**: Limit response length
- **History Size**: Maximum conversation history

## 📊 Model Comparison

| Model | Best For | Reasoning Timeout | Performance |
|-------|----------|------------------|-------------|
| **GPT-5** | Complex reasoning, detailed analysis | 3-12 minutes | Highest quality |
| **GPT-5 Mini** | Balanced use cases | 1.5-6 minutes | Good balance |
| **GPT-5 Nano** | Quick responses, simple tasks | 1-4 minutes | Fastest |

## 🗂️ Project Structure

```
gpt5/
├── main.py           # Main unified CLI application
├── config.py         # Configuration and model definitions
├── agent.py          # Core chat agent implementation
├── utils.py          # Utility functions
├── export.py         # Conversation export functionality
├── requirements.txt  # Python dependencies
├── README.md         # This file
└── agents/          # Agent data (created automatically)
    └── {agent-id}/
        ├── config.yaml      # Agent configuration
        ├── history.json     # Conversation history
        ├── secrets.json     # API keys (git-ignored)
        ├── backups/         # History backups
        ├── logs/           # Application logs
        └── exports/        # Exported conversations
```

## 🔐 Security

- API keys are stored securely and automatically added to `.gitignore`
- Support for environment variables and secure file storage
- Model-specific API key management
- No sensitive data in logs or exports

## 🎨 User Experience Highlights

- **Beautiful ASCII banners** and colorful interface
- **Smart input validation** with helpful error messages
- **Progress indicators** for long reasoning operations
- **Intuitive commands** with tab-completion style help
- **Rich statistics** and conversation analytics
- **Professional export formats** with modern styling

## 🐛 Troubleshooting

### Common Issues

1. **API Key Issues**: Ensure your OpenAI API key is valid and has sufficient credits
2. **Timeout Errors**: Try reducing reasoning effort from high to medium or low
3. **File Not Found**: Use `/files` command to see available files for inclusion
4. **Permission Errors**: Ensure write permissions in the project directory

### Getting Help

- Use the `/help` command in chat for available commands
- Check the agent info with `--info` command
- Review logs in `agents/{agent-id}/logs/`

## 📝 License

This project is provided as-is for educational and professional use.

## 🤝 Contributing

This is a unified, professional implementation combining multiple OpenAI GPT agents with enhanced user experience. All French instructions have been converted to English for international accessibility.
