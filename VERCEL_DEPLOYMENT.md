# 🚀 Vercel Deployment Guide

## Complete Guide to Deploy Campus AI Chatbot on Vercel (FREE)

---

## 🎯 Overview

This guide shows you how to deploy your Campus AI Chatbot to **Vercel** for FREE with cloud-based LLM providers that work on serverless platforms.

### ✅ What Works on Vercel
- **Groq API** (100% FREE, 30 req/min, very fast) ⭐ **RECOMMENDED**
- **Hugging Face Inference API** (FREE with rate limits)
- **Together AI** ($25 FREE credit on signup)
- All PDF processing and knowledge base features
- Full admin panel and customization

### ❌ What Doesn't Work on Vercel
- **Ollama** (requires local server, can't run on serverless)
- **Local Hugging Face models** (too large for serverless)
- Any local LLM that needs persistent processes

---

## 📋 Prerequisites

1. **GitHub Account** (free)
2. **Vercel Account** (free - signup at https://vercel.com)
3. **FREE LLM API Key** - Choose ONE:
   - **Groq** (Recommended): https://console.groq.com
   - **Hugging Face**: https://huggingface.co/settings/tokens
   - **Together AI**: https://api.together.xyz

---

## 🔑 Step 1: Get FREE LLM API Key

### Option A: Groq (RECOMMENDED - Fastest & Easiest)

1. Go to https://console.groq.com
2. Sign up for FREE account
3. Click "API Keys" in sidebar
4. Click "Create API Key"
5. Copy your API key (starts with `gsk_...`)

**Why Groq?**
- ✅ 100% FREE
- ✅ 30 requests per minute (enough for small-medium campus)
- ✅ Very fast responses (< 1 second)
- ✅ Easy to set up
- ✅ Reliable

### Option B: Hugging Face Inference API

1. Go to https://huggingface.co/settings/tokens
2. Sign up for FREE account
3. Click "New token"
4. Select "Read" permissions
5. Copy your token (starts with `hf_...`)

### Option C: Together AI

1. Go to https://api.together.xyz
2. Sign up (get $25 FREE credit)
3. Go to "API Keys"
4. Create new key
5. Copy your API key

---

## 📦 Step 2: Prepare Your Project

### 2.1 Create vercel.json

Create this file in your project root:

```json
{
  "version": 2,
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ],
  "env": {
    "PYTHONUNBUFFERED": "1"
  }
}
```

### 2.2 Create requirements.txt for Vercel

Your `requirements.txt` should have these cloud-ready dependencies:

```
flask==3.0.0
flask-cors==4.0.0
flask-socketio==5.3.6
python-socketio==5.10.0
python-dotenv==1.0.0
requests==2.31.0
chromadb==0.4.18
sentence-transformers==2.2.2
PyPDF2==3.0.1
pdfplumber==0.10.3
numpy==1.24.3
```

**Remove these (they won't work on Vercel):**
```
# Don't include:
ollama==0.1.6  # ❌ Local only
transformers==4.36.0  # ❌ Too large for serverless
```

### 2.3 Update .env for Vercel

Your `.env` should look like this:

```env
# Flask Configuration
SECRET_KEY=your-secret-key-here-change-this

# LLM Provider (choose ONE that works on Vercel)
LLM_PROVIDER=groq

# Groq Configuration (RECOMMENDED)
GROQ_API_KEY=gsk_your_actual_groq_key_here
GROQ_MODEL=llama-3.1-8b-instant

# OR Hugging Face Inference API
# LLM_PROVIDER=huggingface_api
# HUGGINGFACE_API_KEY=hf_your_actual_token_here
# HUGGINGFACE_MODEL=mistralai/Mistral-7B-Instruct-v0.2

# OR Together AI
# LLM_PROVIDER=together
# TOGETHER_API_KEY=your_together_key_here
# TOGETHER_MODEL=mistralai/Mistral-7B-Instruct-v0.2

# Features
ENABLE_VOICE=false
ENABLE_FEEDBACK=true
ENABLE_ANALYTICS=true
```

---

## 🐙 Step 3: Push to GitHub

### 3.1 Initialize Git (if not already done)

```powershell
cd "c:\Users\shiva\OneDrive\Desktop\Vishwasri mam proj\campus-chatbot"
git init
git add .
git commit -m "Initial commit - Campus AI Chatbot"
```

### 3.2 Create GitHub Repository

1. Go to https://github.com/new
2. Name: `campus-ai-chatbot`
3. Visibility: Public or Private
4. Click "Create repository"

### 3.3 Push Code

```powershell
git remote add origin https://github.com/YOUR_USERNAME/campus-ai-chatbot.git
git branch -M main
git push -u origin main
```

---

## 🚀 Step 4: Deploy on Vercel

### 4.1 Import Project

1. Go to https://vercel.com/dashboard
2. Click "Add New..." → "Project"
3. Click "Import Git Repository"
4. Select your `campus-ai-chatbot` repository
5. Click "Import"

### 4.2 Configure Project

**Framework Preset:** Other (or detect automatically)

**Root Directory:** `./` (leave as default)

**Build Command:** Leave empty (Flask doesn't need build)

**Output Directory:** Leave empty

**Install Command:** `pip install -r requirements.txt`

### 4.3 Add Environment Variables

In the Vercel deployment settings, add these environment variables:

```
SECRET_KEY = your-random-secret-key-here
LLM_PROVIDER = groq
GROQ_API_KEY = gsk_your_actual_groq_api_key_here
GROQ_MODEL = llama-3.1-8b-instant
ENABLE_FEEDBACK = true
ENABLE_ANALYTICS = true
```

**Important:** Never commit API keys to Git! Only add them in Vercel's environment variables.

### 4.4 Deploy

1. Click "Deploy"
2. Wait 2-3 minutes for build
3. Once deployed, you'll get a URL like: `https://campus-ai-chatbot.vercel.app`

---

## 🎨 Step 5: Customize Your Campus

### 5.1 Access Admin Panel

Visit: `https://your-app.vercel.app/admin`

### 5.2 Update Configuration

1. **Campus Information**
   - University name
   - Contact details
   - Website URL

2. **Branding**
   - Primary color
   - Secondary color
   - Upload logo (hosted on CDN or use URL)

3. **Upload Documents**
   - Fee structure PDFs
   - Exam schedules
   - Hostel handbooks
   - Library guides

---

## 🔍 Step 6: Test Your Deployment

### Test Checklist

- [ ] Visit your Vercel URL
- [ ] Chat interface loads properly
- [ ] Send a test message
- [ ] Bot responds with LLM
- [ ] Upload a PDF in admin panel
- [ ] Ask question about uploaded content
- [ ] Check mobile responsiveness
- [ ] Test quick actions buttons
- [ ] Verify branding appears correctly

---

## 🐛 Troubleshooting

### Issue 1: "LLM Provider Failed to Initialize"

**Solution:**
- Check environment variables in Vercel dashboard
- Make sure `LLM_PROVIDER=groq` is set
- Verify API key is correct (no extra spaces)
- Check API key hasn't expired

### Issue 2: "Module Not Found" Errors

**Solution:**
- Ensure all dependencies in `requirements.txt`
- Remove local-only packages (ollama, transformers)
- Redeploy after updating requirements.txt

### Issue 3: "Function Timeout" Errors

**Solution:**
- Groq is usually fast enough
- If using Hugging Face API, first request may be slow (model loading)
- Consider switching to Groq for faster responses

### Issue 4: "ChromaDB Errors"

**Solution:**
- Vercel filesystem is read-only
- Use in-memory ChromaDB for serverless:

```python
# In knowledge_base.py
self.client = chromadb.Client(Settings(
    is_persistent=False,  # Use in-memory for Vercel
    anonymized_telemetry=False
))
```

### Issue 5: PDF Uploads Don't Persist

**Solution:**
- Vercel has ephemeral filesystem
- Use Vercel Blob Storage for permanent files:
  - Install: `pip install @vercel/blob`
  - Update upload logic to use Vercel Blob

---

## 💰 Cost Breakdown (FREE!)

| Service | Cost | Limits |
|---------|------|--------|
| **Vercel Hosting** | FREE | 100 GB bandwidth/month |
| **Groq API** | FREE | 30 requests/min |
| **Hugging Face API** | FREE | Rate limited (varies by model) |
| **Together AI** | $25 FREE credit | ~50K requests |
| **Domain (.vercel.app)** | FREE | Included |
| **SSL Certificate** | FREE | Auto-generated |

**Total Monthly Cost: $0** 🎉

---

## 🔒 Security Best Practices

### 1. Environment Variables
- ✅ Store API keys in Vercel environment variables
- ❌ Never commit API keys to Git
- ✅ Use strong SECRET_KEY for Flask sessions

### 2. Rate Limiting
- Implement request limits per user
- Use Vercel's Edge Config for IP-based limits

### 3. Input Validation
- Sanitize all user inputs
- Validate file uploads (size, type)
- Prevent prompt injection attacks

---

## 📈 Scaling

### Free Tier Limits (Vercel)
- 100 GB bandwidth/month
- 100 GB-hrs compute time
- Serverless function timeout: 10 seconds

### When to Upgrade

**Consider paid plans when:**
- More than 10,000 students using chatbot
- Need longer function timeouts
- Require custom domains without limits
- Need team collaboration features

### Optimization Tips

1. **Cache responses** for common questions
2. **Implement rate limiting** per user
3. **Use CDN** for static assets
4. **Compress PDFs** before upload
5. **Monitor usage** with Vercel Analytics

---

## 🎯 Custom Domain Setup

### Add Custom Domain (Optional)

1. Go to Vercel Dashboard
2. Select your project
3. Go to "Settings" → "Domains"
4. Add your domain (e.g., `chatbot.university.edu`)
5. Update DNS records as shown
6. SSL auto-configures (FREE)

---

## 🔄 Continuous Deployment

### Auto-Deploy on Git Push

Every time you push to GitHub main branch:
1. Vercel automatically detects changes
2. Builds new version
3. Runs tests
4. Deploys if successful
5. Rolls back if errors occur

```powershell
# Make changes locally
git add .
git commit -m "Updated chatbot responses"
git push

# Vercel auto-deploys in ~2 minutes
```

---

## 📊 Monitoring

### Built-in Vercel Analytics

- Real-time visitor count
- Response times
- Error rates
- Bandwidth usage

### Custom Logging

Add to your `app.py`:

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/api/chat', methods=['POST'])
def chat():
    logger.info(f"Chat request from {request.remote_addr}")
    # ... rest of code
```

View logs in Vercel Dashboard → Functions → Logs

---

## 🎓 Best Practices for Campus Deployment

### 1. Branding
- Use your university colors
- Upload official logo
- Match campus website design

### 2. Content
- Upload comprehensive handbooks
- Keep documents up-to-date
- Organize by category (fees, exams, etc.)

### 3. Testing
- Test with real student questions
- Get feedback from departments
- Iterate based on usage patterns

### 4. Promotion
- Announce on campus website
- Share on social media
- Add QR codes in campus areas
- Email to all students

---

## 📞 Support

### Get Help

1. **Check logs** in Vercel Dashboard
2. **Review error messages** in browser console (F12)
3. **Test API keys** independently
4. **Check Groq status**: https://status.groq.com

### Common Questions

**Q: How many requests can I handle?**
A: Groq FREE tier: 30 req/min = ~43,200 per day. Enough for most campuses!

**Q: Can I use multiple LLM providers?**
A: Yes! Set fallback providers in code for redundancy.

**Q: How do I update documents?**
A: Use admin panel → Documents → Upload new PDFs

**Q: Is data secure?**
A: Yes! All communication over HTTPS. API keys encrypted in Vercel.

---

## 🎉 Success Checklist

Before launching to students:

- [ ] Deployed successfully on Vercel
- [ ] Custom domain configured (optional)
- [ ] All campus information updated
- [ ] Logo and branding applied
- [ ] PDFs uploaded for all categories
- [ ] Tested with 20+ sample questions
- [ ] Mobile version tested
- [ ] Admin panel secured
- [ ] Monitoring enabled
- [ ] Feedback system working
- [ ] Department contacts updated

---

## 🚀 Next Steps

After successful deployment:

1. **Monitor Usage**
   - Track popular questions
   - Identify missing information
   - Add more content as needed

2. **Gather Feedback**
   - Add feedback button in chat
   - Survey students
   - Improve responses

3. **Expand Features**
   - Add voice input
   - Multi-language support
   - Integration with campus systems

4. **Scale**
   - Upgrade Vercel plan if needed
   - Add more LLM providers
   - Implement caching

---

## 📚 Additional Resources

- **Vercel Documentation**: https://vercel.com/docs
- **Groq API Docs**: https://console.groq.com/docs
- **Hugging Face Inference API**: https://huggingface.co/docs/api-inference
- **Flask on Vercel**: https://vercel.com/guides/using-flask-with-vercel

---

**🎓 Your Campus AI Chatbot is now live on Vercel!**

**Built with ❤️ for Educational Excellence**

Need help? Check the troubleshooting section or review the logs in Vercel Dashboard.

**Happy Deploying! 🚀**
