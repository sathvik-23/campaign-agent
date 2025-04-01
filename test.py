import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env
load_dotenv()

# Get the API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("🚨 API Key not found! Please check your .env file.")

# Configure Gemini API
genai.configure(api_key=api_key)

# Test API connection
try:
    models = genai.list_models()
    for model in models:
        print(model.name)
except Exception as e:
    print(f"❌ Error: {e}")
