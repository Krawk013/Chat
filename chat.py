from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)
messages = []

@app.route("/")
def index():
    return render_template("index.html", messages=messages)

@app.route("/send_message", methods=["POST"])
def send_message():
    username = request.form["username"]
    message = request.form["message"]
    timestamp = datetime.now().strftime("%H:%M:%S")
    messages.append((timestamp, username, message))
    return index()

if __name__ == "__main__":
    app.run(debug=True)
