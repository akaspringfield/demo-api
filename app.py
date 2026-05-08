from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "API running"}

@app.route("/health-check")
def health():
    return {"status": "ok"}