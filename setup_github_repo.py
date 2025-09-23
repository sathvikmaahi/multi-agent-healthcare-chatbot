#!/usr/bin/env python3
"""
GitHub Repository Setup Script
This script helps you set up a GitHub repository for the Multi-Agent Healthcare Chatbot project.
"""

import os
import subprocess
import sys

def run_command(command, description):
    """Run a shell command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        print(f"Error output: {e.stderr}")
        return None

def check_git_installed():
    """Check if git is installed"""
    result = run_command("git --version", "Checking Git installation")
    return result is not None

def check_git_repo():
    """Check if this is already a git repository"""
    return os.path.exists('.git')

def initialize_git_repo():
    """Initialize git repository"""
    if not check_git_repo():
        run_command("git init", "Initializing Git repository")
    else:
        print("✅ Git repository already initialized")

def add_files():
    """Add files to git"""
    run_command("git add .", "Adding files to Git")

def create_initial_commit():
    """Create initial commit"""
    run_command('git commit -m "Initial commit: Multi-Agent Healthcare Chatbot"', "Creating initial commit")

def setup_gitignore():
    """Ensure .gitignore is properly configured"""
    gitignore_path = '.gitignore'
    if os.path.exists(gitignore_path):
        print("✅ .gitignore already exists")
    else:
        print("❌ .gitignore not found")

def check_required_files():
    """Check if all required files exist"""
    required_files = [
        'README.md',
        'LICENSE',
        'requirements.txt',
        'healthcare_chatbot.py',
        'demo_app.py',
        '.gitignore',
        'CONTRIBUTING.md',
        'SECURITY.md',
        'CHANGELOG.md'
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Missing required files: {', '.join(missing_files)}")
        return False
    else:
        print("✅ All required files present")
        return True

def main():
    """Main setup function"""
    print("🚀 GitHub Repository Setup for Multi-Agent Healthcare Chatbot")
    print("=" * 60)
    
    # Check prerequisites
    if not check_git_installed():
        print("❌ Git is not installed. Please install Git first.")
        sys.exit(1)
    
    # Check required files
    if not check_required_files():
        print("❌ Some required files are missing. Please ensure all files are created.")
        sys.exit(1)
    
    # Initialize git repository
    initialize_git_repo()
    
    # Setup gitignore
    setup_gitignore()
    
    # Add files
    add_files()
    
    # Create initial commit
    create_initial_commit()
    
    print("\n🎉 Git repository setup completed!")
    print("\n📋 Next steps:")
    print("1. Create a new repository on GitHub")
    print("2. Add the remote origin:")
    print("   git remote add origin https://github.com/yourusername/multi-agent-healthcare-chatbot.git")
    print("3. Push to GitHub:")
    print("   git branch -M main")
    print("   git push -u origin main")
    print("\n🔗 GitHub repository creation:")
    print("1. Go to https://github.com/new")
    print("2. Repository name: multi-agent-healthcare-chatbot")
    print("3. Description: Multi-Agent AI Healthcare Consultation System using AutoGen")
    print("4. Make it public")
    print("5. Don't initialize with README (we already have one)")
    print("6. Click 'Create repository'")
    
    print("\n📚 Documentation:")
    print("- README.md: Complete project documentation")
    print("- docs/presentation_script.md: Presentation guide")
    print("- docs/QUICK_START.md: Quick setup guide")
    print("- CONTRIBUTING.md: Contribution guidelines")
    print("- SECURITY.md: Security policy")
    print("- CHANGELOG.md: Version history")

if __name__ == "__main__":
    main()
