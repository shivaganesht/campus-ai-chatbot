#!/usr/bin/env python
"""Test Groq API connection"""

import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_groq():
    print("\n🔧 Testing Groq API Connection...")
    print("=" * 50)
    
    api_key = os.getenv('GROQ_API_KEY')
    model = os.getenv('GROQ_MODEL', 'llama-3.1-8b-instant')
    
    if not api_key:
        print("❌ ERROR: GROQ_API_KEY not found in .env file")
        return False
    
    print(f"✅ API Key loaded: {api_key[:20]}...")
    print(f"✅ Model: {model}")
    print("\n📡 Sending test request to Groq API...")
    
    try:
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": model,
            "messages": [
                {"role": "user", "content": "Say 'Hello from Campus AI Chatbot!' in a friendly way."}
            ],
            "max_tokens": 50,
            "temperature": 0.7
        }
        
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=30
        )
        
        print(f"📊 Status Code: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            message = result['choices'][0]['message']['content']
            print("\n✅ SUCCESS! Groq API is working!")
            print("=" * 50)
            print("🤖 Bot Response:")
            print(message)
            print("=" * 50)
            print("\n🎉 Your chatbot is ready to deploy!")
            print("📝 Next steps:")
            print("   1. Run: python app.py")
            print("   2. Visit: http://localhost:5000")
            print("   3. Or deploy to Vercel!")
            return True
        else:
            print(f"\n❌ ERROR: API returned status {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"\n❌ ERROR: Failed to connect to Groq API")
        print(f"Details: {str(e)}")
        return False
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        return False

if __name__ == "__main__":
    success = test_groq()
    exit(0 if success else 1)
