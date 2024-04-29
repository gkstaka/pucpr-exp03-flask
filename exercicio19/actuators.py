from flask import Flask, Blueprint, render_template, request

actuators = Blueprint("actuators", __name__, template_folder="templates_actuators")

devices = {
    "Servo": 122,
    "Lampada": 1
}


@actuators.route("/register_actuator")
def register_actuator():
    return render_template("register_actuator.html")


@actuators.route("/register_actuator_form", methods=["GET", "POST"])
def register_actuator_form():
    global devices
    if request.method == "POST":
        actuator = request.form["actuator"]
        state = request.form["state"]
    else:
        actuator = request.args.get("actuator", None)
        state = request.args.get("state", None)
    devices[actuator] = state
    return render_template("list_actuators.html", dictionary=devices, dict_type="Atuadores")


@actuators.route("/list_actuators")
def list_actuators():
    return render_template("list_actuators.html", dictionary=devices, dict_type="Atuadores")


@actuators.route("/remove_actuator")
def remove_actuator():
    return render_template("remove_actuator.html", dictionary=devices)


@actuators.route("/del_actuator", methods=["GET", "POST"])
def del_actuator():
    global devices
    if request.method == "POST":
        actuator = request.form["actuator"]
    else:
        actuator = request.args.get("actuator", None)
    devices.pop(actuator)
    return render_template("list_actuators.html", dict_type="Atuadores", dictionary=devices)
