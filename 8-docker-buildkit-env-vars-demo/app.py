import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    env = os.environ.get("APP_ENV", "development")
    return f"Hello from Flask! Running in {env} mode."

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)