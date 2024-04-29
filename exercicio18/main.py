from flask import Flask, render_template, request, url_for
from login import login
from sensors import sensors

app = Flask(__name__)

app.register_blueprint(login, url_prefix='/')
app.register_blueprint(sensors, url_prefix='/')

actuators = {
    "Servo": 122,
    "Lampada": 1
}


@app.route("/")
def index():
    return render_template("login.html")


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/register_actuator")
def register_actuator():
    return render_template("register_actuator.html")


@app.route("/register_actuator_form", methods=["GET", "POST"])
def register_actuator_form():
    global actuators
    if request.method == "POST":
        actuator = request.form["actuator"]
        state = request.form["state"]
    else:
        actuator = request.args.get("actuator", None)
        state = request.args.get("state", None)
    actuators[actuator] = state
    return render_template("list_actuators.html", dictionary=actuators, dict_type="Atuadores")


@app.route("/list_actuators")
def list_actuators():
    return render_template("list_actuators.html", dictionary=actuators, dict_type="Atuadores")


@app.route("/remove_actuator")
def remove_actuator():
    return render_template("remove_actuator.html", dictionary=actuators)


@app.route("/del_actuator", methods=["GET", "POST"])
def del_actuator():
    global actuators
    if request.method == "POST":
        actuator = request.form["actuator"]
    else:
        actuator = request.args.get("actuator", None)
    actuators.pop(actuator)
    return render_template("list_actuators.html", dict_type="Atuadores", dictionary=actuators)


if __name__ == "__main__":
    app.run("0.0.0.0", port=80, debug=True)
