# 🎓 Campus AI Chatbot - Complete Project Documentation

## 📋 Project Overview

**Campus AI Chatbot** is a fully customizable, FREE AI-powered chatbot designed for university administration support. It integrates with university handbook PDFs to provide instant answers about:

- 💰 Fee structures and payment information
- 📝 Exam schedules and academic calendars
- 🏠 Hostel rules and accommodation details
- 📚 Library services and resources

### Key Features
✅ **100% FREE Options Available** (Ollama, Hugging Face)
✅ **No Coding Required** - User-friendly admin panel
✅ **Full Customization** - Logo, colors, branding
✅ **PDF Integration** - Upload handbooks directly
✅ **RAG Technology** - Accurate answers from documents
✅ **Mobile Responsive** - Works on all devices
✅ **Real-time Chat** - WebSocket support

---

## 🚀 Getting Started

### Installation (5 Minutes)

1. **Open PowerShell in project directory**
   ```powershell
   cd "c:\Users\shiva\OneDrive\Desktop\Vishwasri mam proj\campus-chatbot"
   ```

2. **Install Python packages**
   ```powershell
   pip install -r requirements.txt
   ```

3. **Configure environment**
   ```powershell
   copy .env.example .env
   notepad .env
   ```

4. **Choose your LLM provider** (in .env):
   - `LLM_PROVIDER=ollama` (FREE, local - recommended)
   - `LLM_PROVIDER=huggingface` (FREE with API key)
   - Leave blank for fallback mode (works immediately)

5. **Start the application**
   ```powershell
   python app.py
   ```

6. **Access the chatbot**
   - Main Interface: http://localhost:5000
   - Admin Panel: http://localhost:5000/admin

### OR Use Automated Setup

```powershell
.\setup.ps1
```

---

## 📚 Documentation

### For Administrators
- [QUICKSTART.md](QUICKSTART.md) - 5-minute setup guide
- [CUSTOMIZATION_GUIDE.md](CUSTOMIZATION_GUIDE.md) - Complete branding guide
- [README.md](README.md) - Full documentation

### For Developers
- [TESTING_GUIDE.md](TESTING_GUIDE.md) - Testing procedures
- [langflow_config.json](langflow_config.json) - LangFlow configuration

---

## 🎨 Customization Steps

### 1. Campus Information (Admin Panel → Customization)
```
✏️ University Name: "Stanford University"
✏️ Short Name: "Stanford"
✏️ Tagline: "The Wind of Freedom Blows"
✏️ Contact Email: info@stanford.edu
✏️ Contact Phone: +1-650-723-2300
✏️ Website: https://www.stanford.edu
```

### 2. Branding (Admin Panel → Customization)
```
🎨 Primary Color: #8C1515 (Stanford Cardinal)
🎨 Secondary Color: #007C89
🎨 Accent Color: #F9B800
📁 Upload Logo: campus_logo.png
📁 Upload Avatar: bot_avatar.png
📁 Upload Favicon: favicon.ico
```

### 3. Bot Settings (Admin Panel → Customization)
```
🤖 Bot Name: "Cardinal Helper"
💬 Welcome Message: 
"👋 Hello! I'm Cardinal Helper, your Stanford AI Assistant.

I can help you with:
💰 Fee Structure
📝 Exam Schedules
🏠 Housing Information
📚 Library Services

What would you like to know?"
```

### 4. Department Contacts (Edit config/campus_config.json)
```json
{
  "departments": {
    "fees": {
      "name": "Student Financial Services",
      "contact": "sfs@stanford.edu",
      "phone": "+1-650-723-3591",
      "location": "Old Union, 2nd Floor",
      "hours": "Mon-Fri: 9:00 AM - 5:00 PM"
    }
  }
}
```

### 5. Upload Documents (Admin Panel → Documents)
```
📄 Fee Structure → Upload: Fee_Handbook_2025.pdf
📄 Exam Schedule → Upload: Exam_Calendar_Fall2025.pdf
📄 Hostel Rules → Upload: Housing_Handbook.pdf
📄 Library Info → Upload: Library_Guide.pdf
```

---

## 🆓 FREE LLM Setup

### Option 1: Ollama (Recommended - 100% FREE)

**Advantages:**
- ✅ Completely free
- ✅ Runs locally (privacy)
- ✅ No API keys needed
- ✅ Good performance
- ✅ Multiple models available

**Setup:**
```powershell
# 1. Download from https://ollama.ai
# 2. Install Ollama
# 3. Open new terminal and run:
ollama serve

# 4. In another terminal:
ollama pull llama2  # or mistral, phi, gemma

# 5. In .env file:
LLM_PROVIDER=ollama
OLLAMA_MODEL=llama2
```

