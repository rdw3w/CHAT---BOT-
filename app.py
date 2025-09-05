import streamlit as st
from database.auth_new import render_auth_page
from core.session_handler import SessionManager
from ui.chat_interface import UIComponents
from models.ai_models import LLMClient



import os
from core.app_config import Config

def main():
    # Initialize session
    SessionManager.init_session()
    
    # Create necessary directories
    os.makedirs("./data", exist_ok=True)
    
    # Check authentication
    if not SessionManager.is_authenticated():
        render_auth_page()
        return
    

    
    # Main app
    render_main_app()

def render_main_app():
    st.set_page_config(
        page_title="AI Chatbot Pro",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Clean Professional Chat Page CSS
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        background-attachment: fixed;
        font-family: 'Inter', sans-serif;
        min-height: 100vh;
    }
    
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(255, 255, 255, 0.9);
        backdrop-filter: blur(10px);
        z-index: -1;
    }
    
    .main {
        padding: 1rem;
        max-width: 1000px;
        margin: 0 auto;
    }
    
    .stSidebar {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        border-right: 1px solid #E5E7EB;
    }
    
    .chat-header {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        border-radius: 16px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        text-align: center;
    }
    
    .stChatMessage {
        max-width: 70%;
        margin: 1rem 0;
        animation: slideIn 0.3s ease-out;
    }
    
    @keyframes slideIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* User messages - Right side */
    .stChatMessage[data-testid="chat-message-user"] {
        margin-left: auto;
        margin-right: 0;
    }
    
    .stChatMessage[data-testid="chat-message-user"] > div {
        background: linear-gradient(135deg, #4F46E5, #06B6D4);
        color: white;
        border-radius: 20px 20px 5px 20px;
        padding: 1rem 1.25rem;
        box-shadow: 0 4px 15px rgba(79, 70, 229, 0.3);
        text-align: right;
    }
    
    /* Assistant messages - Left side */
    .stChatMessage[data-testid="chat-message-assistant"] {
        margin-left: 0;
        margin-right: auto;
    }
    
    .stChatMessage[data-testid="chat-message-assistant"] > div {
        background: #F8FAFC;
        color: #1E293B;
        border-radius: 20px 20px 20px 5px;
        padding: 1rem 1.25rem;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        border: 1px solid #E5E7EB;
    }
    
    .stChatInput {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        border-top: 1px solid #E5E7EB;
        padding: 1rem;
        z-index: 1000;
    }
    
    .stChatInput > div {
        max-width: 1000px;
        margin: 0 auto;
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    [data-testid="stToolbar"] {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)
    
    # Get user info
    user_info = SessionManager.get_user_info()
    
    # Initialize components
    llm_client = LLMClient()
    
    # Sidebar
    UIComponents.render_sidebar(user_info)
    
    # Main chat area
    render_chat_interface(llm_client)
    
    # No navigation needed

def handle_file_upload(uploaded_file, rag_pipeline):
    """Handle file upload and processing"""
    file_info, message = FileLoader.process_file(uploaded_file)
    
    if file_info:
        # Simple duplicate check by filename
        existing_names = [f["name"] for f in st.session_state.uploaded_files]
        
        if file_info["name"] not in existing_names:
            st.session_state.uploaded_files.append(file_info)
            st.session_state.conversation_stats["files_uploaded"] += 1
            
            # Add to RAG pipeline
            if isinstance(file_info["content"], str):
                rag_pipeline.add_documents([file_info["content"]])
            
            st.success(f"✅ {message}")
        else:
            st.warning("⚠️ File already uploaded")
    else:
        st.error(f"❌ {message}")

def render_chat_interface(llm_client):
    """Clean Professional Chat Interface"""
    # Simple header
    st.markdown("""
    <div class='chat-header'>
        <div style='display: flex; align-items: center; justify-content: center; gap: 1rem;'>
            <div style='width: 60px; height: 60px; background: linear-gradient(135deg, #4F46E5, #06B6D4); border-radius: 15px; display: flex; align-items: center; justify-content: center; font-size: 2.5rem; box-shadow: 0 4px 15px rgba(79, 70, 229, 0.3);'>🤖</div>
            <div>
                <h1 style='margin: 0; color: #1E293B; font-size: 2.2rem; font-weight: 700;'>AI Chatbot Pro</h1>
                <p style='margin: 0; color: #64748B; font-size: 1rem;'>Intelligent AI Assistant - Multi-Model Support</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Chat messages container
    st.markdown("""
    <div style='height: 65vh; overflow-y: auto; padding: 1rem 0; margin-bottom: 10vh;'>
    """, unsafe_allow_html=True)
    
    # Display messages with proper alignment
    for message in st.session_state.messages:
        with st.chat_message(message["role"], avatar="👤" if message["role"] == "user" else "🤖"):
            st.markdown(message["content"])
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Chat input at bottom
    if prompt := st.chat_input("💬 Type your message here..."):
        from core.session_handler import SessionManager
        
        # Add user message
        SessionManager.add_message("user", prompt)
        
        # Show Gemini-style thinking animation
        thinking_placeholder = st.empty()
        with thinking_placeholder.container():
            with st.chat_message("assistant", avatar="🤖"):
                thinking_text = st.empty()
                import time
                
                # Animated thinking dots like Gemini
                for i in range(4):
                    dots = "." * ((i % 3) + 1)
                    thinking_text.markdown(f"🤖 **Thinking{dots}**")
                    time.sleep(0.4)
        
        # Generate AI response
        try:
            # Ensure model is properly set
            if 'selected_model' not in st.session_state:
                st.session_state.selected_model = 'grok'
            
            current_model = st.session_state.selected_model
            
            messages = [
                {"role": "system", "content": "You are a helpful AI assistant. Be friendly, informative and engaging."},
                {"role": "user", "content": prompt}
            ]
            
            # Get response from AI
            response = llm_client.generate_response(messages, current_model)
            
            # Clear thinking animation
            thinking_placeholder.empty()
            
            # Add assistant response
            SessionManager.add_message("assistant", response)
            st.rerun()
            
        except Exception as e:
            thinking_placeholder.empty()
            error_response = f"I'm having trouble connecting right now. Please try again! 😊\n\nError: {str(e)}"
            SessionManager.add_message("assistant", error_response)
            st.rerun()

def render_navigation():
    """Render navigation menu"""
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 🧭 Navigation")
    
    if st.sidebar.button("📊 Analytics", use_container_width=True):
        st.session_state.current_page = "analytics"
        st.rerun()
    
    if st.sidebar.button("💬 Chat", use_container_width=True):
        st.session_state.current_page = "chat"
        st.rerun()
    
    # Handle page navigation
    current_page = st.session_state.get("current_page", "chat")
    
    if current_page == "analytics":
        render_analytics_page()

def render_analytics_page():
    """Render analytics page"""
    st.empty()  # Clear main content
    Analytics.render_analytics_page()
    
    if st.button("← Back to Chat"):
        st.session_state.current_page = "chat"
        st.rerun()

if __name__ == "__main__":
    main()