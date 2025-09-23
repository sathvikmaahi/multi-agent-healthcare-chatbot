# 🤖 Multi-Agent Healthcare Chatbot

## 🎯 Overview

This project demonstrates a **Multi-Agent AI Healthcare Consultation System** built using Microsoft's AutoGen framework. Instead of a single AI chatbot, this system uses multiple specialized AI agents that collaborate to provide comprehensive medical guidance, similar to a medical team consultation.

### 🌟 Key Features

- **🤖 Multi-Agent Collaboration**: 4 specialized AI agents working together
- **🏥 Healthcare Focus**: Medical consultation simulation
- **🔄 Structured Conversations**: Round-robin agent interactions
- **🌐 Web Interface**: Streamlit-based demo application
- **💻 Command Line**: Terminal-based interaction
- **📚 Comprehensive Documentation**: Complete guides and examples

## 🏗️ Architecture

### Agent Roles
```
Patient Agent → "I have headaches and fatigue"
    ↓
Diagnosis Agent → "Possible causes: dehydration, stress, migraines"
    ↓
Pharmacy Agent → "Recommend: rest, hydration, ibuprofen"
    ↓
Consultation Agent → "Monitor symptoms, see doctor if worsening. CONSULTATION_COMPLETE"
```

### Technology Stack
- **AutoGen**: Microsoft's multi-agent orchestration platform
- **GPT-4o**: OpenAI's latest language model
- **Streamlit**: Web interface framework
- **Python 3.8+**: Core programming language

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/account/api-keys))

### Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/multi-agent-healthcare-chatbot.git
cd multi-agent-healthcare-chatbot

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
export OPENAI_API_KEY=your_api_key_here
```

### Usage

#### Command Line Interface
```bash
# Basic usage
python healthcare_chatbot.py

# With custom symptoms
SYMPTOMS="chest pain and fatigue" python healthcare_chatbot.py

# Interactive mode
INTERACTIVE=true python healthcare_chatbot.py
```

#### Web Interface
```bash
# Start web application
streamlit run demo_app.py
# Opens in browser at http://localhost:8501
```

## 📁 Project Structure

```
multi-agent-healthcare-chatbot/
├── 📄 README.md                          # This file
├── 📄 LICENSE                            # MIT License
├── 📄 CONTRIBUTING.md                    # Contribution guidelines
├── 📄 SECURITY.md                        # Security policy
├── 📄 CHANGELOG.md                       # Version history
├── 📄 requirements.txt                   # Python dependencies
├── 🐍 healthcare_chatbot.py              # Main application
├── 🌐 demo_app.py                        # Web interface
├── 📓 Build Multi-Agent Chatbot...       # Original notebook
├── 📄 chatbot_output.txt                # Sample output
└── 📁 docs/                              # Documentation
    ├── presentation_script.md
    ├── QUICK_START.md
    └── PROJECT_SUMMARY.md
```
