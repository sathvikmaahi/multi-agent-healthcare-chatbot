# Contributing to Multi-Agent Healthcare Chatbot

Thank you for your interest in contributing to this project! This document provides guidelines for contributing to the Multi-Agent Healthcare Chatbot.

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- Git
- OpenAI API key (for testing)
- Basic understanding of multi-agent systems

### Setup Development Environment
```bash
# Clone the repository
git clone https://github.com/yourusername/multi-agent-healthcare-chatbot.git
cd multi-agent-healthcare-chatbot

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install pytest black flake8
```

## 📋 How to Contribute

### 1. Fork and Clone
1. Fork the repository on GitHub
2. Clone your fork locally
3. Create a new branch for your feature/fix

### 2. Make Changes
- Follow the existing code style
- Add tests for new functionality
- Update documentation as needed
- Ensure all tests pass

### 3. Submit Pull Request
1. Push your changes to your fork
2. Create a pull request with a clear description
3. Wait for review and feedback

## 🎯 Areas for Contribution

### High Priority
- **New Agent Types**: Add specialized medical agents (cardiology, neurology, etc.)
- **UI Improvements**: Enhance the Streamlit interface
- **Error Handling**: Improve error handling and user feedback
- **Testing**: Add comprehensive test suite
- **Documentation**: Improve code comments and documentation

### Medium Priority
- **Performance**: Optimize agent communication
- **Internationalization**: Add multi-language support
- **Voice Interface**: Add speech-to-text capabilities
- **Mobile App**: Create mobile interface
- **Analytics**: Add conversation analytics

### Low Priority
- **Themes**: Add UI themes and customization
- **Plugins**: Create plugin system for agents
- **Deployment**: Add Docker and cloud deployment guides
- **Monitoring**: Add system monitoring and logging

## 📝 Code Style Guidelines

### Python Code
- Follow PEP 8 style guide
- Use type hints where appropriate
- Write docstrings for functions and classes
- Keep functions small and focused

### Example:
```python
def create_agent(name: str, system_message: str, llm_config: dict) -> ConversableAgent:
    """
    Create a new ConversableAgent with specified configuration.
    
    Args:
        name: Agent name
        system_message: System message for the agent
        llm_config: LLM configuration dictionary
        
    Returns:
        ConversableAgent: Configured agent instance
    """
    return ConversableAgent(
        name=name,
        system_message=system_message,
        llm_config=llm_config
    )
```

### Commit Messages
Use clear, descriptive commit messages:
- `feat: add cardiology agent for heart-related consultations`
- `fix: resolve API key validation issue`
- `docs: update README with new installation steps`
- `test: add unit tests for agent creation`

## 🧪 Testing

### Running Tests
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=healthcare_chatbot

# Run specific test file
pytest tests/test_agents.py
```

### Writing Tests
- Test both success and failure cases
- Mock external API calls
- Test agent interactions
- Verify error handling

### Example Test:
```python
import pytest
from unittest.mock import Mock, patch
from healthcare_chatbot import create_agent

def test_agent_creation():
    """Test that agents are created with correct configuration."""
    llm_config = {"model": "gpt-4o", "api_key": "test_key"}
    
    agent = create_agent("test_agent", "Test message", llm_config)
    
    assert agent.name == "test_agent"
    assert agent.system_message == "Test message"
    assert agent.llm_config == llm_config
```

## 📚 Documentation

### Code Documentation
- Add docstrings to all functions and classes
- Include type hints
- Explain complex algorithms
- Add inline comments for non-obvious code

### User Documentation
- Update README.md for new features
- Add examples and use cases
- Include troubleshooting guides
- Update installation instructions

### API Documentation
- Document all public functions
- Include parameter descriptions
- Provide usage examples
- Explain return values

## 🐛 Reporting Issues

### Bug Reports
When reporting bugs, please include:
- Clear description of the issue
- Steps to reproduce
- Expected vs actual behavior
- Environment details (OS, Python version, etc.)
- Error messages or logs

### Feature Requests
For feature requests, please include:
- Clear description of the feature
- Use cases and benefits
- Potential implementation approach
- Any relevant examples

## 🔒 Security

### Security Considerations
- Never commit API keys or secrets
- Use environment variables for sensitive data
- Validate all user inputs
- Follow security best practices

### Reporting Security Issues
- Email security issues to: security@example.com
- Do not create public issues for security vulnerabilities
- Include detailed information about the issue

## 📄 License

By contributing to this project, you agree that your contributions will be licensed under the MIT License.

## 🤝 Code of Conduct

### Our Pledge
We are committed to providing a welcoming and inclusive environment for all contributors.

### Expected Behavior
- Be respectful and inclusive
- Accept constructive criticism
- Focus on what's best for the community
- Show empathy towards other community members

### Unacceptable Behavior
- Harassment or discrimination
- Trolling or inflammatory comments
- Personal attacks or political discussions
- Spam or off-topic discussions

## 📞 Getting Help

### Questions and Support
- Create an issue for questions
- Use GitHub Discussions for general discussions
- Check existing documentation first
- Be specific about your problem

### Community
- Join our Discord server (if available)
- Follow us on Twitter (if available)
- Star the repository if you find it useful

## 🎉 Recognition

### Contributors
All contributors will be recognized in:
- CONTRIBUTORS.md file
- Release notes
- Project documentation

### Types of Contributions
We welcome all types of contributions:
- Code contributions
- Documentation improvements
- Bug reports and fixes
- Feature requests
- Testing and quality assurance
- Community support

Thank you for contributing to the Multi-Agent Healthcare Chatbot! 🚀
