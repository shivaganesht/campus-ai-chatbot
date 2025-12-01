"""
Campus AI Chatbot - Vercel Serverless Version
"""
from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import requests
import json

app = Flask(__name__)
CORS(app)

# Groq API configuration
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_MODEL = os.getenv('GROQ_MODEL', 'llama-3.1-8b-instant')

# System prompt for campus chatbot
SYSTEM_PROMPT = """You are a helpful campus administration assistant. You help students with:
- Fee structure and payment information
- Exam schedules and academic calendar
- Hostel rules and accommodation
- Library hours and availability
- General campus information

Provide clear, concise, and friendly responses. If you don't have specific information, suggest the student contact the relevant department."""

@app.route('/')
def home():
    return jsonify({
        'status': 'working',
        'message': 'Campus AI Chatbot is running!',
        'version': '1.0',
        'endpoints': ['/api/chat', '/api/health']
    })

@app.route('/api/health')
def health():
    return jsonify({'status': 'healthy', 'llm': 'groq-connected'})

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({'error': 'Message is required'}), 400
        
        if not GROQ_API_KEY:
            return jsonify({'error': 'Groq API key not configured'}), 500
        
        # Call Groq API
        headers = {
            'Authorization': f'Bearer {GROQ_API_KEY}',
            'Content-Type': 'application/json'
        }
        
        payload = {
            'model': GROQ_MODEL,
            'messages': [
                {'role': 'system', 'content': SYSTEM_PROMPT},
                {'role': 'user', 'content': user_message}
            ],
            'temperature': 0.7,
            'max_tokens': 500
        }
        
        response = requests.post(GROQ_API_URL, headers=headers, json=payload, timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            bot_response = result['choices'][0]['message']['content']
            return jsonify({
                'response': bot_response,
                'model': GROQ_MODEL,
                'status': 'success'
            })
        else:
            return jsonify({
                'error': 'Failed to get response from LLM',
                'details': response.text
            }), response.status_code
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run()