### Option 2: Hugging Face (FREE with limits)

**Advantages:**
- ✅ Free tier available
- ✅ Cloud-based (no local resources)
- ✅ Multiple models
- ✅ Easy setup

**Setup:**
```powershell
# 1. Go to https://huggingface.co/settings/tokens
# 2. Create free account
# 3. Generate API token
# 4. In .env file:
LLM_PROVIDER=huggingface
HUGGINGFACE_API_KEY=hf_your_token_here
```

### Option 3: Fallback Mode (No LLM)

**Advantages:**
- ✅ Works immediately
- ✅ No setup required
- ✅ Uses knowledge base only
- ✅ Good for testing

**Setup:**
```powershell
# Just run the application!
python app.py
# Bot will use template responses
```

---

## 📁 Project Structure

```
campus-chatbot/
│
├── 📄 app.py                    # Main Flask application
├── 📄 requirements.txt          # Python dependencies
├── 📄 .env.example             # Environment template
├── 📄 setup.ps1                # Automated setup script
│
├── 📂 config/
│   └── campus_config.json      # Campus settings (edit this!)
│
├── 📂 src/                     # Backend Python modules
│   ├── chatbot_engine.py       # Core chatbot logic
│   ├── llm_provider.py         # Multi-LLM support (Ollama, HF, etc)
│   ├── knowledge_base.py       # Vector database (ChromaDB)
│   ├── document_processor.py   # PDF processing
│   └── config_manager.py       # Configuration handler
│
├── 📂 templates/               # HTML templates
│   ├── index.html              # Main chat interface
│   └── admin.html              # Admin customization panel
│
├── 📂 static/                  # Frontend assets
│   ├── css/
│   │   ├── styles.css          # Main chat styles
│   │   └── admin.css           # Admin panel styles
│   └── js/
│       ├── chat.js             # Chat functionality
│       └── admin.js            # Admin functionality
│
├── 📂 assets/                  # Custom campus assets
│   └── README.txt              # Instructions for assets
│
├── 📂 documents/               # Uploaded PDF handbooks
│   └── (your PDFs go here)
│
├── 📂 data/                    # Knowledge base storage
│   ├── chroma_db/              # Vector database
│   └── feedback.jsonl          # User feedback
│
└── 📂 Documentation/
    ├── README.md               # Full documentation
    ├── QUICKSTART.md           # Quick setup guide
    ├── CUSTOMIZATION_GUIDE.md  # Branding guide
    └── TESTING_GUIDE.md        # Testing procedures
```

---

## 🔧 Configuration Files

### 1. Environment Variables (.env)
```env
# Flask Configuration
SECRET_KEY=your-secret-key-here

# LLM Provider (choose one)
LLM_PROVIDER=ollama           # Options: ollama, huggingface, ibm_granite, openai

# Ollama Configuration (FREE)
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama2

# Hugging Face (FREE)
HUGGINGFACE_API_KEY=your_key
HUGGINGFACE_MODEL=HuggingFaceH4/zephyr-7b-beta

# Features
ENABLE_VOICE=false
ENABLE_FEEDBACK=true
```

### 2. Campus Configuration (config/campus_config.json)
```json
{
  "campus_info": {
    "name": "Your University",
    "contact_email": "info@university.edu"
  },
  "branding": {
    "primary_color": "#1e3a8a",
    "logo_path": "assets/logo.png"
  },
  "chatbot_settings": {
    "bot_name": "CampusBot",
    "welcome_message": "Hello! How can I help?"
  }
}
```

---

## 📊 Features Breakdown

### User-Facing Features
- ✅ Natural language chat interface
- ✅ Quick action buttons
- ✅ Real-time typing indicators
- ✅ Message history
- ✅ Related questions suggestions
- ✅ Department contact info display
- ✅ Mobile responsive design
- ✅ Dark/light mode support

### Admin Features
- ✅ Campus information editor
- ✅ Branding customization
- ✅ PDF document upload
- ✅ Document management
- ✅ Usage statistics
- ✅ LLM provider configuration
- ✅ Department contact editor
- ✅ Quick links manager

### Technical Features
- ✅ RAG (Retrieval Augmented Generation)
- ✅ Vector similarity search (ChromaDB)
- ✅ PDF text extraction
- ✅ Table extraction from PDFs
- ✅ Smart text chunking
- ✅ Intent classification
- ✅ Session management
- ✅ Feedback collection
- ✅ WebSocket real-time chat
- ✅ REST API endpoints

---

## 🧪 Testing

### Quick Test Checklist

1. **Install & Run**
   - [ ] Dependencies installed
   - [ ] Application starts without errors
   - [ ] Ports are accessible

