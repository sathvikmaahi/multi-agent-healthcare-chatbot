#!/usr/bin/env python3
"""
Multi-Agent Healthcare Chatbot using AutoGen
Fixed version of the notebook that runs end-to-end without errors
"""

import warnings
import os
import sys

# Suppress autogen and other deprecation/user warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings('ignore', category=UserWarning)

try:
    from autogen import ConversableAgent, GroupChat, GroupChatManager
    from openai import OpenAI
    from dotenv import load_dotenv
    import logging
except ImportError as e:
    print(f"Missing dependencies: {e}")
    print("Please install: pip install autogen==0.7 openai==1.64.0 python-dotenv==1.1.0")
    sys.exit(1)

# Load environment variables from a .env file if present
load_dotenv()

# Suppress warnings from autogen.oai.client
logging.getLogger("autogen.oai.client").setLevel(logging.ERROR)

print("🤖 Multi-Agent Healthcare Chatbot Setup")
print("=" * 50)

# Initialize OpenAI Client (API Key is automatically managed from environment variables)
client = OpenAI()

# Disable Docker execution to prevent runtime errors
code_execution_config = {"use_docker": False}

# Sample LLM Configuration
llm_config = {"config_list": [{"model": "gpt-4o", "api_key": os.getenv("OPENAI_API_KEY")}]}

print(f"✅ OpenAI client initialized")
print(f"✅ LLM config set to: {llm_config['config_list'][0]['model']}")

# Check if API key is available
if not os.getenv("OPENAI_API_KEY"):
    print("⚠️  OPENAI_API_KEY not set. Creating agents but skipping live chat.")
    print("   Set OPENAI_API_KEY environment variable to run the full demo.")
else:
    print("✅ OpenAI API key found")

print("\n📋 Creating AI Agents...")

# Step 1: Create AI Agents with Defined Roles
patient_agent = ConversableAgent(
    name="patient", 
    system_message="You describe symptoms and ask for medical help.", 
    llm_config=llm_config
)

diagnosis_agent = ConversableAgent(
    name="diagnosis", 
    system_message="You analyze symptoms and provide a possible diagnosis. Summarize key points in one response.", 
    llm_config=llm_config
)

pharmacy_agent = ConversableAgent(
    name="pharmacy", 
    system_message="You recommend medications based on diagnosis. Only respond once.", 
    llm_config=llm_config
)

consultation_agent = ConversableAgent(
    name="consultation", 
    system_message="You determine if a doctor's visit is required. Provide a final summary with clear next steps. IMPORTANT: End your response with 'CONSULTATION_COMPLETE' to signal the end of the conversation.", 
    llm_config=llm_config
)

print("✅ Patient agent created")
print("✅ Diagnosis agent created") 
print("✅ Pharmacy agent created")
print("✅ Consultation agent created")

# Step 2: Create GroupChat for Structured Interaction
groupchat = GroupChat(
    agents=[diagnosis_agent, pharmacy_agent, consultation_agent],  # Patient only initiates
    messages=[], 
    max_round=5,  # Limits conversation to 5 rounds
    speaker_selection_method="round_robin"  # Ensures structured conversation flow
)

print("✅ GroupChat created with round-robin speaker selection")

# Step 3: Create GroupChatManager to Handle Conversation
manager = GroupChatManager(name="manager", groupchat=groupchat)

print("✅ GroupChatManager created")

print("\n🎯 Healthcare Consultation System Ready!")
print("=" * 50)

# Step 4: Get Patient Input and Start Consultation
print("\n🤖 Welcome to the AI Healthcare Consultation System!")

# Get symptoms - use environment variable for non-interactive runs
symptoms = os.getenv("SYMPTOMS", "headache and fatigue")

if os.getenv("INTERACTIVE", "false").lower() == "true":
    try:
        symptoms = input("🩺 Please describe your symptoms: ")
    except EOFError:
        print("🩺 Using default symptoms: headache and fatigue")
        symptoms = "headache and fatigue"

print(f"🩺 Patient symptoms: {symptoms}")

if not os.getenv("OPENAI_API_KEY"):
    print("\n⚠️ OPENAI_API_KEY not set. Skipping live chat run.")
    print("   To run the full demo:")
    print("   1. Set OPENAI_API_KEY environment variable")
    print("   2. Run: python healthcare_chatbot.py")
    print("   3. Or run interactively: INTERACTIVE=true python healthcare_chatbot.py")
else:
    print("\n🩺 Diagnosing symptoms...")
    try:
        response = patient_agent.initiate_chat(
            manager,
            message=f"I am feeling {symptoms}. Can you help?",
        )
        print("\n✅ Consultation completed successfully!")
    except Exception as e:
        print(f"\n❌ Error during consultation: {e}")
        print("This might be due to API rate limits or network issues.")

print("\n📊 System Summary:")
print(f"   - Agents created: 4")
print(f"   - GroupChat rounds: 5")
print(f"   - Speaker method: round_robin")
print(f"   - Model: {llm_config['config_list'][0]['model']}")
print(f"   - API key configured: {'Yes' if os.getenv('OPENAI_API_KEY') else 'No'}")

print("\n🎉 Multi-Agent Healthcare Chatbot Demo Complete!")
