import requests
import openai
import google.generativeai as genai
from core.app_config import Config

class LLMClient:
    def __init__(self):
        self.config = Config()
        self.setup_clients()
    
    def setup_clients(self):
        # Gemini
        if self.config.GEMINI_API_KEY:
            genai.configure(api_key=self.config.GEMINI_API_KEY)
    
    def call_grok(self, messages, model="grok-4-latest"):
        if not self.config.GROK_API_KEY:
            return "Grok API key not configured"
        
        try:
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.config.GROK_API_KEY}"
            }
            
            data = {
                "messages": messages,
                "model": model,
                "stream": False,
                "temperature": 0.7
            }
            
            response = requests.post(
                "https://api.x.ai/v1/chat/completions",
                headers=headers,
                json=data
            )
            
            if response.status_code == 200:
                return response.json()["choices"][0]["message"]["content"]
            else:
                return f"Grok API error: {response.status_code}"
        except Exception as e:
            return f"Grok error: {str(e)}"
    
    def call_gemini(self, messages, model="gemini-2.0-flash"):
        if not self.config.GEMINI_API_KEY:
            return "Gemini API key not configured"
        
        try:
            # Convert messages to Gemini format
            prompt = ""
            for msg in messages:
                if msg["role"] == "system":
                    prompt += f"System: {msg['content']}\n"
                elif msg["role"] == "user":
                    prompt += f"User: {msg['content']}\n"
                elif msg["role"] == "assistant":
                    prompt += f"Assistant: {msg['content']}\n"
            
            model_instance = genai.GenerativeModel(model)
            response = model_instance.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Gemini error: {str(e)}"
    
    def call_openai(self, messages, model="gpt-3.5-turbo"):
        if not self.config.OPENAI_API_KEY:
            return "OpenAI API key not configured. Please add your API key to the .env file."
        
        try:
            client = openai.OpenAI(api_key=self.config.OPENAI_API_KEY)
            response = client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=0.7,
                max_tokens=1000
            )
            return response.choices[0].message.content
        except openai.AuthenticationError:
            return "OpenAI API key is invalid. Please check your API key in the .env file."
        except openai.RateLimitError:
            return "OpenAI rate limit exceeded. Please try again later."
        except openai.APIError as e:
            return f"OpenAI API error: {str(e)}"
        except Exception as e:
            return f"OpenAI connection error: {str(e)}"
    
    def call_local_model(self, messages):
        # Placeholder for local model integration
        return "Local model not implemented yet. Please use cloud models."
    
    def generate_response(self, messages, model_name):
        # Normalize model name to lowercase
        model_name = str(model_name).lower().strip()
        
        if model_name == "grok":
            return self.call_grok(messages)
        elif model_name == "gemini":
            return self.call_gemini(messages)
        elif model_name == "openai":
            return self.call_openai(messages)
        elif model_name == "local":
            return self.call_local_model(messages)
        else:
            # Default to grok if unknown model
            return self.call_grok(messages)