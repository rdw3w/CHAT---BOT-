# 🤖 AI Chatbot Pro

A professional AI chatbot application with multi-model support, built with Streamlit.

## ✨ Features

- 🔐 **Secure Authentication** - Login/signup system with bcrypt password hashing
Signup page ---->>
<img width="500" height="422" alt="Screenshot 2025-09-05 091720" src="https://github.com/user-attachments/assets/ea9b58f1-2a5e-4b5e-b565-ef50c22f023c" />

Login Page----->>


<img width="522" height="407" alt="Screenshot 2025-09-05 091740" src="https://github.com/user-attachments/assets/fa513a88-ceae-4d2f-80ec-b2752984a909" />

- 🤖 **Multi-AI Support** - Choose from Grok, Gemini, or OpenAI models

- <img width="306" height="240" alt="Screenshot 2025-09-05 092000" src="https://github.com/user-attachments/assets/6da5e649-7ed0-4dab-8dee-02169a80304e" />

- 👤 **User Profiles** - Editable profiles with name, email, phone, and bio

- <img width="303" height="367" alt="Screenshot 2025-09-05 091939" src="https://github.com/user-attachments/assets/57503df6-a285-4604-aa3e-321678952be7" />

- 💬 **Modern Chat UI** - ChatGPT-style interface with thinking animations

- <img width="929" height="420" alt="Screenshot 2025-09-05 091908" src="https://github.com/user-attachments/assets/053a42bd-3fe8-44cf-92af-fd15e661e01a" />

- 🎨 **Some Demo Of chat Bot Pro** ----
- 
- 1.Question------>>>
- 
<img width="486" height="385" alt="Screenshot 2025-09-05 092227" src="https://github.com/user-attachments/assets/cc15acd0-618b-4137-b5d7-53ea8f22de72" />

<img width="349" height="337" alt="Screenshot 2025-09-05 092558" src="https://github.com/user-attachments/assets/464f1487-8a31-4a3c-8386-06162c3ce8f3" />

2.Simple Web Page---

<img width="413" height="407" alt="Screenshot 2025-09-05 092323" src="https://github.com/user-attachments/assets/f5d79516-54c7-41f3-af33-c18845394cdd" />

## 🚀 Quick Start


### Prerequisites
- Python 3.8+
- API keys for AI models

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd ai-chatbot-pro
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API keys:**
   Create a `.env` file and add your API keys:
   ```env
   GROK_API_KEY=your_grok_api_key_here
   GEMINI_API_KEY=your_gemini_api_key_here
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. **Run the application:**
   ```bash
   streamlit run app.py
   ```

## 📁 Project Structure

```
├── core/                   # Core functionality
│   ├── app_config.py      # Configuration management
│   └── session_handler.py # Session management
├── database/              # Authentication
│   └── auth_new.py        # Login/signup system
├── models/                # AI integrations
│   └── ai_models.py       # Grok, Gemini, OpenAI clients
├── ui/                    # User interface
│   └── chat_interface.py  # Chat UI components
├── utils/                 # Utilities
│   └── password_utils.py  # Password security
├── data/                  # CSV data storage (auto-created)
│   └── users.csv          # User data in CSV format
├── app.py                 # Main application
├── requirements.txt       # Dependencies
└── README.md              # Project documentation
```

## 🔧 Getting API Keys

- **Grok**: [X.AI Platform](https://x.ai/)
- **Gemini**: [Google AI Studio](https://makersuite.google.com/)
- **OpenAI**: [OpenAI Platform](https://platform.openai.com/)

## 💻 Usage

1. **Authentication** - Create account or login
2. **Select AI Model** - Choose from sidebar dropdown
3. **Start Chatting** - Type messages and get AI responses
4. **Profile Management** - Edit your profile in sidebar

## 🔒 Security

- Password hashing with bcrypt
- Secure session management
- Environment variables for API keys
- CSV data storage for user information

## 📦 Dependencies

- `streamlit` - Web framework
- `bcrypt` - Password hashing
- `pandas` - CSV data handling
- `openai` - OpenAI API
- `google-generativeai` - Gemini API
- `requests` - HTTP requests

## 🛠️ Troubleshooting

**API Errors:**
- Verify API keys in `.env` file
- Check internet connection
- Review API usage limits

**Login Issues:**
- Ensure password is at least 6 characters
- Check if database is created properly

## 📝 License

MIT License - see LICENSE file for details.

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

**Made with ❤️ using Streamlit and Python**
