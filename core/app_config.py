import os

class Config:
    GROK_API_KEY = os.getenv("GROK_API_KEY")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    
    # Models
    AVAILABLE_MODELS = {
        "Grok": "grok-beta",
        "Gemini": "gemini-pro",
        "OpenAI": "gpt-3.5-turbo"
    }