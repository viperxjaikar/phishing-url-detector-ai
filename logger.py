import csv
import os
from datetime import datetime

LOG_FILE = "logs/predictions_log.csv"

def log_prediction(url, model_result, google_result, final_result, feedback=None):
    os.makedirs("logs", exist_ok=True)
    
    with open(LOG_FILE, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if file.tell() == 0:  # File is empty
            writer.writerow(["timestamp", "url", "model_result", "google_result", "final_result", "user_feedback"])
        
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            url,
            model_result,
            google_result,
            final_result,
            feedback or "None"
        ])