2. **Admin Panel**
   - [ ] Can access admin panel
   - [ ] Can update campus info
   - [ ] Can upload logo
   - [ ] Can change colors
   - [ ] Can upload PDFs

3. **Chatbot**
   - [ ] Chat interface loads
   - [ ] Can send messages
   - [ ] Bot responds
   - [ ] Quick actions work
   - [ ] Related actions appear

4. **Knowledge Base**
   - [ ] PDF uploads successfully
   - [ ] Bot uses PDF content in answers
   - [ ] Search returns relevant results

### Sample Test Questions
```
✅ "What is the fee structure?"
✅ "When are the semester exams?"
✅ "What are the hostel rules?"
✅ "What are the library timings?"
✅ "How do I contact the administration?"
```

---

## 🐛 Troubleshooting

### Common Issues

**1. Port 5000 already in use**
```powershell
# Kill process on port 5000
netstat -ano | findstr :5000
taskkill /PID <process_id> /F

# Or change port in app.py:
socketio.run(app, port=5001)
```

**2. Ollama connection failed**
```powershell
# Start Ollama service
ollama serve

# Check if model exists
ollama list

# Download model if missing
ollama pull llama2
```

**3. PDF upload not working**
```powershell
# Install PDF libraries
pip install pdfplumber PyPDF2 pypdf

# Check PDF:
# - Not password protected
# - Contains text (not scanned image)
# - Size < 16MB
```

**4. ChromaDB errors**
```powershell
# Reinstall ChromaDB
pip uninstall chromadb
pip install chromadb==0.4.18

# Clear database
rmdir /s data\chroma_db
```

**5. Module not found errors**
```powershell
# Reinstall all dependencies
pip install -r requirements.txt --upgrade
```

---

## 🚀 Deployment (Production)

### For Production Use

1. **Use Production Server**
   ```powershell
   pip install gunicorn
   gunicorn -w 4 -k eventlet -b 0.0.0.0:5000 app:app
   ```

2. **Environment Variables**
   - Set strong SECRET_KEY
   - Use environment-specific .env files
   - Never commit .env to version control

3. **HTTPS**
   - Use reverse proxy (nginx/Apache)
   - Enable SSL certificates
   - Force HTTPS redirects

4. **Database Backups**
   - Backup `data/` directory regularly
   - Backup `documents/` directory
   - Backup `config/` directory

5. **Monitoring**
   - Set up error logging
   - Monitor resource usage
   - Track API rate limits

---

## 📈 Performance Optimization

### For Better Performance

1. **Use GPU** (if available)
   ```powershell
   # Ollama automatically uses GPU if available
   # Significant speed improvement for responses
   ```

2. **Optimize PDFs**
   - Remove unnecessary pages
   - Keep files under 10MB
   - Use text-based PDFs (not scans)

3. **Cache Responses**
   - Enable caching for common queries
   - Store frequently accessed data

4. **Limit Concurrent Users**
   - Adjust worker count in Gunicorn
   - Use load balancing for high traffic

---

## 🤝 Support & Community

### Getting Help

1. **Documentation**
   - Read README.md
   - Check QUICKSTART.md
   - Review CUSTOMIZATION_GUIDE.md

2. **Troubleshooting**
   - Check error messages in terminal
   - Review browser console
   - Verify configuration files

3. **Community**
   - Report issues on GitHub
   - Share your customizations
   - Contribute improvements

---

## 📝 License

MIT License - Free to use for educational institutions

---

## 🎯 Next Steps

After setup:

1. **Customize Your Campus**
   - Update all campus information
   - Upload your logo and branding
   - Configure department contacts

2. **Add Knowledge**
   - Upload all relevant PDF handbooks
   - Test with sample questions
   - Refine responses

3. **Launch**
   - Train staff on admin panel
   - Announce to students
   - Collect feedback

4. **Maintain**
   - Update documents annually
   - Monitor usage statistics
   - Respond to user feedback

---

## 🌟 Success Metrics

Track these KPIs:

- ✅ Number of queries handled
- ✅ User satisfaction ratings
- ✅ Response accuracy
- ✅ Reduction in support tickets
- ✅ Student engagement

---

**🎓 Your Campus AI Chatbot is Ready!**

**Built with ❤️ for Educational Excellence**

---

## Quick Reference Commands

```powershell
# Start application
python app.py

# Install dependencies
pip install -r requirements.txt

# Setup Ollama
ollama serve
ollama pull llama2

# Run automated setup
.\setup.ps1

# Access URLs
# Main: http://localhost:5000
# Admin: http://localhost:5000/admin
```

---

**For questions, issues, or contributions, please refer to the documentation files in this project.**

**Happy Chatbotting! 🚀**
