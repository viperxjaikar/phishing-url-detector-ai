import re
import math
from urllib.parse import urlparse
import tldextract

# Suspicious keywords commonly found in phishing URLs
SUSPICIOUS_KEYWORDS = [
    'login', 'verify', 'update', 'free', 'secure', 'account',
    'webscr', 'confirm', 'bank', 'paypal', 'signin', 'submit'
]

# Whitelist of popular trusted domains
WHITELIST = [
    'google.com', 'youtube.com', 'microsoft.com',
    'github.com', 'amazon.com', 'facebook.com'
]

def calculate_entropy(s):
    probabilities = [float(s.count(c)) / len(s) for c in set(s)]
    return -sum(p * math.log(p) / math.log(2.0) for p in probabilities)

def extract_features(url):
    features = []

    parsed = urlparse(url)
    ext = tldextract.extract(url)

    domain = ext.domain + '.' + ext.suffix
    subdomain = ext.subdomain
    path = parsed.path

    # 1. URL Length
    features.append(len(url))

    # 2. Domain Length
    features.append(len(domain))

    # 3. Path Length
    features.append(len(path))

    # 4–10. Count of specific characters
    features.append(url.count('.'))
    features.append(url.count('-'))
    features.append(url.count('@'))
    features.append(url.count('%'))
    features.append(url.count('='))
    features.append(url.count('~'))

    # 11. Number of digits
    digits = len(re.findall(r'\d', url))
    features.append(digits)

    # 12. Number of letters
    letters = len(re.findall(r'[a-zA-Z]', url))
    features.append(letters)

    # 13. Digit-to-letter ratio
    ratio = digits / (letters + 1e-5)
    features.append(ratio)

    # 14. Use of HTTPS
    features.append(1 if parsed.scheme == 'https' else 0)

    # 15. Subdomain count
    features.append(len(subdomain.split('.')) if subdomain else 0)

    # 16. Entropy
    features.append(calculate_entropy(url))

    # 17–28. Suspicious keyword presence
    for keyword in SUSPICIOUS_KEYWORDS:
        features.append(1 if keyword in url.lower() else 0)

    # 29. Uses IP instead of domain
    features.append(1 if re.match(r'^http[s]?://\d+\.\d+\.\d+\.\d+', url) else 0)

    # 30. Extra slashes in path
    features.append(1 if '//' in path else 0)

    # 31. Whitelisted domain
    features.append(1 if domain in WHITELIST else 0)

    return features
