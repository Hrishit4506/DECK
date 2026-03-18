# Deploying to Render

## ✅ What We've Set Up

Your app is now ready for Render deployment! Here's what we've added:

### 📋 **Dependencies**
- ✅ Clean `requirements.txt` with only necessary packages
- ✅ `gunicorn` for production-ready WSGI server

### 🚀 **Deployment Files**
- ✅ `render.yaml` - Render deployment configuration
- ✅ `Procfile` - Process file for running the app
- ✅ Updated `app.py` to use PORT environment variable

### 🔧 **Production-Ready Changes**
- ✅ App runs on `0.0.0.0` (accessible externally)
- ✅ Port configurable via `PORT` environment variable
- ✅ Debug mode controlled by `FLASK_DEBUG` environment variable

## 📝 Step-by-Step Deployment Guide

### 1. Sign Up / Log In to Render

- Go to [render.com](https://render.com)
- Sign up with GitHub for easiest integration
- It's FREE for basic usage!

### 2. Push Your Code to GitHub

```bash
git init
git add .
git commit -m "Initial commit - Clash Royale Deck Analyzer"
git branch -M main

# Create a GitHub repository first, then:
git remote add origin https://github.com/YOUR_USERNAME/clash-royale-deck-analyzer.git
git push -u origin main
```

### 3. Create New Web Service on Render

- Click "New" → "Web Service"
- Connect your GitHub repository
- Select your repository

### 4. Configure Your Service

**Build Settings:**
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn app:app`

**Instance Details:**
- **Name:** `clash-royale-deck-analyzer` (or your choice)
- **Region:** Pick closest to you (e.g., Ohio, Frankfurt)
- **Branch:** `main`

**Environment:**
- Python 3
- Free tier (unless you need more resources)

### 5. Add Environment Variable

Add your Clash Royale API token:

- **Key:** `CLASH_API_TOKEN`
- **Value:** Your API token from [developer.clashroyale.com](https://developer.clashroyale.com)

### 6. Deploy!

- Click "Create Web Service"
- Wait for the build and deployment
- Once complete, click the URL to access your app

## 🔐 Important Notes

### Clash Royale API Token Setup:

1. Go to [Clash Royale for Developers](https://developer.clashroyale.com)
2. Create an account and log in
3. Create a new API key
4. Add your Render app IP to allowed IPs (or leave open for testing)
5. Copy the token to Render environment variables

### Render Free Tier Limitations:

- ✅ Perfect for personal use
- ⚠️ App sleeps after 15 minutes of inactivity
- ⚠️ Takes ~30 seconds to "wake up" when idle
- ⚠️ Limited to 750 hours/month (but plenty for a personal app)
- ✅ No credit card required

### Optional: Keep Alive

To prevent sleeping, you can use a free uptime monitor:
- [UptimeRobot](https://uptimerobot.com/)
- [Render has native cron jobs](https://render.com/docs/cronjobs)

## 🧪 Test Before Deploying

Test locally with production settings:

```bash
# Set environment variables
export FLASK_DEBUG=False
export PORT=5000

# Run with gunicorn (simulating Render)
gunicorn app:app

# Or with Python
python app.py
```

## 🐛 Troubleshooting

**If deployment fails:**
1. Check build logs in Render dashboard
2. Ensure all files are committed to GitHub
3. Verify `CLASH_API_TOKEN` is set correctly
4. Check Python version compatibility

**Common Issues:**
- Missing environment variable → Add CLASH_API_TOKEN
- Port already in use → Render sets PORT automatically
- Module not found → Check requirements.txt

---

## 🎉 You're Ready to Deploy!

Your Clash Royale Deck Analyzer is production-ready and configured for Render deployment. Just follow the steps above and your app will be live in minutes!
