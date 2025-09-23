# 🤖 Multi-Agent Healthcare Chatbot with AutoGen

A demonstration of Microsoft AutoGen's multi-agent capabilities in healthcare applications, featuring collaborative AI agents that work together to provide medical consultation.

## 🎯 Overview

This project showcases how multiple AI agents can collaborate to simulate a medical team consultation. Instead of a single chatbot, this system uses specialized agents that communicate and validate each other's responses.

## 🏗️ Architecture

### Agent Roles
- **Patient Agent**: Collects symptoms and medical history
- **Diagnosis Agent**: Analyzes symptoms and suggests conditions  
- **Pharmacy Agent**: Recommends medications and treatments
- **Consultation Agent**: Determines if professional medical attention is needed

### Technology Stack
- **AutoGen**: Microsoft's multi-agent orchestration framework
- **GPT-4o**: OpenAI's language model for medical reasoning
- **Streamlit**: Web interface for easy interaction
- **Python 3.8+**: Core implementation

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/account/api-keys))

### Installation
```bash
# Clone the repository
git clone https://github.com/sathvikmaahi/multi-agent-healthcare-chatbot.git
cd multi-agent-healthcare-chatbot

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
export OPENAI_API_KEY=your_api_key_here
```

### Usage

#### Command Line Interface
```bash
python healthcare_chatbot.py
```

#### Web Interface
```bash
streamlit run demo_app.py
# Opens in browser at http://localhost:8501
```

## 📁 Project Structure

```
├── healthcare_chatbot.py              # Main command-line application
├── demo_app.py                        # Streamlit web interface
├── requirements.txt                   # Python dependencies
├── Build Multi-Agent Chatbot...       # Original Jupyter notebook
├── test_healthcare_chatbot.py         # Test suite
└── setup_github_repo.py               # GitHub setup script
```

## 🎮 Demo Examples

### Example 1: Basic Consultation
```bash
python healthcare_chatbot.py
# Enter: "I have headaches and fatigue"
```

### Example 2: Web Interface
```bash
streamlit run demo_app.py
# Open http://localhost:8501 in browser
```

## 🔧 Configuration

### Environment Variables
- `OPENAI_API_KEY`: Your OpenAI API key (required)
- `SYMPTOMS`: Default symptoms for non-interactive mode
- `INTERACTIVE`: Set to "true" for interactive input mode

### Agent Configuration
- **Model**: GPT-4o (configurable in `llm_config`)
- **Max Rounds**: 5 (prevents infinite loops)
- **Speaker Method**: Round-robin (ensures fair turn-taking)

## 🎯 Use Cases

### Healthcare Applications
- **Symptom Checker**: Initial assessment before doctor visits
- **Medical Education**: Teaching students about multi-agent systems
- **Telemedicine**: Supporting remote healthcare consultations

### Business Applications
- **Customer Support**: Multi-agent customer service systems
- **Technical Support**: Collaborative problem-solving agents
- **Consulting**: Multi-expert consultation systems

## 🛠️ Development

### Running Tests
```bash
python test_healthcare_chatbot.py
```

### Code Structure
- `healthcare_chatbot.py`: Core multi-agent implementation
- `demo_app.py`: Streamlit web interface
- `requirements.txt`: All required dependencies


## 🙏 Acknowledgments

- **Microsoft AutoGen**: Multi-agent orchestration framework
- **OpenAI**: GPT-4o language model
- **Streamlit**: Web interface framework


