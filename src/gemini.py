# src/gemini.py
import os
import requests

def get_analysis(prompt):
    api_key = os.getenv("GEMINI_API_KEY")
    api_secret = os.getenv("GEMINI_API_SECRET")
    
    if not api_key or not api_secret:
        raise ValueError("Gemini API credentials are not set in the .env file")
    
    payload = {"prompt": prompt}
    
    # Replace with your actual Gemini API endpoint
    url = "https://api.gemini.example.com/analyze"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data.get("analysis", "No analysis available")
    else:
        raise Exception(f"Gemini API error: {response.status_code} - {response.text}")
