import streamlit as st
from datetime import datetime

class SessionManager:
    @staticmethod
    def init_session():
        if "authenticated" not in st.session_state:
            st.session_state.authenticated = False
        
        if "user" not in st.session_state:
            st.session_state.user = None
        
        if "messages" not in st.session_state:
            st.session_state.messages = []
        
        if "uploaded_files" not in st.session_state:
            st.session_state.uploaded_files = []
        
        if "selected_model" not in st.session_state:
            st.session_state.selected_model = "Gemini"
        

        
        if "conversation_stats" not in st.session_state:
            st.session_state.conversation_stats = {
                "total_messages": 0,
                "total_queries": 0,
                "files_uploaded": 0,
                "session_start": datetime.now()
            }
    
    @staticmethod
    def add_message(role, content):
        st.session_state.messages.append({
            "role": role,
            "content": content,
            "timestamp": datetime.now()
        })
        
        if role == "user":
            st.session_state.conversation_stats["total_queries"] += 1
        
        st.session_state.conversation_stats["total_messages"] += 1
    
    @staticmethod
    def clear_chat():
        st.session_state.messages = []
        st.session_state.conversation_stats["total_messages"] = 0
        st.session_state.conversation_stats["total_queries"] = 0
    
    @staticmethod
    def logout():
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
    
    @staticmethod
    def get_user_info():
        return st.session_state.get("user", {})
    
    @staticmethod
    def is_authenticated():
        return st.session_state.get("authenticated", False)