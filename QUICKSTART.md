# 🚀 Quick Start - Campus AI Chatbot

## Instant Setup (3 Steps)

### 1. Install Dependencies
```powershell
pip install -r requirements.txt
```

### 2. Set Up Environment
```powershell
# Copy environment template
copy .env.example .env

# Edit .env and set:
# LLM_PROVIDER=ollama  (or huggingface, or leave as fallback)
```

### 3. Run the Application
```powershell
python app.py
```

**That's it!** 🎉

- **Main Chatbot**: http://localhost:5000
- **Admin Panel**: http://localhost:5000/admin

---

## FREE LLM Setup (Optional but Recommended)

### Option A: Ollama (100% FREE, Local)
```powershell
# 1. Download Ollama from https://ollama.ai
# 2. Install and run:
ollama serve

# 3. Download a model:
ollama pull llama2

# 4. In .env file, set:
# LLM_PROVIDER=ollama
```

### Option B: Hugging Face (FREE with API key)
```powershell
# 1. Get free API key from https://huggingface.co/settings/tokens
# 2. In .env file, set:
# LLM_PROVIDER=huggingface
# HUGGINGFACE_API_KEY=your_key_here
```

### Option C: No LLM (Works immediately)
```powershell
# Uses template responses - works without any setup!
# Just run: python app.py
```

---

## First Time Setup Checklist

### Admin Panel Configuration (http://localhost:5000/admin)

1. **Campus Information** (2 minutes)
   - [ ] Enter university name
   - [ ] Add contact email and phone
   - [ ] Set website URL

2. **Branding** (2 minutes)
   - [ ] Upload campus logo
   - [ ] Choose brand colors
   - [ ] Upload bot avatar (optional)

3. **Upload Documents** (5 minutes)
   - [ ] Upload Fee Structure PDF
   - [ ] Upload Exam Schedule PDF
   - [ ] Upload Hostel Handbook PDF
   - [ ] Upload Library Manual PDF

4. **Test the Bot** (2 minutes)
   - [ ] Go to main page
   - [ ] Ask: "What is the fee structure?"
   - [ ] Ask: "When are the exams?"
   - [ ] Check if bot uses uploaded documents

---

## Troubleshooting

### "pip install" fails?
```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Port 5000 already in use?
Edit `app.py`, line at bottom, change:
```python
socketio.run(app, port=5000)  # Change 5000 to 5001
```

### Ollama connection error?
```powershell
# Make sure Ollama is running:
ollama serve

# Check if model is downloaded:
ollama list

# If not, download:
ollama pull llama2
```

### PDF upload not working?
- Ensure PDF is not password-protected
- Check file size (must be < 16MB)
- Verify PDF contains text (not just images)

---

## Advanced: PowerShell Setup Script

Run automated setup:
```powershell
.\setup.ps1
```

This will:
- ✅ Check Python installation
- ✅ Create virtual environment
- ✅ Install all dependencies
- ✅ Create necessary directories
- ✅ Check for Ollama
- ✅ Offer to start the application

---

## What You Get

### For Students
- 💬 Natural language chat interface
- 🔍 Instant answers about fees, exams, hostel, library
- 📞 Automatic department contact information
- 📱 Mobile-friendly design

### For Administrators
- ⚙️ Easy customization panel
- 📤 Simple PDF upload system
- 📊 Usage statistics
- 🎨 Full branding control
- 💾 No coding required

---

## Need Help?

1. Read [README.md](README.md) for detailed documentation
2. Check [CUSTOMIZATION_GUIDE.md](CUSTOMIZATION_GUIDE.md) for branding
3. See [TESTING_GUIDE.md](TESTING_GUIDE.md) for sample questions

---

**Enjoy your new Campus AI Chatbot! 🎓✨**
