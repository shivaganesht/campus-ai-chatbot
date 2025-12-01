# 🔑 FREE LLM API Keys - Quick Setup Guide

## Get Your FREE API Key in 3 Minutes

This guide shows you how to get FREE LLM API keys that work perfectly with Vercel deployment.

---

## 🏆 Option 1: Groq (RECOMMENDED)

### Why Groq?
- ✅ **100% FREE forever**
- ✅ **30 requests per minute** (43,200 per day!)
- ✅ **Lightning fast** (< 1 second response)
- ✅ **No credit card required**
- ✅ **Works perfectly on Vercel**
- ✅ **Best models**: Llama 3.1, Mixtral, Gemma

### Get Your Groq API Key

**Step 1:** Go to https://console.groq.com

**Step 2:** Sign up with email or Google account (FREE)

**Step 3:** Once logged in, click "API Keys" in left sidebar

**Step 4:** Click "Create API Key" button

**Step 5:** Give it a name (e.g., "Campus Chatbot")

**Step 6:** Copy your API key (starts with `gsk_...`)

**Step 7:** Add to your `.env` file:
```env
LLM_PROVIDER=groq
GROQ_API_KEY=gsk_your_actual_key_here
GROQ_MODEL=llama-3.1-8b-instant
```

**Step 8:** For Vercel deployment, add the same in Vercel Dashboard → Settings → Environment Variables

### Available Groq Models

| Model | Speed | Quality | Use Case |
|-------|-------|---------|----------|
| `llama-3.1-8b-instant` | ⚡⚡⚡ Very Fast | ⭐⭐⭐ Good | General chat (RECOMMENDED) |
| `llama-3.1-70b-versatile` | ⚡⚡ Fast | ⭐⭐⭐⭐ Great | Complex questions |
| `mixtral-8x7b-32768` | ⚡⚡ Fast | ⭐⭐⭐⭐ Great | Long context |
| `gemma-7b-it` | ⚡⚡⚡ Very Fast | ⭐⭐⭐ Good | Simple queries |

**Recommended for campus chatbot:** `llama-3.1-8b-instant`

### Groq Rate Limits (FREE Tier)
- **Requests:** 30 per minute
- **Tokens:** 14,000 per minute
- **Daily:** ~43,200 requests
- **Perfect for:** Small to medium-sized campuses (up to 5,000 students)

---

## 🤗 Option 2: Hugging Face Inference API

### Why Hugging Face?
- ✅ **FREE tier available**
- ✅ **1,000+ models**
- ✅ **No credit card required**
- ✅ **Works on Vercel**
- ⚠️ Slower than Groq (first request can take 20-30 seconds)

### Get Your Hugging Face Token

**Step 1:** Go to https://huggingface.co/join

**Step 2:** Sign up (FREE)

**Step 3:** Go to https://huggingface.co/settings/tokens

**Step 4:** Click "New token"

**Step 5:** Token name: "Campus Chatbot"

**Step 6:** Token type: "Read"

**Step 7:** Click "Generate token"

**Step 8:** Copy your token (starts with `hf_...`)

**Step 9:** Add to your `.env` file:
```env
LLM_PROVIDER=huggingface_api
HUGGINGFACE_API_KEY=hf_your_actual_token_here
HUGGINGFACE_MODEL=mistralai/Mistral-7B-Instruct-v0.2
```

### Recommended Models

| Model | Speed | Quality | FREE Tier |
|-------|-------|---------|-----------|
| `mistralai/Mistral-7B-Instruct-v0.2` | ⚡⚡ Medium | ⭐⭐⭐⭐ Great | Yes |
| `meta-llama/Llama-2-7b-chat-hf` | ⚡⚡ Medium | ⭐⭐⭐ Good | Yes |
| `google/flan-t5-xxl` | ⚡⚡⚡ Fast | ⭐⭐⭐ Good | Yes |
| `bigscience/bloom` | ⚡ Slow | ⭐⭐⭐⭐ Great | Yes |

**Recommended for campus chatbot:** `mistralai/Mistral-7B-Instruct-v0.2`

### Hugging Face Rate Limits (FREE)
- **Requests:** Varies by model (typically 1-2 per second)
- **First request:** Can be slow (20-30 seconds - model loading)
- **Subsequent:** Faster (2-5 seconds)
- **Note:** Some models may have rate limits during peak hours

