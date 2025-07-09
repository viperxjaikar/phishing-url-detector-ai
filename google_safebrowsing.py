import requests

API_KEY = "AIzaSyANZZJyiKdmE1cGyiwKmwpSSoxz1_W2mOs"  # 🔁 Replace with your actual API key

def check_url_google_safebrowsing(url):
    endpoint = "https://safebrowsing.googleapis.com/v4/threatMatches:find"

    payload = {
        "client": {
            "clientId": "phishing-detector",
            "clientVersion": "1.0"
        },
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING", "UNWANTED_SOFTWARE", "POTENTIALLY_HARMFUL_APPLICATION"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": url}]
        }
    }

    params = {"key": API_KEY}
    response = requests.post(endpoint, params=params, json=payload)
    
    if response.status_code == 200:
        result = response.json()
        return bool(result.get("matches"))  # True if it's a threat
    else:
        return False
