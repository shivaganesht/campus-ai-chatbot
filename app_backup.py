"""
Campus AI Chatbot - Main Application (Vercel Optimized)
========================================================
Serverless-ready Flask app for Vercel deployment
"""

import os
import json
from datetime import datetime
from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__, 
            static_folder='static',
            template_folder='templates')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'campus-chatbot-secret-key-change-me')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Enable CORS
CORS(app, resources={r"/*": {"origins": "*"}})

# Initialize managers (with error handling for Vercel)
config_manager = None
chatbot = None
doc_processor = None

def init_app():
    """Initialize app components (lazy loading for Vercel)"""
    global config_manager, chatbot, doc_processor
    
    if config_manager is None:
        try:
            from src.chatbot_engine import CampusChatbot
            from src.document_processor import DocumentProcessor
            from src.config_manager import ConfigManager
            
            config_manager = ConfigManager()
            chatbot = CampusChatbot(config_manager)
            doc_processor = DocumentProcessor(config_manager)
            
            print("✅ Campus AI Chatbot initialized")
        except Exception as e:
            print(f"⚠️ Initialization warning: {e}")
            # Create minimal fallback
            config_manager = type('obj', (object,), {
                'get_config': lambda: {},
                'get_value': lambda *args: 'Campus Chatbot'
            })()

# Initialize on first import
init_app()


# ==================== WEB ROUTES ====================

@app.route('/')
def index():
    """Main chatbot interface"""
    config = config_manager.get_public_config()
    return render_template('index.html', config=config)


@app.route('/admin')
def admin_panel():
    """Admin customization panel"""
    config = config_manager.get_public_config()
    return render_template('admin.html', config=config)


@app.route('/assets/<path:filename>')
def serve_assets(filename):
    """Serve custom campus assets"""
    return send_from_directory('assets', filename)


@app.route('/documents/<path:filename>')
def serve_documents(filename):
    """Serve uploaded PDF documents"""
    return send_from_directory('documents', filename)


# ==================== API ROUTES ====================

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'llm_provider': os.getenv('LLM_PROVIDER', 'ollama'),
        'version': '1.0.0'
    })


