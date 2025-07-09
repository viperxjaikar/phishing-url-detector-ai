# 🔐 Phishing URL Detector AI

An AI-powered phishing URL detection tool using Flask, Machine Learning, and Google Safe Browsing API.  
This app analyzes URLs and tells you whether they're **safe** or **phishing** based on intelligent ML features, real-time API checks, and user feedback.

---

## 🚀 Features

- 🧠 ML model trained on phishing & legitimate URLs
- 🌐 Google Safe Browsing API integration
- 📊 Logs all predictions and user feedback
- ✨ Beautiful responsive web UI (dark mode)
- ✅ Real-time predictions with instant feedback options

---

## 📦 Tech Stack

- **Frontend**: HTML, CSS (custom styling, dark UI)
- **Backend**: Python, Flask
- **AI/ML**: scikit-learn, pandas, tldextract
- **Security**: Google Safe Browsing API
- **Logging**: CSV file with all user feedback

---

## 🧪 How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/viperxjaikar/phishing-url-detector-ai.git
cd phishing-url-detector-ai

# 2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your Google Safe Browsing API key
# → In config.py: SAFE_BROWSING_API_KEY = "your-key-here"

# 5. Run the app
python app.py
