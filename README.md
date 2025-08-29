# 🌐 OpenAI GPT-5 Unified Chat Agent  

**👨‍💻 Author: Simon-Pierre Boucher**  

✨ A **professional, unified command-line interface (CLI)** for **all OpenAI GPT model variants**, designed to deliver a **legendary user experience**.  

---

## 🚀 Key Features  

### 🔄 Multi-Model Support  
- 🔹 **GPT-5** → Advanced reasoning (3–12 min timeouts)  
- 🔹 **GPT-5 Mini** → Balanced efficiency/performance (1.5–6 min timeouts)  
- 🔹 **GPT-5 Nano** → Speed-optimized lightweight model (1–4 min timeouts)  

### 🛠️ Professional Features  
- ✨ **Enhanced CLI** with colors and intuitive design  
- 💬 **Persistent conversation history** with automatic backups  
- 🌊 **Streaming & non-streaming** support  
- 📁 **File inclusion** via `{filename}` syntax  
- ⚙️ **Advanced agent-based configuration management**  
- 📊 **Detailed statistics & analytics**  
- 📤 **Export formats**: JSON, TXT, Markdown, HTML  
- 🔐 **Secure API key management** with env & file support  
- 🔍 **Conversation search** and history navigation  
- 🎯 **Adaptive timeouts** based on reasoning effort  

---

## 📦 Installation  

1. 📥 Clone or download the repository  
2. ⚙️ Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  
3. 🔑 Set your OpenAI API key:  
   ```bash
   export OPENAI_API_KEY="your-api-key-here"
   ```  
   *(or the program will prompt you and store it securely)*  

---

## 🎯 Quick Start  

- ▶️ Start GPT-5:  
  ```bash
  python main.py --agent-id my-agent --model gpt-5
  ```  
- ⚡ GPT-5 Mini (faster responses):  
  ```bash
  python main.py --agent-id my-agent --model gpt-5-mini
  ```  
- 🚀 GPT-5 Nano (optimized for speed):  
  ```bash
  python main.py --agent-id my-agent --model gpt-5-nano
  ```  
- 📋 List all agents:  
  ```bash
  python main.py --list
  ```  
- 🛠️ Configure an agent:  
  ```bash
  python main.py --agent-id my-agent --config
  ```  
- 🔍 View agent details:  
  ```bash
  python main.py --info my-agent
  ```  

---

## 💻 Interactive Commands  

- `/help` → Show all commands  
- `/history [n]` → Display last n messages  
- `/search <term>` → Search conversation history  
- `/stats` → Show conversation stats  
- `/config` → View current configuration  
- `/export <format>` → Export (json | txt | md | html)  
- `/clear` → Clear history  
- `/files` → List available files  
- `/info` → Show agent info  
- `/quit` → Exit session  

---

## 📁 File Inclusion  

Easily include file contents inside messages:  

```
Can you review this code? {main.py}  

Please analyze these configs: {config.yaml}, {settings.json}
```  

✅ Supported file types:  
- Programming files (.py, .js, .ts, .java, .cpp, .rs, etc.)  
- Config files (.yaml, .json, .toml, .env, etc.)  
- Documentation (.md, .txt, .rst)  
- Web files (.html, .css, .scss)  
- …and more  

---

## 📊 Model Comparison  

| ⚙️ Model       | 📌 Best Use Case            | ⏱️ Timeout | 🚀 Performance |
|----------------|-----------------------------|------------|----------------|
| **GPT-5**      | Complex reasoning & analysis | 3–12 min   | 🌟🌟🌟🌟🌟 |
| **GPT-5 Mini** | Balanced workloads           | 1.5–6 min  | 🌟🌟🌟🌟 |
| **GPT-5 Nano** | Quick/simple tasks           | 1–4 min    | 🌟🌟🌟 |  

---

## 🗂️ Project Structure  

```
gpt5/
├── main.py           # Main CLI app
├── config.py         # Config & model definitions
├── agent.py          # Core agent logic
├── utils.py          # Utility functions
├── export.py         # Export functionality
├── requirements.txt  # Python dependencies
├── README.md         # This file
└── agents/           # Agent data
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
- ✅ Auto `.gitignore` handling for keys  
- 🔑 Multi-model API key support  

---

## 🎨 User Experience  

- 🖼️ Beautiful ASCII banners & colors  
- ✅ Smart input validation  
- 📊 Rich statistics & export formatting  
- ⏳ Progress indicators for reasoning  
- 🔎 Intuitive navigation & command help  

---

## 🐛 Troubleshooting  

- ❌ **API Key Error** → Check validity & credits  
- ⏱️ **Timeout** → Lower reasoning effort  
- 📂 **File not found** → Use `/files` command  
- 🔐 **Permission denied** → Check write access  

---

## 📝 License  

📜 Provided as-is for educational and professional use.  

---

## 🤝 Contributing  

Contributions are welcome to make the agent even more **robust, aesthetic, and powerful**.  

---

**2025-08-29**  
*Université Laval*  
