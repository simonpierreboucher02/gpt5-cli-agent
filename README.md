# 🌐 OpenAI GPT-5 Unified Chat Agent  

**👨‍💻 Author: Simon-Pierre Boucher**  

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)  
![OpenAI](https://img.shields.io/badge/OpenAI-API-green?logo=openai&logoColor=white)  
![License](https://img.shields.io/badge/License-MIT-yellow)  
![Version](https://img.shields.io/badge/Version-1.0.0-purple)  

**A professional, unified command-line interface for all GPT-5 variants**  
*Legendary UX with enhanced CLI, persistence, and advanced reasoning support*  

[📦 Features](#-key-features) • [⚙️ Installation](#-installation) • [🚀 Quick Start](#-quick-start) • [💻 Commands](#-interactive-commands) • [📁 File Inclusion](#-file-inclusion) • [📊 Model Comparison](#-model-comparison) • [🗂️ Project Structure](#-project-structure) • [🔐 Security](#-security) • [🎨 UX](#-user-experience) • [🐛 Troubleshooting](#-troubleshooting) • [📝 License](#-license) • [🤝 Contributing](#-contributing)

</div>  

---

## 🚀 Key Features  

### 🔄 Multi-Model Support  
- 🔹 **GPT-5** → Advanced reasoning (3–12 min timeouts)  
- 🔹 **GPT-5 Mini** → Balanced efficiency/performance (1.5–6 min timeouts)  
- 🔹 **GPT-5 Nano** → Speed-optimized lightweight model (1–4 min timeouts)  

### 🛠️ Professional Features  
- ✨ Enhanced CLI with colors and intuitive design  
- 💬 Persistent conversation history with automatic backups  
- 🌊 Streaming & non-streaming support  
- 📁 File inclusion via `{filename}` syntax  
- ⚙️ Agent-based configuration management  
- 📊 Detailed statistics & analytics  
- 📤 Multi-format exports (JSON, TXT, MD, HTML)  
- 🔐 Secure API key management  
- 🔍 Conversation search & history navigation  
- 🎯 Adaptive timeouts per reasoning effort  

---

## ⚙️ Installation  

1. 📥 Clone or download the repository  
2. ⚙️ Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  
3. 🔑 Set your API key:  
   ```bash
   export OPENAI_API_KEY="your-api-key-here"
   ```  

---

## 🚀 Quick Start  

- ▶️ GPT-5:  
  ```bash
  python main.py --agent-id my-agent --model gpt-5
  ```  

- ⚡ GPT-5 Mini:  
  ```bash
  python main.py --agent-id my-agent --model gpt-5-mini
  ```  

- 🚀 GPT-5 Nano:  
  ```bash
  python main.py --agent-id my-agent --model gpt-5-nano
  ```  

- 📋 List agents:  
  ```bash
  python main.py --list
  ```  

---

## 💻 Interactive Commands  

| Command | Description |
|---------|-------------|
| `/help` | Show all available commands |
| `/history [n]` | Show last n messages |
| `/search <term>` | Search conversation history |
| `/stats` | Show conversation statistics |
| `/config` | Show current configuration |
| `/export <format>` | Export conversation |
| `/clear` | Clear conversation history |
| `/files` | List available files |
| `/info` | Show agent info |
| `/quit` | Exit chat |  

---

## 📁 File Inclusion  

Use `{filename}` to include content:  

```
Can you review this code? {main.py}  
Please analyze configs: {config.yaml}, {settings.json}
```  

Supported file types:  
- Programming → `.py`, `.js`, `.cpp`, `.rs` …  
- Config → `.json`, `.yaml`, `.toml` …  
- Docs → `.md`, `.txt` …  
- Web → `.html`, `.css` …  

---

## 📊 Model Comparison  

| ⚙️ Model | 📌 Best Use Case | ⏱️ Timeout | 🚀 Performance |
|----------|-----------------|------------|----------------|
| **GPT-5** | Complex reasoning, analysis | 3–12 min | 🌟🌟🌟🌟🌟 |
| **GPT-5 Mini** | Balanced workloads | 1.5–6 min | 🌟🌟🌟🌟 |
| **GPT-5 Nano** | Quick/simple tasks | 1–4 min | 🌟🌟🌟 |  

---

## 🗂️ Project Structure  

```
gpt5/
├── main.py
├── config.py
├── agent.py
├── utils.py
├── export.py
├── requirements.txt
├── README.md
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

## 🔐 Security  

- 🔒 Secure storage of API keys  
- 🚫 No sensitive data in logs/exports  
- ✅ Auto `.gitignore` handling  
- 🔑 Multi-model API key support  

---

## 🎨 User Experience  

- 🖼️ ASCII banners & colorful UI  
- ✅ Smart input validation  
- 📊 Rich statistics & export styling  
- ⏳ Progress indicators  
- 🔎 Intuitive navigation & help  

---

## 🐛 Troubleshooting  

- ❌ **API Key Error** → Check validity & credits  
- ⏱️ **Timeout** → Lower reasoning effort  
- 📂 **File not found** → Use `/files`  
- 🔐 **Permission denied** → Check file rights  

---

## 📝 License  

MIT License — for educational & professional use.  

---

## 🤝 Contributing  

Contributions welcome: bug reports, features, docs, code.  

---

**2025-08-29**  
*Université Laval*  
