from flask import Flask, render_template, request
from feature_extraction import extract_features
from google_safebrowsing import check_url_google_safebrowsing
from logger import log_prediction
import joblib

app = Flask(__name__)
model = joblib.load('phishing_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    url = request.form['url']

    # Step 1: Google Safe Browsing
    is_threat = check_url_google_safebrowsing(url)

    # Step 2: ML model prediction
    model_pred = model.predict([extract_features(url)])[0]
    model_result = "Phishing" if model_pred == 1 else "Safe"

    # Step 3: Combine results
    if is_threat:
        final_result = "Phishing (Google)"
        result = "🔴 Phishing Website (Verified by Google Safe Browsing)"
    elif model_pred == 1:
        final_result = "Phishing (Model)"
        result = "🔴 Phishing Website (Detected by AI Model)"
    else:
        final_result = "Safe"
        result = "🟢 Safe Website"

    # Log result
    log_prediction(url, model_result, str(is_threat), final_result)

    return render_template('index.html', url=url, result=result)

@app.route('/feedback', methods=['POST'])
def feedback():
    url = request.form['url']
    result = request.form['result']
    feedback = request.form['feedback']

    # Log the feedback
    log_prediction(url, "-", "-", result, feedback)

    # Re-show the result with feedback confirmation
    return render_template('index.html', url=url, result=result, feedback_recorded=True)

if __name__ == '__main__':
    app.run(debug=True)