---

## 🔷 Option 3: Together AI

### Why Together AI?
- ✅ **$25 FREE credit** on signup
- ✅ **Fast responses**
- ✅ **Many models available**
- ✅ **Works on Vercel**
- ⚠️ Credit card required (not charged until credit expires)

### Get Your Together AI Key

**Step 1:** Go to https://api.together.xyz

**Step 2:** Click "Get Started"

**Step 3:** Sign up (you'll get $25 FREE credit)

**Step 4:** Add payment method (won't be charged until $25 credit is used)

**Step 5:** Go to "API Keys" section

**Step 6:** Click "Create new API key"

**Step 7:** Copy your key

**Step 8:** Add to your `.env` file:
```env
LLM_PROVIDER=together
TOGETHER_API_KEY=your_together_key_here
TOGETHER_MODEL=mistralai/Mistral-7B-Instruct-v0.2
```

### Together AI Credit Usage
- **$25 FREE credit** = ~50,000 requests
- **After credit expires:** ~$0.0005 per request
- **Good for:** Testing and small deployments

---

## 🆚 Comparison: Which Should You Choose?

### For Most Campus Deployments: **Groq** ⭐

| Feature | Groq | Hugging Face | Together AI |
|---------|------|--------------|-------------|
| **Cost** | FREE forever | FREE (limited) | $25 FREE credit |
| **Speed** | ⚡⚡⚡ Very Fast | ⚡⚡ Medium | ⚡⚡⚡ Fast |
| **Rate Limit** | 30 req/min | Varies | High (with credit) |
| **Setup** | 2 minutes | 2 minutes | 5 minutes |
| **Credit Card** | ❌ Not required | ❌ Not required | ✅ Required |
| **Vercel Ready** | ✅ Yes | ✅ Yes | ✅ Yes |
| **Best For** | Production | Development | Testing |

### Decision Tree

```
Do you want 100% FREE forever?
├─ YES → Use Groq ⭐
└─ NO → Do you have a credit card?
    ├─ YES → Use Together AI (fast + $25 credit)
    └─ NO → Use Hugging Face (slower but works)
```

---

## 🔧 Configuration Examples

### For Local Development (.env)

```env
# Flask Settings
SECRET_KEY=dev-secret-key-change-in-production
FLASK_ENV=development

# Choose ONE LLM provider:

# Option 1: Groq (RECOMMENDED)
LLM_PROVIDER=groq
GROQ_API_KEY=gsk_your_groq_key_here
GROQ_MODEL=llama-3.1-8b-instant

# Option 2: Hugging Face
# LLM_PROVIDER=huggingface_api
# HUGGINGFACE_API_KEY=hf_your_token_here
# HUGGINGFACE_MODEL=mistralai/Mistral-7B-Instruct-v0.2

# Option 3: Together AI
# LLM_PROVIDER=together
# TOGETHER_API_KEY=your_together_key_here
# TOGETHER_MODEL=mistralai/Mistral-7B-Instruct-v0.2
```

### For Vercel Deployment (Environment Variables)

Go to Vercel Dashboard → Your Project → Settings → Environment Variables

Add these:

```
Key: SECRET_KEY
Value: random-string-generate-strong-key

Key: LLM_PROVIDER
Value: groq

Key: GROQ_API_KEY
Value: gsk_your_actual_groq_key_here

Key: GROQ_MODEL
Value: llama-3.1-8b-instant
```

---

## 🧪 Testing Your API Key

### Test Groq Key

```powershell
curl -X POST https://api.groq.com/openai/v1/chat/completions `
  -H "Authorization: Bearer gsk_your_key_here" `
  -H "Content-Type: application/json" `
  -d '{\"model\": \"llama-3.1-8b-instant\", \"messages\": [{\"role\": \"user\", \"content\": \"Hello\"}]}'
```

### Test Hugging Face Key

```powershell
curl -X POST https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2 `
  -H "Authorization: Bearer hf_your_token_here" `
  -H "Content-Type: application/json" `
  -d '{\"inputs\": \"Hello, how are you?\"}'
```

### Test Together AI Key

```powershell
curl -X POST https://api.together.xyz/v1/chat/completions `
  -H "Authorization: Bearer your_together_key_here" `
  -H "Content-Type: application/json" `
  -d '{\"model\": \"mistralai/Mistral-7B-Instruct-v0.2\", \"messages\": [{\"role\": \"user\", \"content\": \"Hello\"}]}'
```

---

## 🔒 Security Best Practices

### DO ✅
- Store API keys in `.env` file (local)
- Add `.env` to `.gitignore`
- Use Vercel environment variables (production)
- Rotate keys every 6 months
- Use separate keys for dev/prod

### DON'T ❌
- Commit API keys to Git
- Share keys publicly
- Hardcode keys in source code
- Use same key across multiple projects
- Store keys in frontend code

---

## 📊 Usage Monitoring

### Check Your Usage

**Groq:**
- Dashboard: https://console.groq.com
- View: API Keys → Select key → Usage stats

**Hugging Face:**
- No official dashboard for Inference API
- Monitor via application logs

**Together AI:**
- Dashboard: https://api.together.xyz/dashboard
- View: Billing → Usage

---

## 🚨 Troubleshooting

### "Invalid API Key" Error

**Solution:**
1. Check for typos in key
2. Ensure no extra spaces
3. Verify key is active (not revoked)
4. Regenerate key if needed

### "Rate Limit Exceeded"

**Solution:**
1. Groq: Wait 1 minute (30 req/min limit)
2. Implement request queuing
3. Cache common responses
4. Upgrade to paid tier if needed

### "Model Not Found"

**Solution:**
1. Check model name spelling
2. Verify model is available in FREE tier
3. Use recommended models from this guide

### "Connection Timeout"

**Solution:**
1. Check internet connection
2. Verify API endpoint URL
3. Increase timeout in code (30 seconds recommended)

---

## 💡 Tips for Maximizing FREE Tier

### 1. Cache Responses
```python
# Store common questions and answers
cache = {}
if question in cache:
    return cache[question]
```

### 2. Implement Rate Limiting
```python
# Limit to 1 request per user per 5 seconds
from flask_limiter import Limiter
limiter = Limiter(app, key_func=lambda: request.remote_addr)

@app.route('/api/chat', methods=['POST'])
@limiter.limit("12 per minute")  # 30/60 = 0.5/sec, so 12/min is safe
def chat():
    # ...
```

### 3. Use Shorter Prompts
- Remove unnecessary context
- Summarize long documents
- Use concise questions

### 4. Optimize Token Usage
- Lower max_tokens (300-500 is enough)
- Use temperature=0.7 (less creative = fewer tokens)
- Trim responses programmatically

---

## 📞 Support

### Get Help

**Groq Support:**
- Discord: https://discord.gg/groq
- Email: support@groq.com
- Status: https://status.groq.com

**Hugging Face:**
- Forum: https://discuss.huggingface.co
- Discord: https://discord.gg/huggingface
- Docs: https://huggingface.co/docs

**Together AI:**
- Discord: https://discord.gg/together-ai
- Email: support@together.ai
- Docs: https://docs.together.ai

---

## 🎯 Quick Start Commands

### 1. Get Groq Key (2 minutes)
```
1. Visit: https://console.groq.com
2. Sign up (free)
3. Click "API Keys" → "Create API Key"
4. Copy key (starts with gsk_...)
```

### 2. Add to Project
```powershell
cd "c:\Users\shiva\OneDrive\Desktop\Vishwasri mam proj\campus-chatbot"
notepad .env
```

### 3. Add These Lines
```env
LLM_PROVIDER=groq
GROQ_API_KEY=gsk_your_actual_key_here
GROQ_MODEL=llama-3.1-8b-instant
```

### 4. Test Locally
```powershell
python app.py
# Visit http://localhost:5000
```

### 5. Deploy to Vercel
```
1. Push to GitHub
2. Import to Vercel
3. Add environment variables
4. Deploy!
```

---

## ✅ Checklist

Before deploying:

- [ ] Got FREE API key (Groq recommended)
- [ ] Added to `.env` file
- [ ] Tested locally
- [ ] `.env` is in `.gitignore`
- [ ] Environment variables added to Vercel
- [ ] Tested on Vercel deployment
- [ ] Monitoring usage
- [ ] Rate limiting implemented

---

**🎉 You're all set with FREE LLM API!**

**No credit card, no subscriptions, just FREE AI for your campus chatbot!**

**Questions? Check the troubleshooting section above or test your key using the curl commands.**

**Happy Coding! 🚀**
