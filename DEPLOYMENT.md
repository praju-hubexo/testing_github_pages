# Time & Greeting API - Deployment Guide

## Quick Deploy to Replit

1. Go to [replit.com](https://replit.com) and sign up
2. Click **"Create Repl"** → Select **Python**
3. Copy-paste the contents of `app.py` from this repo
4. Install dependencies: Run `pip install -r requirements.txt` in the console
5. Click **Run** - Your API will be live at a public URL
6. Copy the URL (e.g., `https://your-repl.username.repl.co`)
7. Update `docs/index.html` line 71: Replace `http://localhost:8000` with your Replit URL

## Deploy to Railway (Free)

1. Go to [railway.app](https://railway.app)
2. Connect your GitHub repo
3. Set Python as your runtime
4. Railway will auto-deploy when you push changes
5. Get your public URL and update it in `docs/index.html`

## Deploy to Render (Free)

1. Go to [render.com](https://render.com)
2. Create new **Web Service**
3. Connect your GitHub repo
4. Set:
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app:app --host 0.0.0.0 --port 8000`
5. Deploy and get your public URL
6. Update `docs/index.html` with the URL

## Update the GitHub Pages Documentation

Once you have your API URL, we'll update `docs/index.html` to point to your live API instead of localhost.
