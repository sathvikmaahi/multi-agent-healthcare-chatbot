# 🚀 Quick Start Guide

## 📋 **What You Need**
- Python 3.8+
- OpenAI API Key (get one at https://platform.openai.com/account/api-keys)
- 5 minutes of your time

## ⚡ **3-Step Setup**

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Set API Key
```bash
export OPENAI_API_KEY=your_api_key_here
```

### Step 3: Run the Demo
```bash
# Command line version
python healthcare_chatbot.py

# Web interface version
streamlit run demo_app.py
```

## 🎯 **What You'll See**

### Command Line Demo
```
🤖 Multi-Agent Healthcare Chatbot Setup
✅ OpenAI client initialized
✅ All agents created successfully
🎯 System ready for consultation
💬 Multi-agent conversation initiated
📊 Consultation completed
```

### Web Interface Demo
- Interactive symptom input
- Real-time agent collaboration
- Visual conversation flow
- System status monitoring

## 🎮 **Try These Examples**

### Example 1: Headache and Fatigue
```bash
SYMPTOMS="headache and fatigue" python healthcare_chatbot.py
```

### Example 2: Chest Pain
```bash
SYMPTOMS="chest pain and shortness of breath" python healthcare_chatbot.py
```

### Example 3: Interactive Mode
```bash
INTERACTIVE=true python healthcare_chatbot.py
```

## 🔧 **Troubleshooting**

### Common Issues
1. **"API key not found"**
   - Solution: Set `OPENAI_API_KEY` environment variable

2. **"Module not found"**
   - Solution: Install dependencies with `pip install -r requirements.txt`

3. **"Permission denied"**
   - Solution: Use virtual environment: `python -m venv venv && source venv/bin/activate`

### Getting Help
- Check the full README.md for detailed documentation
- Review the presentation_script.md for explanation tips
- Look at the code comments for technical details

## 🎉 **You're Ready!**

Once you see the agents collaborating, you'll understand:
- How multi-agent systems work
- Why collaboration improves AI responses
- How to build scalable AI applications
- The potential of healthcare AI

**Happy exploring!** 🚀
