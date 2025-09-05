import pandas as pd
import streamlit as st
import os
from datetime import datetime

from utils.password_utils import hash_password, verify_password

class AuthManager:
    def __init__(self):
        self.csv_path = "./data/users.csv"
        self.init_csv()
    
    def init_csv(self):
        os.makedirs("./data", exist_ok=True)
        if not os.path.exists(self.csv_path):
            df = pd.DataFrame(columns=['id', 'name', 'phone', 'email', 'password_hash', 'created_at'])
            df.to_csv(self.csv_path, index=False)
    
    def register_user(self, name, phone, email, password):
        try:
            df = pd.read_csv(self.csv_path)
            
            if email in df['email'].values:
                return False, "Email already exists"
            
            password_hash = hash_password(password)
            new_id = len(df) + 1
            new_user = {
                'id': new_id,
                'name': name,
                'phone': phone,
                'email': email,
                'password_hash': password_hash,
                'created_at': datetime.now().isoformat()
            }
            
            df = pd.concat([df, pd.DataFrame([new_user])], ignore_index=True)
            df.to_csv(self.csv_path, index=False)
            return True, "User registered successfully"
        except Exception as e:
            return False, f"Registration failed: {str(e)}"
    
    def authenticate_user(self, email, password):
        try:
            df = pd.read_csv(self.csv_path)
            user_row = df[df['email'] == email]
            
            if not user_row.empty and verify_password(password, user_row.iloc[0]['password_hash']):
                user = user_row.iloc[0]
                return True, {
                    "id": int(user['id']),
                    "name": user['name'],
                    "phone": user['phone'],
                    "email": user['email']
                }
            return False, "Invalid credentials"
        except Exception as e:
            return False, f"Authentication failed: {str(e)}"
    


