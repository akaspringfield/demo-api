from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "<h1>Version 2 deployed automatically 🎉</h1>"}

# health check api
@app.route("/health-check")
def health():
    return {"status": "ok"}
