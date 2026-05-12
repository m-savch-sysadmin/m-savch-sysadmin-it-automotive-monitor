from flask import Flask, request
from datetime import datetime
import os

app = Flask(__name__)
LOG_FILE = "/app/data/log.txt"

@app.route('/')
def index():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    
    log_entry = f"[{now}] Zalogowano wizytę | IP: {ip} | Browser: {user_agent}\n"
    
    with open(LOG_FILE, "a") as f:
        f.write(log_entry)
        
    return "<h1>Serwer Monitorowany</h1><p>Status: OK</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)