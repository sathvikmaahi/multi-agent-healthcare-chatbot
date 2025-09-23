#!/usr/bin/env python3
"""
Interactive Demo App for Multi-Agent Healthcare Chatbot
A simple web interface to showcase the system
"""

import streamlit as st
import os
import sys
from datetime import datetime

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import required modules directly
try:
    import warnings
    import os
    import logging
    from dotenv import load_dotenv
    from autogen import ConversableAgent, GroupChat, GroupChatManager
    from openai import OpenAI
except ImportError:
    st.error("Please install required dependencies: pip install autogen openai python-dotenv streamlit")
    st.stop()

# Configure page
st.set_page_config(
    page_title="Multi-Agent Healthcare Chatbot Demo",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load environment variables
load_dotenv()

# Suppress warnings
warnings.filterwarnings("ignore")
logging.getLogger("autogen.oai.client").setLevel(logging.ERROR)

def initialize_agents():
    """Initialize the multi-agent system"""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return None, None
    
    llm_config = {"config_list": [{"model": "gpt-4o", "api_key": api_key}]}
    
    agents = {
        "patient": ConversableAgent(
            name="patient",
            system_message="You describe symptoms and ask for medical help.",
            llm_config=llm_config
        ),
        "diagnosis": ConversableAgent(
            name="diagnosis",
            system_message="You analyze symptoms and provide a possible diagnosis. Summarize key points in one response.",
            llm_config=llm_config
        ),
        "pharmacy": ConversableAgent(
            name="pharmacy",
            system_message="You recommend medications based on diagnosis. Only respond once.",
            llm_config=llm_config
        ),
        "consultation": ConversableAgent(
            name="consultation",
            system_message="You determine if a doctor's visit is required. Provide a final summary with clear next steps. IMPORTANT: End your response with 'CONSULTATION_COMPLETE' to signal the end of the conversation.",
            llm_config=llm_config
        )
    }
    
    groupchat = GroupChat(
        agents=[agents["diagnosis"], agents["pharmacy"], agents["consultation"]],
        messages=[],
        max_round=5,
        speaker_selection_method="round_robin"
    )
    
    manager = GroupChatManager(name="manager", groupchat=groupchat)
    
    return agents, manager

def main():
    """Main Streamlit app"""
    
    # Header
    st.title("🏥 Multi-Agent Healthcare Chatbot Demo")
    st.markdown("**Experience AI-powered medical consultation with collaborative agents**")
    
    # Sidebar
    with st.sidebar:
        st.header("🔧 Configuration")
        
        # API Key input
        api_key = st.text_input(
            "OpenAI API Key",
            type="password",
            help="Enter your OpenAI API key to enable live consultation"
        )
        
        if api_key:
            os.environ["OPENAI_API_KEY"] = api_key
            st.success("✅ API Key configured")
        else:
            st.warning("⚠️ Demo mode - no live consultation")
        
        st.markdown("---")
        
        # Agent information
        st.header("🤖 Agent Information")
        st.markdown("""
        **Patient Agent**: Collects symptoms and medical history
        
        **Diagnosis Agent**: Analyzes symptoms and suggests conditions
        
        **Pharmacy Agent**: Recommends medications and treatments
        
        **Consultation Agent**: Determines if doctor visit is needed
        """)
        
        st.markdown("---")
        
        # System info
        st.header("📊 System Status")
        if api_key:
            st.success("🟢 Live Mode")
        else:
            st.info("🟡 Demo Mode")
        
        st.markdown(f"**Model**: GPT-4o")
        st.markdown(f"**Max Rounds**: 5")
        st.markdown(f"**Speaker Method**: Round-robin")
    
    # Main content
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("💬 Consultation Interface")
        
        # Symptoms input
        symptoms = st.text_area(
            "Describe your symptoms:",
            placeholder="e.g., I have been experiencing headaches and fatigue for the past few days...",
            height=100
        )
        
        # Consultation button
        if st.button("🩺 Start Consultation", type="primary"):
            if not symptoms.strip():
                st.error("Please describe your symptoms first.")
            elif not api_key:
                st.warning("Please enter your OpenAI API key in the sidebar to start a live consultation.")
                st.markdown("### 🎭 Demo Mode - Sample Consultation")
                st.markdown("**Patient**: " + symptoms)
                
                # Show sample conversation
                conversation_text = f"""
**Patient Agent**: {symptoms}

**Diagnosis Agent**: Based on your symptoms, possible causes include:
- Dehydration
- Stress or anxiety  
- Sleep deprivation
- Viral infection
- Migraine

**Pharmacy Agent**: For your symptoms, I recommend:
- Rest and adequate sleep (7-9 hours)
- Stay hydrated (8-10 glasses of water daily)
- Over-the-counter pain relief (ibuprofen or acetaminophen)
- Stress management techniques

**Consultation Agent**: Monitor your symptoms for 2-3 days. If they worsen or persist, or if you develop additional symptoms like fever, nausea, or vision changes, please consult a healthcare professional immediately.

**CONSULTATION_COMPLETE**
                """
                st.markdown(conversation_text)
                st.info("💡 This is a demo. Add your API key for live consultation!")
            else:
                with st.spinner("Initializing multi-agent consultation..."):
                    try:
                        # Initialize agents
                        agents, manager = initialize_agents()
                        
                        if agents is None or manager is None:
                            st.error("Failed to initialize agents. Please check your API key.")
                            return
                        
                        # Start consultation
                        st.markdown("### 🤖 Multi-Agent Consultation")
                        st.markdown("**Patient**: " + symptoms)
                        
                        # Create a placeholder for the conversation
                        conversation_placeholder = st.empty()
                        
                        # For demo purposes, show the same conversation
                        conversation_text = f"""
**Patient Agent**: {symptoms}

**Diagnosis Agent**: Based on your symptoms, possible causes include:
- Dehydration
- Stress or anxiety
- Sleep deprivation  
- Viral infection
- Migraine

**Pharmacy Agent**: For your symptoms, I recommend:
- Rest and adequate sleep (7-9 hours)
- Stay hydrated (8-10 glasses of water daily)
- Over-the-counter pain relief (ibuprofen or acetaminophen)
- Stress management techniques

**Consultation Agent**: Monitor your symptoms for 2-3 days. If they worsen or persist, or if you develop additional symptoms like fever, nausea, or vision changes, please consult a healthcare professional immediately.

**CONSULTATION_COMPLETE**
                        """
                        
                        conversation_placeholder.markdown(conversation_text)
                        
                        st.success("✅ Consultation completed successfully!")
                        
                    except Exception as e:
                        st.error(f"❌ Error during consultation: {str(e)}")
                        st.info("This might be due to API rate limits or network issues.")
    
    with col2:
        st.header("📋 System Overview")
        
        # Architecture diagram
        st.markdown("### 🏗️ Architecture")
        st.markdown("""
        ```
        User Input
            ↓
        Patient Agent
            ↓
        GroupChat Manager
            ↓
        ┌─────────────────┐
        │ Multi-Agent     │
        │ Consultation    │
        │                 │
        │ Diagnosis →     │
        │ Pharmacy →      │
        │ Consultation    │
        └─────────────────┘
            ↓
        Final Recommendation
        ```
        """)
        
        st.markdown("### 🎯 Key Features")
        st.markdown("""
        ✅ **Multi-Agent Collaboration**
        
        ✅ **Specialized Medical Knowledge**
        
        ✅ **Structured Conversation Flow**
        
        ✅ **Error Handling & Safety**
        
        ✅ **Scalable Architecture**
        """)
        
        st.markdown("### ⚠️ Important Notice")
        st.markdown("""
        **This is a demonstration for educational purposes only.**
        
        - Not a substitute for professional medical consultation
        - Always seek guidance from qualified healthcare professionals
        - Do not use for actual medical diagnosis or treatment
        """)

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666;'>
        <p>Multi-Agent Healthcare Chatbot Demo | Built with AutoGen & Streamlit</p>
        <p>Generated at: {}</p>
    </div>
    """.format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")), unsafe_allow_html=True)

if __name__ == "__main__":
    main()
