# Multi-Agent Healthcare Chatbot with AutoGen

A demonstration of Microsoft AutoGen's multi-agent capabilities in healthcare applications, featuring collaborative AI agents that work together to provide medical consultation.

## Overview

This project showcases how multiple AI agents can collaborate to simulate a medical team consultation. Instead of a single chatbot, this system uses specialized agents that communicate and validate each other's responses.

## Architecture

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

## Quick Start

### Prerequisites:
- Python 3.8 or higher

### Installation:
```bash
# Clone the repository
git clone https://github.com/sathvikmaahi/multi-agent-healthcare-chatbot.git
cd multi-agent-healthcare-chatbot

# Install dependencies
pip install -r requirements.txt


### Usage

#### Web Interface
```bash
streamlit run demo_app.py
# Opens in browser at http://localhost:8501
```

## Project Structure:

```
├── healthcare_chatbot.py              # Main command-line application
├── demo_app.py                        # Streamlit web interface to interact with the chatbot
├── requirements.txt                   # Python dependencies required to run the chatbot
├── Build Multi-Agent Chatbot...       # Original Jupyter notebook
├── test_healthcare_chatbot.py         # Test suite
```

### Agent Configuration:
- **Model**: GPT-4o (configurable in `llm_config`)
- **Max Rounds**: 5 (prevents infinite loops)
- **Speaker Method**: Round-robin (ensures fair turn-taking)

## Use Cases:

### Healthcare Applications:
- **Symptom Checker**: Initial assessment before doctor visits
- **Medical Education**: Teaching students about multi-agent systems
- **Telemedicine**: Supporting remote healthcare consultations

### Business Applications:
- **Customer Support**: Multi-agent customer service systems
- **Technical Support**: Collaborative problem-solving agents
- **Consulting**: Multi-expert consultation systems


### Code Structure:
- `healthcare_chatbot.py`: Core multi-agent implementation
- `demo_app.py`: Streamlit web interface
- `requirements.txt`: All required dependencies


## Acknowledgments:
- **Microsoft AutoGen**: Multi-agent orchestration framework
- **OpenAI**: GPT-4o language model
- **Streamlit**: Web interface framework


