from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, web world"

if __name__ == "__main__":
    app.run('0.0.0.0', port=80, debug=True)