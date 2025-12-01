# ⚡ Vercel Deployment - Environment Variables

## 🔑 Required Environment Variables

Add these in **Vercel Dashboard → Settings → Environment Variables**:

```
SECRET_KEY=campus-chatbot-secret-key-2025-change-this
LLM_PROVIDER=groq
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=llama-3.1-8b-instant
```

**Note**: Replace `your_groq_api_key_here` with your actual Groq API key from https://console.groq.com

## 📝 Step-by-Step Setup

### 1. Open Vercel Dashboard
https://vercel.com/shivaganesht/campus-ai-chatbot

### 2. Go to Settings
Click "Settings" tab → "Environment Variables"

### 3. Add Each Variable

**Variable 1:**
- **Key**: `SECRET_KEY`
- **Value**: `campus-chatbot-secret-key-2025-change-this`
- **Environment**: Production, Preview, Development (select all)

**Variable 2:**
- **Key**: `LLM_PROVIDER`
- **Value**: `groq`
- **Environment**: Production, Preview, Development (select all)

**Variable 3:**
- **Key**: `GROQ_API_KEY`
- **Value**: `YOUR_ACTUAL_GROQ_API_KEY` (get from https://console.groq.com)
- **Environment**: Production, Preview, Development (select all)

**Variable 4:**
- **Key**: `GROQ_MODEL`
- **Value**: `llama-3.1-8b-instant`
- **Environment**: Production, Preview, Development (select all)

### 4. Redeploy

After adding all variables:
1. Go to "Deployments" tab
2. Click the three dots (...) on the latest deployment
3. Click "Redeploy"
4. Wait 2-3 minutes

## ✅ Verification

Once deployed, test these endpoints:

1. **Health Check**:
   ```
   https://your-app.vercel.app/api/health
   ```
   Should return: `{"status": "healthy", "llm_provider": "groq"}`

2. **Main Page**:
   ```
   https://your-app.vercel.app/
   ```
   Should show the chatbot interface

3. **Test Chat**:
   Send a message and verify you get a response from Groq

## 🐛 Troubleshooting

### "LLM Provider Failed"
- Check that `GROQ_API_KEY` is set correctly
- Verify no extra spaces in the key
- Make sure all environment variables are in "Production" scope

### "500 Internal Server Error"
- Check Vercel function logs (Dashboard → Functions → Logs)
- Verify all 4 environment variables are set
- Try redeploying after setting variables

### "App loads but no response"
- Test API key with curl:
  ```bash
  curl -X POST https://api.groq.com/openai/v1/chat/completions \
    -H "Authorization: Bearer YOUR_KEY" \
    -H "Content-Type: application/json" \
    -d '{"model": "llama-3.1-8b-instant", "messages": [{"role": "user", "content": "Hi"}]}'
  ```

## 📊 Current Status

- **Repository**: github.com/shivaganesht/campus-ai-chatbot
- **Vercel Project**: campus-ai-chatbot
- **Dependencies**: ✅ Optimized for Vercel (< 50MB)
- **Serverless**: ✅ No SocketIO, plain Flask
- **LLM**: Groq API (FREE, 30 req/min)

## 🎯 Quick Deploy Checklist

- [ ] All 4 environment variables added in Vercel
- [ ] Variables set for all environments (Production, Preview, Development)
- [ ] Redeployed after adding variables
- [ ] Tested `/api/health` endpoint
- [ ] Tested main page loads
- [ ] Tested sending a chat message
- [ ] Verified bot responds

---

**Your chatbot should be live at**: `https://campus-ai-chatbot-<random>.vercel.app`

**Need help?** Check Vercel logs in Dashboard → Deployments → [Latest] → Function Logs
