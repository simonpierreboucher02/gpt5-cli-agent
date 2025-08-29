# 🌐 OpenAI GPT-5 Unified Chat Agent  

**👨‍💻 Author: Simon-Pierre Boucher**  

<div align="center">  

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)  
![OpenAI](https://img.shields.io/badge/OpenAI-API-green?logo=openai&logoColor=white)  
![License](https://img.shields.io/badge/License-MIT-yellow)  
![Version](https://img.shields.io/badge/Version-1.0.0-purple)  

**A professional, unified CLI agent for OpenAI GPT-5 models**  
*Supports GPT-5, GPT-5 Mini, and GPT-5 Nano with advanced reasoning, exports, and modern CLI*  

[✨ Features](#-features) • [⚙️ Installation](#-installation) • [🚀 Quick Start](#-quick-start) • [💻 Commands](#-interactive-commands) • [📁 File Inclusion](#-file-inclusion) • [📊 Model Comparison](#-model-comparison) • [🏗️ Architecture](#-project-structure) • [🔒 Security](#-security) • [🐛 Troubleshooting](#-troubleshooting) • [📄 License](#-license) • [🤝 Contributing](#-contributing)  

</div>  

---

## ✨ Features  

- 🔹 **All GPT-5 Models**: GPT-5, GPT-5 Mini, GPT-5 Nano  
- 🎨 **Enhanced CLI**: Beautiful colored output, banners, intuitive commands  
- 💬 **Persistent History**: Auto backup & restore  
- 📁 **File Inclusion**: `{filename}` syntax  
- 📤 **Multi-format Export**: JSON, TXT, Markdown, HTML  
- ⚙️ **Advanced Config**: Parameters, streaming, system prompts  
- 📊 **Statistics & Analytics**  
- 🛡️ **Error Handling & Logging**  

---

## ⚙️ Installation  

Clone the repository:  
```bash
git clone https://github.com/simonpierreboucher02/gpt5-cli-agent.git
cd gpt5-cli-agent
```

Create and activate a virtual environment (recommended):  
```bash
python -m venv venv
source venv/bin/activate
```

Install dependencies:  
```bash
pip install -r requirements.txt
```

Set your OpenAI API key:  
```bash
export OPENAI_API_KEY=your_api_key_here
```  

---

## 🚀 Quick Start  

### Start GPT-5  
```bash
python main.py --agent-id my-agent --model gpt-5
```  

### Use GPT-5 Mini  
```bash
python main.py --agent-id my-agent --model gpt-5-mini
```  

### Use GPT-5 Nano  
```bash
python main.py --agent-id my-agent --model gpt-5-nano
```  

### List all agents  
```bash
python main.py --list
```  

### Configure an agent interactively  
```bash
python main.py --agent-id my-agent --config
```  

### Export conversation  
```bash
python main.py --agent-id my-agent --export html
```  

---

## 💻 Interactive Commands  

| Command | Description |
|---------|-------------|
| `/help` | Show all available commands |
| `/history [n]` | Show last n messages |
| `/search <term>` | Search conversation history |
| `/stats` | Show statistics |
| `/config` | Show current configuration |
| `/export <format>` | Export conversation (json/txt/md/html) |
| `/clear` | Clear history |
| `/files` | List available files |
| `/info` | Show agent info |
| `/quit` | Exit chat |  

---

## 📁 File Inclusion  

```
Review this code: {main.py}  
Check config: {config.yaml}, {settings.json}  
```  

Supported file types: Python, JavaScript, TypeScript, C/C++, Go, Rust, HTML, CSS, JSON, YAML, Markdown, etc.  

---

## 📊 Model Comparison  

| Model | Best Use Case | Timeout | Performance |
|-------|---------------|---------|-------------|
| **GPT-5** | Complex reasoning, analysis | 3–12 min | 🌟🌟🌟🌟🌟 |
| **GPT-5 Mini** | Balanced workloads | 1.5–6 min | 🌟🌟🌟🌟 |
| **GPT-5 Nano** | Quick/simple tasks | 1–4 min | 🌟🌟🌟 |  

---

## 🏗️ Project Structure  

```
gpt5-cli-agent/
├── main.py
├── config.py
├── agent.py
├── utils.py
├── export.py
├── requirements.txt
└── agents/
    └── {agent-id}/
        ├── config.yaml
        ├── history.json
        ├── secrets.json
        ├── backups/
        ├── logs/
        └── exports/
```  

---

## 🔒 Security  

- 🔑 Secure API key management  
- 🚫 No sensitive data in logs/exports  
- ✅ `.gitignore` automatically excludes secrets  
- 🔐 Multi-model key support  

---

## 🐛 Troubleshooting  

- ❌ Import errors → `pip install -r requirements.txt`  
- 🔑 API key issues → `export OPENAI_API_KEY=...`  
- ⏱️ Timeout issues → Adjust reasoning effort or temperature  
- 📂 File not found → Use `/files` command  

---

## 📄 License  

MIT License — professional & educational use.  

---

## 🤝 Contributing  

Contributions welcome!  

---

**2025-08-29**  
*Université Laval*  