@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat messages"""
    try:
        data = request.json
        user_message = data.get('message', '').strip()
        session_id = data.get('session_id', 'default')
        
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400
        
        if len(user_message) > 500:
            return jsonify({'error': 'Message too long (max 500 characters)'}), 400
        
        response = chatbot.get_response(user_message, session_id)
        return jsonify(response)
        
    except Exception as e:
        print(f"Chat error: {e}")
        return jsonify({'error': str(e)}), 500


@app.route('/api/config', methods=['GET'])
def get_config():
    """Get public configuration"""
    return jsonify(config_manager.get_public_config())


@app.route('/api/config', methods=['POST'])
def update_config():
    """Update campus configuration"""
    try:
        data = request.json
        success = config_manager.update_config(data)
        
        if success:
            # Reload chatbot with new config
            global chatbot
            chatbot = CampusChatbot(config_manager)
            
            return jsonify({
                'status': 'success',
                'message': 'Configuration updated successfully'
            })
        
        return jsonify({
            'status': 'error',
            'message': 'Failed to update configuration'
        }), 500
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/upload-document', methods=['POST'])
def upload_document():
    """Upload and process PDF handbook"""
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file uploaded'}), 400
        
        file = request.files['file']
        category = request.form.get('category', 'general')
        
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not file.filename.lower().endswith('.pdf'):
            return jsonify({'error': 'Only PDF files are supported'}), 400
        
        result = doc_processor.process_document(file, category)
        return jsonify(result)
        
    except Exception as e:
        print(f"Upload error: {e}")
        return jsonify({'error': str(e)}), 500


@app.route('/api/upload-asset', methods=['POST'])
def upload_asset():
    """Upload campus branding assets"""
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file uploaded'}), 400
        
        file = request.files['file']
        asset_type = request.form.get('type', 'logo')
        
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        allowed_extensions = {'.png', '.jpg', '.jpeg', '.ico', '.svg', '.gif', '.webp'}
        file_ext = os.path.splitext(file.filename)[1].lower()
        
        if file_ext not in allowed_extensions:
            return jsonify({'error': f'Invalid file type. Allowed: {", ".join(allowed_extensions)}'}), 400
        
        # Save file
        filename = f"{asset_type}{file_ext}"
        filepath = os.path.join('assets', filename)
        os.makedirs('assets', exist_ok=True)
        file.save(filepath)
        
        # Update config
        config_manager.update_asset_path(asset_type, f'assets/{filename}')
        
        return jsonify({
            'status': 'success',
            'path': f'assets/{filename}',
            'message': f'{asset_type} uploaded successfully'
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/documents', methods=['GET'])
def list_documents():
    """List all uploaded documents"""
    try:
        documents = doc_processor.get_processed_documents()
        return jsonify({'documents': documents})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/documents/<filename>', methods=['DELETE'])
def delete_document(filename):
    """Delete a document"""
    try:
        success = doc_processor.delete_document(filename)
        if success:
            return jsonify({'status': 'success', 'message': 'Document deleted'})
        return jsonify({'error': 'Document not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/quick-actions', methods=['GET'])
def get_quick_actions():
    """Get quick action buttons"""
    actions = [
        {"id": "fees", "label": "💰 Fee Structure", "query": "What is the fee structure?", "icon": "💰"},
        {"id": "exams", "label": "📝 Exam Schedule", "query": "When are the exams?", "icon": "📝"},
        {"id": "hostel", "label": "🏠 Hostel Rules", "query": "What are the hostel rules?", "icon": "🏠"},
        {"id": "library", "label": "📚 Library Info", "query": "Tell me about library services", "icon": "📚"},
        {"id": "contact", "label": "📞 Contact", "query": "How to contact administration?", "icon": "📞"},
        {"id": "calendar", "label": "📅 Calendar", "query": "Show academic calendar", "icon": "📅"}
    ]
    return jsonify({'actions': actions})


@app.route('/api/feedback', methods=['POST'])
def submit_feedback():
    """Submit feedback for responses"""
    try:
        data = request.json
        message_id = data.get('message_id')
        rating = data.get('rating')
        comment = data.get('comment', '')
        
        chatbot.record_feedback(message_id, rating, comment)
        return jsonify({'status': 'success', 'message': 'Feedback recorded'})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get chatbot statistics"""
    try:
        stats = chatbot.get_statistics()
        kb_stats = chatbot.knowledge_base.get_statistics()
        
        return jsonify({
            'chatbot': stats,
            'knowledge_base': kb_stats,
            'documents': len(doc_processor.get_processed_documents())
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# ==================== HEALTH CHECK ====================

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint for Vercel"""
    return jsonify({
        'status': 'healthy',
        'llm_provider': os.getenv('LLM_PROVIDER', 'groq'),
        'timestamp': datetime.now().isoformat()
    })


# ==================== ERROR HANDLERS ====================

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404


@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500


# ==================== MAIN ====================

if __name__ == '__main__':
    # Create necessary directories
    os.makedirs('assets', exist_ok=True)
    os.makedirs('documents', exist_ok=True)
    os.makedirs('data', exist_ok=True)
    os.makedirs('config', exist_ok=True)
    
    # Check if LLM is available
    llm_provider = os.getenv('LLM_PROVIDER', 'groq')
    print(f"\n🚀 Starting server with {llm_provider.upper()} provider...")
    print("📝 Access the chatbot at: http://localhost:5000")
    print("⚙️  Admin panel at: http://localhost:5000/admin\n")
    
    # Run the application (standard Flask for local, works on Vercel)
    app.run(host='0.0.0.0', port=5000, debug=True)
