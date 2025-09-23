#!/usr/bin/env python3
"""
Test suite for Multi-Agent Healthcare Chatbot
"""

import pytest
import os
import sys
from unittest.mock import Mock, patch, MagicMock

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test that all required modules can be imported"""
    try:
        import warnings
        import os
        from dotenv import load_dotenv
        from autogen import ConversableAgent, GroupChat, GroupChatManager
        from openai import OpenAI
        import logging
        assert True
    except ImportError as e:
        pytest.fail(f"Failed to import required modules: {e}")

def test_environment_loading():
    """Test that environment variables can be loaded"""
    from dotenv import load_dotenv
    load_dotenv()
    assert True  # If no exception is raised, test passes

@patch('os.getenv')
def test_agent_creation_without_api_key(mock_getenv):
    """Test agent creation when no API key is provided"""
    mock_getenv.return_value = None
    
    # This should not raise an exception
    from healthcare_chatbot import initialize_agents
    agents, manager = initialize_agents()
    
    assert agents is None
    assert manager is None

@patch('os.getenv')
@patch('autogen.ConversableAgent')
@patch('autogen.GroupChat')
@patch('autogen.GroupChatManager')
def test_agent_creation_with_api_key(mock_manager, mock_groupchat, mock_agent, mock_getenv):
    """Test agent creation when API key is provided"""
    mock_getenv.return_value = "test_api_key"
    
    # Mock the agent creation
    mock_agent_instance = Mock()
    mock_agent.return_value = mock_agent_instance
    
    # Mock the groupchat
    mock_groupchat_instance = Mock()
    mock_groupchat.return_value = mock_groupchat_instance
    
    # Mock the manager
    mock_manager_instance = Mock()
    mock_manager.return_value = mock_manager_instance
    
    from healthcare_chatbot import initialize_agents
    agents, manager = initialize_agents()
    
    assert agents is not None
    assert manager is not None
    assert mock_agent.call_count == 4  # 4 agents should be created

def test_healthcare_chatbot_script_exists():
    """Test that the main healthcare chatbot script exists and is executable"""
    script_path = os.path.join(os.path.dirname(__file__), 'healthcare_chatbot.py')
    assert os.path.exists(script_path)
    assert os.access(script_path, os.R_OK)

def test_demo_app_script_exists():
    """Test that the demo app script exists and is executable"""
    script_path = os.path.join(os.path.dirname(__file__), 'demo_app.py')
    assert os.path.exists(script_path)
    assert os.access(script_path, os.R_OK)

def test_requirements_file_exists():
    """Test that requirements.txt exists and contains required packages"""
    requirements_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    assert os.path.exists(requirements_path)
    
    with open(requirements_path, 'r') as f:
        content = f.read()
        assert 'autogen' in content
        assert 'openai' in content
        assert 'python-dotenv' in content
        assert 'streamlit' in content

def test_readme_exists():
    """Test that README.md exists and contains key information"""
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    assert os.path.exists(readme_path)
    
    with open(readme_path, 'r') as f:
        content = f.read()
        assert 'Multi-Agent Healthcare Chatbot' in content
        assert 'AutoGen' in content
        assert 'Installation' in content

def test_license_exists():
    """Test that LICENSE file exists"""
    license_path = os.path.join(os.path.dirname(__file__), 'LICENSE')
    assert os.path.exists(license_path)

def test_contributing_exists():
    """Test that CONTRIBUTING.md exists"""
    contributing_path = os.path.join(os.path.dirname(__file__), 'CONTRIBUTING.md')
    assert os.path.exists(contributing_path)

def test_security_exists():
    """Test that SECURITY.md exists"""
    security_path = os.path.join(os.path.dirname(__file__), 'SECURITY.md')
    assert os.path.exists(security_path)

def test_changelog_exists():
    """Test that CHANGELOG.md exists"""
    changelog_path = os.path.join(os.path.dirname(__file__), 'CHANGELOG.md')
    assert os.path.exists(changelog_path)

def test_gitignore_exists():
    """Test that .gitignore exists"""
    gitignore_path = os.path.join(os.path.dirname(__file__), '.gitignore')
    assert os.path.exists(gitignore_path)

def test_docs_directory_exists():
    """Test that docs directory exists and contains documentation"""
    docs_path = os.path.join(os.path.dirname(__file__), 'docs')
    assert os.path.exists(docs_path)
    assert os.path.isdir(docs_path)
    
    # Check for key documentation files
    expected_files = ['presentation_script.md', 'QUICK_START.md', 'PROJECT_SUMMARY.md']
    for file in expected_files:
        file_path = os.path.join(docs_path, file)
        assert os.path.exists(file_path)

def test_github_workflow_exists():
    """Test that GitHub Actions workflow exists"""
    workflow_path = os.path.join(os.path.dirname(__file__), '.github', 'workflows', 'ci.yml')
    assert os.path.exists(workflow_path)

@patch('healthcare_chatbot.OpenAI')
def test_openai_client_initialization(mock_openai):
    """Test OpenAI client initialization"""
    mock_client = Mock()
    mock_openai.return_value = mock_client
    
    from healthcare_chatbot import OpenAI
    client = OpenAI()
    
    mock_openai.assert_called_once()
    assert client == mock_client

def test_medical_disclaimer_present():
    """Test that medical disclaimer is present in key files"""
    files_to_check = ['README.md', 'LICENSE', 'SECURITY.md']
    
    for filename in files_to_check:
        file_path = os.path.join(os.path.dirname(__file__), filename)
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                content = f.read()
                assert 'medical' in content.lower() or 'healthcare' in content.lower()

if __name__ == '__main__':
    pytest.main([__file__])