def render_auth_page():
    st.set_page_config(
        page_title="AI Chatbot Pro - Login",
        page_icon="🤖",
        layout="wide"
    )
    
    # Professional login page with glassmorphism
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #4F46E5 0%, #06B6D4 100%);
        background-attachment: fixed;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        min-height: 100vh;
    }
    
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(135deg, rgba(79, 70, 229, 0.8) 0%, rgba(6, 182, 212, 0.8) 100%);
        backdrop-filter: blur(10px);
        z-index: -1;
    }
    
    .main {
        background: transparent;
        padding: 0;
        display: flex;
        align-items: center;
        justify-content: center;
        min-height: 100vh;
    }
    
    .block-container {
        padding: 2rem 1rem;
        max-width: 100%;
        margin: 0;
    }
    
    .login-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(20px);
        border-radius: 24px;
        box-shadow: 0 25px 50px rgba(0,0,0,0.2);
        padding: 3rem 2.5rem;
        max-width: 450px;
        width: 100%;
        border: 1px solid rgba(255,255,255,0.2);
        animation: fadeSlideIn 0.8s ease-out;
        margin: 0 auto;
    }
    
    @keyframes fadeSlideIn {
        from {
            opacity: 0;
            transform: translateY(40px) scale(0.95);
        }
        to {
            opacity: 1;
            transform: translateY(0) scale(1);
        }
    }
    
    .logo-container {
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .app-logo {
        width: 120px;
        height: 120px;
        background: rgba(255, 255, 255, 0.2);
        border-radius: 24px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 1.5rem;
        font-size: 3rem;
        box-shadow: 0 15px 35px rgba(0,0,0,0.1);
        border: 1px solid rgba(255,255,255,0.3);
    }
    
    .welcome-title {
        font-size: 2.2rem;
        font-weight: 700;
        color: white;
        margin: 0 0 0.5rem 0;
        text-align: center;
        text-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    
    .welcome-subtitle {
        color: rgba(255, 255, 255, 0.8);
        font-size: 1.1rem;
        margin: 0 0 2rem 0;
        text-align: center;
        font-weight: 400;
    }
    
    .stTextInput > div > div > input {
        border: 1px solid rgba(255, 255, 255, 0.3);
        border-radius: 12px;
        padding: 1rem;
        font-size: 1rem;
        font-weight: 400;
        transition: all 0.3s ease;
        background: rgba(255, 255, 255, 0.1);
        color: white;
        backdrop-filter: blur(10px);
    }
    
    .stTextInput > div > div > input::placeholder {
        color: rgba(255, 255, 255, 0.6);
    }
    
    .stTextInput > div > div > input:focus {
        border-color: rgba(255, 255, 255, 0.6);
        box-shadow: 0 0 0 3px rgba(255, 255, 255, 0.1);
        background: rgba(255, 255, 255, 0.15);
        outline: none;
    }
    
    .stTextInput label {
        color: white;
        font-weight: 500;
        font-size: 0.95rem;
        margin-bottom: 0.5rem;
    }
    
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #4F46E5, #06B6D4);
        color: white;
        border: none;
        padding: 1rem;
        border-radius: 12px;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(79, 70, 229, 0.3);
        cursor: pointer;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(79, 70, 229, 0.4);
        background: linear-gradient(135deg, #5B52E8, #07C7DB);
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 0.5rem;
        justify-content: center;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 0.5rem;
        margin-bottom: 2rem;
        backdrop-filter: blur(10px);
    }
    
    .stTabs [data-baseweb="tab"] {
        background: transparent;
        border-radius: 8px;
        padding: 0.75rem 1.5rem;
        font-weight: 500;
        color: rgba(255, 255, 255, 0.7);
        transition: all 0.3s ease;
    }
    
    .stTabs [aria-selected="true"] {
        background: rgba(255, 255, 255, 0.2);
        color: white;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    
    .stAlert {
        border-radius: 12px;
        border: none;
        font-weight: 500;
        margin: 1rem 0;
        backdrop-filter: blur(10px);
    }
    
    .stSuccess {
        background: rgba(16, 185, 129, 0.2);
        color: #10B981;
        border: 1px solid rgba(16, 185, 129, 0.3);
    }
    
    .stError {
        background: rgba(239, 68, 68, 0.2);
        color: #EF4444;
        border: 1px solid rgba(239, 68, 68, 0.3);
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {visibility: hidden;}
    [data-testid="stToolbar"] {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)
    
    auth_manager = AuthManager()
    
    # Centered login card
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<div class="login-card">', unsafe_allow_html=True)
        
        # Professional logo and welcome message
        st.markdown("""
        <div class="logo-container">
            <div class="app-logo">🤖</div>
            <h1 class="welcome-title">Welcome to Your AI Chatbot</h1>
            <p class="welcome-subtitle">Sign in to continue your conversation</p>
        </div>
        """, unsafe_allow_html=True)
        
        tab1, tab2 = st.tabs(["Login", "Sign Up"])
        
        with tab1:
            with st.form("login_form"):
                email = st.text_input("Email Address", placeholder="Enter your email")
                password = st.text_input("Password", type="password", placeholder="Enter your password")
                login_btn = st.form_submit_button("🔑 Sign In")
                
                if login_btn:
                    if email and password:
                        if len(password) >= 6:
                            success, result = auth_manager.authenticate_user(email, password)
                            if success:
                                st.session_state.authenticated = True
                                st.session_state.user = result
                                st.success("✅ Login successful! Redirecting...")
                                st.rerun()
                            else:
                                st.error(f"❌ {result}")
                        else:
                            st.error("❌ Password must be at least 6 characters")
                    else:
                        st.error("❌ Please fill all fields")
        
        with tab2:
            with st.form("signup_form"):
                name = st.text_input("Full Name", placeholder="Enter your full name")
                phone = st.text_input("Phone Number", placeholder="Enter your phone number")
                email = st.text_input("Email Address", placeholder="Enter your email")
                password = st.text_input("Password", type="password", placeholder="Create a password (min 6 chars)")
                confirm_password = st.text_input("Confirm Password", type="password", placeholder="Confirm your password")
                signup_btn = st.form_submit_button("🎆 Create Account")
                
                if signup_btn:
                    if all([name, phone, email, password, confirm_password]):
                        if "@" in email and "." in email:
                            if len(password) >= 6:
                                if password == confirm_password:
                                    success, message = auth_manager.register_user(name, phone, email, password)
                                    if success:
                                        st.success(f"✅ {message}")
                                        st.info("🔄 Please switch to Login tab to sign in")
                                    else:
                                        st.error(f"❌ {message}")
                                else:
                                    st.error("❌ Passwords don't match")
                            else:
                                st.error("❌ Password must be at least 6 characters")
                        else:
                            st.error("❌ Please enter a valid email address")
                    else:
                        st.error("❌ Please fill all fields")
        
        st.markdown('</div>', unsafe_allow_html=True)