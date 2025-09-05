import streamlit as st

class UIComponents:
    @staticmethod
    def render_sidebar(user_info):
        """Clean sidebar with user profile and controls"""
        with st.sidebar:
            # User Profile Section
            st.markdown("### 👤 Profile")
            
            # Simple Profile Section
            if 'user_profile' not in st.session_state:
                st.session_state.user_profile = {'bio': 'AI Enthusiast'}
            
            # Fixed Default Avatar (No Upload Option)
            st.markdown("""
            <div style='text-align: center; margin-bottom: 1rem;'>
                <div style='width: 90px; height: 90px; background: linear-gradient(135deg, #4F46E5, #06B6D4); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto; font-size: 2.5rem; color: white; box-shadow: 0 4px 15px rgba(79, 70, 229, 0.3); border: 3px solid white;'>
                    👤
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Enhanced User Info Display
            st.markdown(f"""
            <div style='background: rgba(255,255,255,0.1); padding: 1rem; border-radius: 12px; margin: 1rem 0;'>
                <h4 style='margin: 0 0 0.5rem 0; color: #1E293B;'>👤 {user_info.get('name', 'User')}</h4>
                <p style='margin: 0; color: #64748B; font-size: 0.9rem;'>📧 {user_info.get('email', 'N/A')}</p>
                <p style='margin: 0; color: #64748B; font-size: 0.9rem;'>📱 {user_info.get('phone', 'N/A')}</p>
                <p style='margin: 0.5rem 0 0 0; color: #64748B; font-size: 0.8rem; font-style: italic;'>{st.session_state.user_profile.get('bio', 'AI Enthusiast')}</p>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("✏️ Edit Profile", use_container_width=True):
                st.session_state.edit_profile = True
                st.rerun()
            
            # Edit profile form in expander
            if st.session_state.get('edit_profile', False):
                with st.expander("✏️ Edit Profile", expanded=True):
                    with st.form("edit_profile_form"):
                        new_name = st.text_input("👤 Full Name", value=user_info.get('name', ''), placeholder="Enter your name")
                        new_email = st.text_input("📧 Email Address", value=user_info.get('email', ''), placeholder="Enter your email")
                        new_phone = st.text_input("📱 Phone Number", value=user_info.get('phone', ''), placeholder="Enter your phone")
                        new_bio = st.text_area("📝 Bio", value=st.session_state.user_profile.get('bio', 'AI Enthusiast'), placeholder="Tell us about yourself", max_chars=100)
                        
                        col1, col2 = st.columns(2)
                        with col1:
                            if st.form_submit_button("💾 Save Changes", use_container_width=True):
                                if new_name and new_email:
                                    st.session_state.user.update({
                                        'name': new_name,
                                        'email': new_email,
                                        'phone': new_phone
                                    })
                                    st.session_state.user_profile['bio'] = new_bio
                                    st.session_state.edit_profile = False
                                    st.success("✅ Profile updated successfully!")
                                    st.rerun()
                                else:
                                    st.error("❌ Name and email are required")
                        with col2:
                            if st.form_submit_button("❌ Cancel", use_container_width=True):
                                st.session_state.edit_profile = False
                                st.rerun()
            
            st.divider()
            
            # AI Model Selection
            st.markdown("### 🤖 AI Model")
            
            # Initialize model if not set
            if 'selected_model' not in st.session_state:
                st.session_state.selected_model = 'grok'
            
            model_options = ["grok", "gemini", "openai"]
            model_labels = ["🚀 Grok", "💎 Gemini", "🧠 OpenAI"]
            
            current_model = st.session_state.selected_model
            
            # Ensure current model is valid
            if current_model not in model_options:
                current_model = 'grok'
                st.session_state.selected_model = current_model
            
            selected_index = st.selectbox(
                "Choose AI Model",
                range(len(model_options)),
                index=model_options.index(current_model),
                format_func=lambda x: model_labels[x],
                key="model_selector"
            )
            
            selected_model = model_options[selected_index]
            
            if selected_model != current_model:
                st.session_state.selected_model = selected_model
                st.success(f"✅ Switched to {model_labels[selected_index]}")
                st.rerun()
            
            st.divider()
            
            # Actions
            st.markdown("### ⚙️ Actions")
            
            if st.button("🗑️ Clear Chat", use_container_width=True):
                from core.session_handler import SessionManager
                SessionManager.clear_chat()
                st.success("✅ Chat cleared!")
                st.rerun()
            
            if st.button("🚪 Logout", use_container_width=True):
                from core.session_handler import SessionManager
                SessionManager.logout()
                st.rerun()