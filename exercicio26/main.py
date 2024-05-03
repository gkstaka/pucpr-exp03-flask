from flask import Flask, render_template, request, url_for
from login import login
from sensors import sensors
from actuators import actuators

app = Flask(__name__)

app.register_blueprint(login, url_prefix='/')
app.register_blueprint(sensors, url_prefix='/')
app.register_blueprint(actuators, url_prefix='/')
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/")
def index():
    return render_template("login.html")


@app.route("/home")
def home():
    return render_template("home.html", privilege=app.config["privilege"])


if __name__ == "__main__":
    app.run("0.0.0.0", port=80, debug=True)
