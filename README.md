<div align="center">

# 🤖 GPT-5 CLI Agent

### A professional, unified command-line interface for all OpenAI GPT-5 model variants

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--5-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com)
[![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)](LICENSE)
[![Version](https://img.shields.io/badge/Version-1.0.0-6366f1?style=for-the-badge)](https://github.com/simonpierreboucher02/gpt5-cli-agent/releases)

[![GitHub Stars](https://img.shields.io/github/stars/simonpierreboucher02/gpt5-cli-agent?style=flat-square&logo=github&color=fbbf24)](https://github.com/simonpierreboucher02/gpt5-cli-agent/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/simonpierreboucher02/gpt5-cli-agent?style=flat-square&logo=github&color=60a5fa)](https://github.com/simonpierreboucher02/gpt5-cli-agent/network)
[![GitHub Issues](https://img.shields.io/github/issues/simonpierreboucher02/gpt5-cli-agent?style=flat-square&logo=github&color=f87171)](https://github.com/simonpierreboucher02/gpt5-cli-agent/issues)
[![Last Commit](https://img.shields.io/github/last-commit/simonpierreboucher02/gpt5-cli-agent?style=flat-square&logo=github&color=34d399)](https://github.com/simonpierreboucher02/gpt5-cli-agent/commits)
[![Repo Size](https://img.shields.io/github/repo-size/simonpierreboucher02/gpt5-cli-agent?style=flat-square&logo=github&color=a78bfa)](https://github.com/simonpierreboucher02/gpt5-cli-agent)
[![Code Size](https://img.shields.io/github/languages/code-size/simonpierreboucher02/gpt5-cli-agent?style=flat-square&color=fb923c)](https://github.com/simonpierreboucher02/gpt5-cli-agent)

[![Maintained](https://img.shields.io/badge/Maintained-Yes-22c55e?style=flat-square)](https://github.com/simonpierreboucher02/gpt5-cli-agent)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-6366f1?style=flat-square)](https://github.com/simonpierreboucher02/gpt5-cli-agent/pulls)
[![Made with Love](https://img.shields.io/badge/Made%20with-%E2%9D%A4%EF%B8%8F-ef4444?style=flat-square)](https://www.spboucher.ai)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows-0ea5e9?style=flat-square)](https://github.com/simonpierreboucher02/gpt5-cli-agent)

---

**A legendary, production-ready CLI for GPT-5 — featuring streaming responses, multi-agent support, rich exports, and an enhanced terminal experience.**

[✨ Features](#-features) •
[⚙️ Installation](#️-installation) •
[🚀 Quick Start](#-quick-start) •
[💻 Commands](#-interactive-commands) •
[📊 Models](#-model-comparison) •
[🏗️ Architecture](#️-project-structure) •
[🔒 Security](#-security) •
[👥 Authors](#-authors) •
[📄 License](#-license)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Requirements](#-requirements)
- [Installation](#️-installation)
- [Quick Start](#-quick-start)
- [Interactive Commands](#-interactive-commands)
- [File Inclusion](#-file-inclusion)
- [Export Formats](#-export-formats)
- [Model Comparison](#-model-comparison)
- [Configuration](#️-configuration)
- [Project Structure](#️-project-structure)
- [Performance Metrics](#-performance-metrics)
- [Security](#-security)
- [Troubleshooting](#-troubleshooting)
- [Authors](#-authors)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🌟 Overview

**GPT-5 CLI Agent** is a professional, unified command-line interface engineered to harness the full power of OpenAI's GPT-5 model family. Built with developer experience in mind, it provides a seamless terminal-native workflow for AI-assisted development, analysis, and automation.

Whether you need the raw intelligence of **GPT-5**, the efficiency of **GPT-5 Mini**, or the blazing speed of **GPT-5 Nano** — this single CLI handles all three with persistent history, advanced configuration, and beautiful formatted output.

```
╔══════════════════════════════════════════════════════╗
║          🤖  GPT-5 Unified CLI Agent  v1.0.0         ║
║     Powered by OpenAI GPT-5 | Built for Builders     ║
╚══════════════════════════════════════════════════════╝
```

---

## ✨ Features

<table>
<tr>
<td>

### 🧠 AI Capabilities
- ✅ **GPT-5** — Full reasoning power
- ✅ **GPT-5 Mini** — Balanced performance
- ✅ **GPT-5 Nano** — Fast & lightweight
- ✅ Streaming token-by-token output
- ✅ Configurable reasoning effort
- ✅ Custom system prompts per agent

</td>
<td>

### 💾 Session Management
- ✅ Persistent conversation history
- ✅ Automatic backups before each session
- ✅ History search with `/search <term>`
- ✅ Multi-agent isolation
- ✅ Session statistics & analytics
- ✅ Auto-save on exit

</td>
</tr>
<tr>
<td>

### 📤 Export System
- ✅ **JSON** — Machine-readable full history
- ✅ **TXT** — Plain text transcripts
- ✅ **Markdown** — Formatted documentation
- ✅ **HTML** — Styled web-ready reports
- ✅ Timestamped export filenames
- ✅ One-command export from CLI

</td>
<td>

### 🎨 Terminal Experience
- ✅ Rich colored output with `colorama`
- ✅ ASCII banners & status indicators
- ✅ Syntax-aware file inclusion
- ✅ Progress feedback on long requests
- ✅ Graceful Ctrl+C / Ctrl+D handling
- ✅ Cross-platform (Linux, macOS, Windows)

</td>
</tr>
</table>

---

## 📦 Requirements

[![Python](https://img.shields.io/badge/Python-≥3.10-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![requests](https://img.shields.io/badge/requests-≥2.31.0-e11d48?style=flat-square)](https://pypi.org/project/requests/)
[![pyyaml](https://img.shields.io/badge/pyyaml-≥6.0.1-facc15?style=flat-square)](https://pypi.org/project/pyyaml/)
[![colorama](https://img.shields.io/badge/colorama-≥0.4.6-4ade80?style=flat-square)](https://pypi.org/project/colorama/)
[![OpenAI API Key](https://img.shields.io/badge/OpenAI-API%20Key%20Required-412991?style=flat-square&logo=openai)](https://platform.openai.com/api-keys)

| Dependency | Version | Purpose |
|---|---|---|
| `python` | ≥ 3.10 | Runtime |
| `requests` | ≥ 2.31.0 | HTTP API calls |
| `pyyaml` | ≥ 6.0.1 | Config file parsing |
| `colorama` | ≥ 0.4.6 | Cross-platform terminal colors |

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/simonpierreboucher02/gpt5-cli-agent.git
cd gpt5-cli-agent
```

### 2. Create a Virtual Environment (Recommended)

```bash
# Create environment
python -m venv venv

# Activate — macOS / Linux
source venv/bin/activate

# Activate — Windows
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Your OpenAI API Key

```bash
# macOS / Linux (add to ~/.zshrc or ~/.bashrc for persistence)
export OPENAI_API_KEY=sk-...your-key-here...

# Windows (Command Prompt)
set OPENAI_API_KEY=sk-...your-key-here...

# Windows (PowerShell)
$env:OPENAI_API_KEY="sk-...your-key-here..."
```

> **Tip:** Add the export line to your shell profile to avoid setting it every session.

---

## 🚀 Quick Start

### Launch with GPT-5 (Default)

```bash
python main.py --agent-id my-agent --model gpt-5
```

### Launch with GPT-5 Mini

```bash
python main.py --agent-id my-agent --model gpt-5-mini
```

### Launch with GPT-5 Nano

```bash
python main.py --agent-id my-agent --model gpt-5-nano
```

### List All Agents

```bash
python main.py --list
```

### Configure an Agent Interactively

```bash
python main.py --agent-id my-agent --config
```

### Export a Conversation

```bash
# Export as HTML
python main.py --agent-id my-agent --export html

# Export as Markdown
python main.py --agent-id my-agent --export md

# Export as JSON
python main.py --agent-id my-agent --export json
```

### Show Help

```bash
python main.py --help
```

---

## 💻 Interactive Commands

Once inside a chat session, use these slash commands:

| Command | Description | Example |
|---|---|---|
| `/help` | Display all available commands | `/help` |
| `/history [n]` | Show last `n` messages (default: 10) | `/history 20` |
| `/search <term>` | Full-text search across conversation | `/search authentication` |
| `/stats` | Show token usage, message count, session duration | `/stats` |
| `/config` | Display current agent configuration | `/config` |
| `/export <format>` | Export conversation (`json`/`txt`/`md`/`html`) | `/export md` |
| `/clear` | Clear conversation history | `/clear` |
| `/files` | List files available for inclusion | `/files` |
| `/info` | Show agent ID, model, and metadata | `/info` |
| `/quit` | Exit the chat session | `/quit` |

---

## 📁 File Inclusion

Embed file contents directly into your prompts using the `{filename}` syntax:

```
> Please review this code: {main.py}

> Compare these two configs: {config.yaml}, {settings.json}

> Analyze the project structure based on: {README.md}
```

### Supported File Types

| Category | Extensions |
|---|---|
| **Python** | `.py`, `.pyw` |
| **JavaScript / TypeScript** | `.js`, `.ts`, `.jsx`, `.tsx` |
| **Systems** | `.c`, `.cpp`, `.h`, `.go`, `.rs` |
| **Web** | `.html`, `.css`, `.scss` |
| **Data / Config** | `.json`, `.yaml`, `.yml`, `.toml`, `.ini` |
| **Documentation** | `.md`, `.rst`, `.txt` |
| **Shell** | `.sh`, `.bash`, `.zsh`, `.ps1` |

---

## 📤 Export Formats

| Format | Extension | Best For |
|---|---|---|
| **JSON** | `.json` | Programmatic processing, data pipelines |
| **Plain Text** | `.txt` | Simple archival, sharing |
| **Markdown** | `.md` | Documentation, GitHub wikis |
| **HTML** | `.html` | Styled reports, client presentations |

Exports are saved to: `agents/<agent-id>/exports/`

---

## 📊 Model Comparison

| Model | Intelligence | Speed | Cost | Best Use Case | Timeout |
|---|---|---|---|---|---|
| ![GPT-5](https://img.shields.io/badge/GPT--5-★★★★★-412991?style=flat-square) | 🌟🌟🌟🌟🌟 | 🐢 | 💰💰💰 | Complex reasoning, deep analysis, research | 3–12 min |
| ![GPT-5 Mini](https://img.shields.io/badge/GPT--5%20Mini-★★★★☆-6366f1?style=flat-square) | 🌟🌟🌟🌟 | 🚗 | 💰💰 | Balanced workloads, code review, writing | 1.5–6 min |
| ![GPT-5 Nano](https://img.shields.io/badge/GPT--5%20Nano-★★★☆☆-60a5fa?style=flat-square) | 🌟🌟🌟 | 🚀 | 💰 | Quick Q&A, summaries, simple tasks | 1–4 min |

### Choosing the Right Model

```
Is the task complex or requires deep reasoning?
  YES → Use GPT-5
  NO  → Do you need a good balance of speed and quality?
          YES → Use GPT-5 Mini
          NO  → Use GPT-5 Nano (fastest, cheapest)
```

---

## ⚙️ Configuration

Each agent stores its configuration in `agents/<agent-id>/config.yaml`:

```yaml
# agents/my-agent/config.yaml

model: gpt-5                    # gpt-5 | gpt-5-mini | gpt-5-nano
temperature: 0.7                # 0.0 (deterministic) → 2.0 (creative)
max_tokens: 4096                # Maximum response tokens
reasoning_effort: medium        # low | medium | high (GPT-5 only)
stream: true                    # Enable token streaming
system_prompt: |
  You are a senior software engineer.
  Provide concise, production-ready code.
```

### Configuration Parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `model` | string | `gpt-5` | Model variant to use |
| `temperature` | float | `0.7` | Response randomness (0–2) |
| `max_tokens` | int | `4096` | Max tokens per response |
| `reasoning_effort` | string | `medium` | Reasoning depth (GPT-5 only) |
| `stream` | bool | `true` | Stream tokens in real time |
| `system_prompt` | string | — | Custom system instructions |

---

## 🏗️ Project Structure

```
gpt5-cli-agent/
│
├── 📄 main.py              # CLI entrypoint, argument parsing, session loop
├── 🧠 agent.py             # Agent class, API calls, streaming logic (462 lines)
├── ⚙️  config.py            # Configuration management, YAML read/write (89 lines)
├── 📤 export.py            # Multi-format export engine (424 lines)
├── 🔧 utils.py             # File inclusion, formatting utilities (285 lines)
├── 📋 requirements.txt     # Python dependencies
├── 📖 README.md            # This file
│
└── agents/                 # Per-agent data directory (auto-created)
    └── {agent-id}/
        ├── config.yaml     # Agent-specific configuration
        ├── history.json    # Persistent conversation history
        ├── secrets.json    # API keys (git-ignored)
        ├── backups/        # Automatic history backups
        ├── logs/           # Session logs
        └── exports/        # Exported conversations
```

### Module Responsibilities

| Module | Lines | Responsibility |
|---|---|---|
| `main.py` | 616 | CLI entry, argument parsing, REPL loop |
| `agent.py` | 462 | GPT-5 API integration, streaming |
| `export.py` | 424 | JSON / TXT / Markdown / HTML export |
| `utils.py` | 285 | File inclusion, text formatting |
| `config.py` | 89 | YAML config read/write |
| **Total** | **1,876** | **Full project** |

---

## 📈 Performance Metrics

| Metric | GPT-5 | GPT-5 Mini | GPT-5 Nano |
|---|---|---|---|
| Avg. First Token | ~3–8s | ~1–3s | ~0.5–1.5s |
| Avg. Full Response | ~30–120s | ~15–60s | ~5–20s |
| Token Throughput | ~30 tok/s | ~60 tok/s | ~100 tok/s |
| Context Window | 128K tokens | 128K tokens | 128K tokens |
| Streaming Support | ✅ | ✅ | ✅ |

> Performance varies based on OpenAI infrastructure load and response complexity.

---

## 🔒 Security

[![Security Policy](https://img.shields.io/badge/Security-Policy-ef4444?style=flat-square&logo=github)](https://github.com/simonpierreboucher02/gpt5-cli-agent/security)

- 🔑 **API keys** are stored in `secrets.json` which is automatically excluded via `.gitignore`
- 🚫 **No sensitive data** is ever included in logs or exports
- ✅ **Environment variable** support — use `OPENAI_API_KEY` instead of file storage
- 🔐 **Multi-model key support** — separate keys per model if needed
- 📂 **Agent isolation** — each agent's data is fully sandboxed in its own directory
- 🛡️ **No telemetry** — no usage data is sent anywhere except OpenAI's API

### Security Best Practices

```bash
# Always use environment variables in production
export OPENAI_API_KEY=sk-...

# Never commit secrets — verify .gitignore is active
cat .gitignore | grep secrets

# Restrict permissions on the agents directory
chmod 700 agents/
```

---

## 🐛 Troubleshooting

### Common Issues

| Error | Cause | Fix |
|---|---|---|
| `ModuleNotFoundError` | Missing dependency | `pip install -r requirements.txt` |
| `AuthenticationError` | Invalid API key | Verify `OPENAI_API_KEY` is set and valid |
| `TimeoutError` | Request too long | Reduce `max_tokens` or lower `reasoning_effort` |
| `FileNotFoundError` | File inclusion failed | Run `/files` to list available files |
| `JSONDecodeError` | Corrupted history | Delete `agents/<id>/history.json` to reset |
| `RateLimitError` | API quota exceeded | Wait and retry, or upgrade OpenAI tier |

### Debug Mode

```bash
# Enable verbose logging
python main.py --agent-id my-agent --model gpt-5 --debug
```

### Reset an Agent

```bash
# Delete agent history (keeps config)
rm agents/my-agent/history.json

# Full reset (removes all agent data)
rm -rf agents/my-agent/
```

---

## 👥 Authors

<table>
<tr>
<td align="center" width="50%">

### 🧑‍💻 Simon-Pierre Boucher

[![Email](https://img.shields.io/badge/Email-spbou4%40protonmail.com-6d4aff?style=flat-square&logo=protonmail&logoColor=white)](mailto:spbou4@protonmail.com)
[![Website](https://img.shields.io/badge/Website-spboucher.ai-0ea5e9?style=flat-square&logo=safari&logoColor=white)](https://www.spboucher.ai)
[![GitHub](https://img.shields.io/badge/GitHub-simonpierreboucher02-24292e?style=flat-square&logo=github)](https://github.com/simonpierreboucher02)

**Creator & Lead Developer**

AI/ML engineer and researcher building production-grade AI tooling. Passionate about making large language models accessible through elegant command-line interfaces.

- 🎓 Université Laval
- 🌐 [www.spboucher.ai](https://www.spboucher.ai)
- 📧 [spbou4@protonmail.com](mailto:spbou4@protonmail.com)

</td>
<td align="center" width="50%">

### 🤖 Claude (Anthropic)

[![Anthropic](https://img.shields.io/badge/Anthropic-Claude-d97706?style=flat-square&logo=anthropic&logoColor=white)](https://anthropic.com)
[![Model](https://img.shields.io/badge/Model-Claude%20Sonnet%204.6-6366f1?style=flat-square)](https://anthropic.com/claude)

**AI Co-Author & Documentation Assistant**

This README was co-authored with Claude, Anthropic's AI assistant, to ensure comprehensive documentation, accurate technical details, and a polished developer experience.

- 🧠 Claude Sonnet 4.6
- 🏢 [Anthropic](https://anthropic.com)
- 🤝 AI pair-programming partner

</td>
</tr>
</table>

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

```bash
# 1. Fork the repository on GitHub

# 2. Clone your fork
git clone https://github.com/YOUR_USERNAME/gpt5-cli-agent.git
cd gpt5-cli-agent

# 3. Create a feature branch
git checkout -b feature/my-new-feature

# 4. Make your changes and test
python main.py --agent-id test --model gpt-5-nano

# 5. Commit your changes
git add .
git commit -m "feat: add my new feature"

# 6. Push and open a Pull Request
git push origin feature/my-new-feature
```

### Contribution Guidelines

- Follow [PEP 8](https://pep8.org/) style for Python code
- Add docstrings to new functions and classes
- Test with all three models before submitting
- Update this README if you add user-facing features
- Keep PRs focused — one feature or fix per PR

[![Open Issues](https://img.shields.io/github/issues/simonpierreboucher02/gpt5-cli-agent?style=flat-square)](https://github.com/simonpierreboucher02/gpt5-cli-agent/issues)
[![Open PRs](https://img.shields.io/github/issues-pr/simonpierreboucher02/gpt5-cli-agent?style=flat-square)](https://github.com/simonpierreboucher02/gpt5-cli-agent/pulls)

---

## 📄 License

```
MIT License

Copyright (c) 2025 Simon-Pierre Boucher

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

[![License: MIT](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)](LICENSE)

---

<div align="center">

**Built with ❤️ by [Simon-Pierre Boucher](https://www.spboucher.ai) & [Claude](https://anthropic.com/claude)**

[![Website](https://img.shields.io/badge/🌐-www.spboucher.ai-0ea5e9?style=for-the-badge)](https://www.spboucher.ai)
[![Email](https://img.shields.io/badge/📧-spbou4%40protonmail.com-6d4aff?style=for-the-badge)](mailto:spbou4@protonmail.com)
[![GitHub](https://img.shields.io/badge/⭐-Star%20this%20repo-fbbf24?style=for-the-badge)](https://github.com/simonpierreboucher02/gpt5-cli-agent)

*If this project helped you, consider giving it a ⭐ on GitHub!*

</div>
