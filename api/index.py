"""
Minimal Flask app for Vercel - Test Version
"""
from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'status': 'working',
        'message': 'Campus AI Chatbot is running!',
        'env_check': {
            'LLM_PROVIDER': os.getenv('LLM_PROVIDER', 'not set'),
            'GROQ_API_KEY': 'set' if os.getenv('GROQ_API_KEY') else 'not set'
        }
    })

@app.route('/api/health')
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run()
