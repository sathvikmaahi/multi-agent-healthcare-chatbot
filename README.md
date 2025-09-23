# 🤖 Multi-Agent Healthcare Chatbot

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![AutoGen](https://img.shields.io/badge/AutoGen-0.7-green.svg)](https://microsoft.github.io/autogen/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-purple.svg)](https://openai.com)

> **⚠️ Medical Disclaimer**: This is an educational demonstration project. It is NOT a medical device and should NOT be used for actual medical diagnosis or treatment. Always consult qualified healthcare professionals.

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

## 🎮 Demo Examples

### Example 1: Basic Consultation
```bash
python healthcare_chatbot.py
# Enter: "I have headaches and fatigue"
```

### Example 2: Non-Interactive Mode
```bash
SYMPTOMS="chest pain and shortness of breath" python healthcare_chatbot.py
```

### Example 3: Web Interface
```bash
streamlit run demo_app.py
# Open http://localhost:8501 in browser
```

## 🔧 Configuration

### Environment Variables
- `OPENAI_API_KEY`: Your OpenAI API key (required for live demo)
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

### Educational Applications
- **AI Learning**: Understanding multi-agent architectures
- **Medical Training**: Simulating medical team consultations
- **Research**: Studying agent collaboration patterns

## 🛠️ Development

### Setting Up Development Environment
```bash
# Install development dependencies
pip install pytest black flake8

# Run tests
pytest

# Format code
black .

# Lint code
flake8 .
```

### Contributing
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## 📊 Performance

### System Requirements
- **Memory**: ~100-200MB
- **CPU**: Minimal (mostly API calls)
- **Network**: Internet connection required
- **Storage**: ~50MB for dependencies

### Response Times
- **Agent Creation**: ~2-3 seconds
- **Response Time**: ~5-10 seconds per agent
- **Total Consultation**: ~30-60 seconds

## 🔒 Security

### Important Notes
- **API Keys**: Never commit API keys to version control
- **User Data**: No user data is stored permanently
- **Conversations**: Conversations are not logged or stored
- **Privacy**: Use environment variables for sensitive data

See [SECURITY.md](SECURITY.md) for detailed security information.

## 📈 Roadmap

### Version 1.1.0 (Planned)
- **Voice Interface**: Speech-to-text input
- **Medical Database**: Integration with medical knowledge bases
- **Multi-language**: Support for multiple languages
- **Mobile App**: Native iOS/Android applications

### Version 1.2.0 (Planned)
- **Specialist Agents**: Cardiology, neurology, pediatrics
- **Medical Records**: Integration with patient history
- **Drug Interactions**: Real-time medication checking
- **Emergency Detection**: Critical symptom identification

### Version 2.0.0 (Planned)
- **Advanced AI Models**: Integration with other LLMs
- **Custom Agent Types**: User-defined agent roles
- **Plugin System**: Extensible architecture
- **Cloud Deployment**: AWS/Azure/GCP support

## 🤝 Community

### Getting Help
- **Issues**: [GitHub Issues](https://github.com/yourusername/multi-agent-healthcare-chatbot/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/multi-agent-healthcare-chatbot/discussions)
- **Documentation**: Check the docs/ folder

### Contributing
- **Code**: Submit pull requests
- **Documentation**: Improve guides and examples
- **Testing**: Add test cases
- **Community**: Help other users

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Important Disclaimers

### Medical Disclaimer
> **This is a demonstration project for educational purposes only.**
> 
> - Not a substitute for professional medical consultation
> - Always seek guidance from qualified healthcare professionals
> - Do not use for actual medical diagnosis or treatment

### Technical Limitations
- Requires OpenAI API key for full functionality
- Internet connection needed for API calls
- Rate limits may apply with heavy usage

## 🙏 Acknowledgments

- **Microsoft AutoGen**: Multi-agent orchestration framework
- **OpenAI**: GPT-4o language model
- **Streamlit**: Web interface framework
- **Contributors**: All project contributors

## 📞 Contact

- **Repository**: [GitHub](https://github.com/yourusername/multi-agent-healthcare-chatbot)
- **Issues**: [GitHub Issues](https://github.com/yourusername/multi-agent-healthcare-chatbot/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/multi-agent-healthcare-chatbot/discussions)

---

## 🎉 Getting Started

Ready to explore multi-agent AI? Start here:

1. **📖 Read the [Quick Start Guide](docs/QUICK_START.md)**
2. **🎮 Try the [Web Demo](http://localhost:8501)**
3. **💻 Run the [Command Line Version](healthcare_chatbot.py)**
4. **📚 Explore the [Documentation](docs/)**

**Happy exploring!** 🚀

---

<div align="center">

**⭐ Star this repository if you find it useful!**

[![GitHub stars](https://img.shields.io/github/stars/yourusername/multi-agent-healthcare-chatbot.svg?style=social&label=Star)](https://github.com/yourusername/multi-agent-healthcare-chatbot)
[![GitHub forks](https://img.shields.io/github/forks/yourusername/multi-agent-healthcare-chatbot.svg?style=social&label=Fork)](https://github.com/yourusername/multi-agent-healthcare-chatbot/fork)

</div>