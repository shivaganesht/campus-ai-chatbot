# 🎓 Campus AI Chatbot

An intelligent AI chatbot for campus administration support with PDF handbook integration. Built with **FREE** cloud-based LLMs and ready for **Vercel deployment**!

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Flask](https://img.shields.io/badge/Flask-3.0-green)
![Vercel](https://img.shields.io/badge/Deploy-Vercel-black)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🌐 Deploy to Vercel (FREE)

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new)

**100% FREE deployment with cloud-based LLM!** See [VERCEL_DEPLOYMENT.md](VERCEL_DEPLOYMENT.md) for complete guide.

## ✨ Features

### 🤖 Intelligent Chatbot
- **FREE Cloud LLMs**: Groq (30 req/min, recommended), Hugging Face Inference API, Together AI ($25 credit)
- **Works on Vercel**: All LLM options are serverless-ready
- **PDF Knowledge Base**: Upload university handbooks and train the bot
- **RAG (Retrieval Augmented Generation)**: Accurate answers from your documents
- **Real-time Chat**: WebSocket support for instant responses
- **Multi-category Support**: Fees, Exams, Hostel, Library, General queries

### 🎨 Full Customization
- **Campus Branding**: Upload logo, colors, favicon
- **Bot Personality**: Customize bot name, avatar, messages
- **Department Info**: Add contact details for all departments
- **Quick Links**: Configure portal links and resources
- **No Code Required**: User-friendly admin panel

### 📄 Document Processing
- **PDF Upload**: Drag and drop university handbooks
- **Auto-categorization**: Automatically sorts content by topic
- **Smart Chunking**: Intelligent text splitting for better retrieval
- **Table Extraction**: Handles fee structures and schedules

### 📊 Analytics
- Track user interactions
- Monitor chatbot performance
- View knowledge base statistics
- Real-time health monitoring

## 🚀 Quick Start

### Prerequisites

**For Local Development:**
- Python 3.9 or higher
- pip (Python package manager)

**For Vercel Deployment (Recommended):**
- GitHub account
- Vercel account (FREE)
- FREE LLM API key (Groq recommended)

### Option 1: Deploy to Vercel (RECOMMENDED) 🚀

**Complete guide:** [VERCEL_DEPLOYMENT.md](VERCEL_DEPLOYMENT.md)

**Quick steps:**
1. Get FREE Groq API key: https://console.groq.com (2 minutes)
2. Push code to GitHub
3. Import to Vercel
4. Add environment variables
5. Deploy! (Your chatbot is live at `https://your-app.vercel.app`)

**Why Vercel?**
- ✅ 100% FREE hosting
- ✅ Auto-scaling
- ✅ HTTPS included
- ✅ Global CDN
- ✅ Zero configuration

### Option 2: Local Installation

1. **Clone or Download the Project**
```powershell
cd "c:\Users\shiva\OneDrive\Desktop\Vishwasri mam proj\campus-chatbot"
```

2. **Install Dependencies**
```powershell
pip install -r requirements.txt
```

3. **Configure Environment**
```powershell
copy .env.example .env
notepad .env
```

4. **Get FREE LLM API Key** (see [FREE_LLM_SETUP.md](FREE_LLM_SETUP.md))

**Option A: Groq (Recommended - FREE, works on Vercel)**
```powershell
# Get FREE key from https://console.groq.com
# In .env, set:
# LLM_PROVIDER=groq
# GROQ_API_KEY=gsk_your_key_here
```

**Option B: Hugging Face Inference API (FREE, works on Vercel)**
```powershell
# Get FREE token from https://huggingface.co/settings/tokens
# In .env, set:
# LLM_PROVIDER=huggingface_api
# HUGGINGFACE_API_KEY=hf_your_token_here
```

**Option C: Ollama (FREE but LOCAL ONLY - doesn't work on Vercel)**
```powershell
# Download from https://ollama.ai
ollama serve
ollama pull llama2
# In .env, set: LLM_PROVIDER=ollama
```

5. **Run the Application**
```powershell
python app.py
```

6. **Access the Chatbot**
- Main Interface: http://localhost:5000
- Admin Panel: http://localhost:5000/admin

## 📖 User Guide

### For Campus Administrators

#### 1. Initial Setup (Admin Panel)

**Step 1: Campus Information**
1. Go to http://localhost:5000/admin
2. Click "🎨 Customization" tab
3. Fill in campus details:
   - University name
   - Contact information
   - Department details
   - Social media links

**Step 2: Branding**
1. Upload campus logo (PNG, JPG, SVG)
2. Upload bot avatar image
3. Choose brand colors (primary, secondary, accent)
4. Upload favicon for browser tab

**Step 3: Upload Documents**
1. Click "📄 Documents" tab
2. Select category (Fees, Exams, Hostel, Library)
3. Upload PDF handbook
4. System automatically processes and extracts knowledge

**Step 4: Test the Bot**
1. Go back to main page
2. Try asking questions:
   - "What is the fee structure?"
   - "When are the exams?"
   - "What are the hostel rules?"
   - "Library timings?"

### For Students/Users

#### Using the Chatbot

1. **Quick Actions**: Click pre-defined questions in sidebar
2. **Type Questions**: Ask in natural language
3. **Related Actions**: Bot suggests follow-up questions
4. **Department Contact**: Get contact info automatically

#### Example Questions
```
- What is the fee structure for first year?
- When are the semester exams?
- What are the hostel check-in rules?
- Is the library open on weekends?
- How do I apply for a scholarship?
- What is the refund policy?
```

## 🔧 Configuration

### Campus Configuration (`config/campus_config.json`)

```json
{
  "campus_info": {
    "name": "Your University Name",
    "short_name": "YUN",
    "tagline": "Excellence in Education",
    "website": "https://www.youruniversity.edu",
    "contact_email": "info@youruniversity.edu",
    "contact_phone": "+1-XXX-XXX-XXXX"
  },
  "branding": {
    "primary_color": "#1e3a8a",
    "secondary_color": "#3b82f6",
    "accent_color": "#f59e0b"
  },
  "chatbot_settings": {
    "bot_name": "CampusBot",
    "welcome_message": "👋 Hello! I'm your Campus AI Assistant..."
  }
}
```

### Environment Variables (`.env`)

```env
# Flask
SECRET_KEY=your-secret-key-here

# LLM Provider (choose one)
LLM_PROVIDER=ollama  # Options: ollama, huggingface, ibm_granite, openai

# Ollama (FREE - Local)
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama2

# Hugging Face (FREE with limits)
HUGGINGFACE_API_KEY=your_key_here

# IBM Granite (Paid)
IBM_GRANITE_API_KEY=your_key_here
IBM_PROJECT_ID=your_project_id

# OpenAI (Paid)
OPENAI_API_KEY=your_key_here
```

## 🆓 FREE LLM Options Comparison

| Provider | Cost | Setup Difficulty | Performance | Best For |
|----------|------|------------------|-------------|----------|
| **Ollama** | FREE | Easy | Good | Production use, privacy |
| **Hugging Face** | FREE | Very Easy | Good | Testing, low traffic |
| **Fallback Mode** | FREE | None | Basic | Demo, no LLM setup |
| IBM Granite | Paid | Medium | Excellent | Enterprise |
| OpenAI | Paid | Easy | Excellent | High quality responses |

## 📁 Project Structure

```
campus-chatbot/
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── .env.example               # Environment template
├── config/
│   └── campus_config.json     # Campus customization
├── src/
│   ├── chatbot_engine.py      # Core chatbot logic
│   ├── llm_provider.py        # Multi-LLM support
│   ├── knowledge_base.py      # Vector database
│   ├── document_processor.py  # PDF processing
│   └── config_manager.py      # Configuration handler
├── templates/
│   ├── index.html             # Chat interface
│   └── admin.html             # Admin panel
├── static/
│   ├── css/
│   │   ├── styles.css         # Main styles
│   │   └── admin.css          # Admin styles
│   └── js/
│       ├── chat.js            # Chat functionality
│       └── admin.js           # Admin functionality
├── assets/                    # Custom campus assets
├── documents/                 # Uploaded PDF handbooks
└── data/                      # Knowledge base storage
```

## 🎯 Supported Document Types

### Fee Structure PDFs
- Tuition fee breakdown
- Payment schedules
- Scholarship information
- Refund policies

### Exam Schedule PDFs
- Semester timetables
- Exam dates and timings
- Assessment schedules
- Result announcements

### Hostel Handbooks
- Rules and regulations
- Room allocation procedures
- Mess menu and timings
- Visitor policies

### Library Handbooks
- Operating hours
- Borrowing procedures
- Fine structures
- E-resource access

## 🔒 Security & Privacy

- **Local Processing**: All data stays on your server
- **No Data Sharing**: Documents never leave your infrastructure
- **Ollama Option**: 100% local AI, no external API calls
- **Configurable**: Control what information is shared

## 🛠️ Troubleshooting

### Ollama Not Working
```powershell
# Check if Ollama is running
ollama list

# Start Ollama service
ollama serve

# Pull a model if not available
ollama pull llama2
```

### PDF Not Processing
- Ensure PDF is not password-protected
- Check file size (max 16MB)
- Verify PDF contains extractable text (not scanned images)

### Port Already in Use
```powershell
# Change port in app.py (line: socketio.run(app, port=5000))
# Or kill process on port 5000
netstat -ano | findstr :5000
taskkill /PID <process_id> /F
```

### ChromaDB Errors
```powershell
# Reinstall ChromaDB
pip uninstall chromadb
pip install chromadb==0.4.18
```

## 🚀 Deployment

### Production Considerations

1. **Use Production WSGI Server**
```powershell
pip install gunicorn
gunicorn -w 4 -k eventlet -b 0.0.0.0:5000 app:app
```

2. **Set Up Reverse Proxy** (nginx/Apache)

3. **Enable HTTPS**

4. **Regular Backups**
- Backup `data/` directory (knowledge base)
- Backup `documents/` directory (PDFs)
- Backup `config/` directory (settings)

5. **Monitor Resources**
- LLM models can be memory-intensive
- Consider dedicated GPU for better performance

## 📊 Performance Tips

1. **Use Ollama with GPU**: 10x faster responses
2. **Limit PDF Size**: Keep under 10MB for faster processing
3. **Clean Text**: Remove unnecessary pages before upload
4. **Cache Responses**: Configure caching for common queries

## 🤝 Contributing

This is an open-source project. Contributions welcome!

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

MIT License - Feel free to use for your campus!

## 💡 Support

For questions or issues:
1. Check the troubleshooting section
2. Review configuration files
3. Check logs in terminal
4. Open an issue on GitHub

## 🎉 Acknowledgments

- Built with Flask, LangChain, and ChromaDB
- Supports Ollama, Hugging Face, IBM Granite, OpenAI
- Designed for educational institutions

---

**Made with ❤️ for Campus Administration**

**Start making your campus smarter today! 🚀**
