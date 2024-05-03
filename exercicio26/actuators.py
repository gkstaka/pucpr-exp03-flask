from flask import Flask, Blueprint, render_template, request, flash, current_app, redirect

actuators = Blueprint("actuators", __name__, template_folder="templates_actuators")

devices = {
    "Servo": 122,
    "Lampada": 1
}


@actuators.route("/register_actuator")
def register_actuator():
    return render_template("register_actuator.html", privilege=current_app.config["privilege"])


@actuators.route("/add_actuator", methods=["GET", "POST"])
def add_actuator():
    global devices
    if request.method == "POST":
        actuator = request.form["actuator"]
        state = request.form["state"]
    else:
        actuator = request.args.get("actuator", None)
        state = request.args.get("state", None)
    if actuator not in devices.keys():
        devices[actuator] = state
    else:
        flash("Atuador ja existente")
    return render_template("list_actuators.html", dictionary=devices, dict_type="Atuadores", privilege=current_app.config["privilege"])


@actuators.route("/list_actuators")
def list_actuators():
    return render_template("list_actuators.html", dictionary=devices, dict_type="Atuadores", privilege=current_app.config["privilege"])


@actuators.route("/remove_actuator")
def remove_actuator():
    return render_template("remove_actuator.html", dictionary=devices, privilege=current_app.config["privilege"])


@actuators.route("/del_actuator", methods=["GET", "POST"])
def del_actuator():
    global devices
    if request.method == "POST":
        actuator = request.form["name"]
    else:
        actuator = request.args.get("name", None)
    devices.pop(actuator)
    return render_template("list_actuators.html", dict_type="Atuadores", dictionary=devices, privilege=current_app.config["privilege"])

@actuators.route("/edit_actuator")
def edit_actuator():
    return render_template("edit_actuator.html")
    
@actuators.route("/edit_actuator_form", methods=["POST"])
def edit_actuator_form():
    global devices
    if request.method == "POST":
        new_name = request.form.get('actuator')
        old_name = request.args.get('name')
        info = devices.pop(old_name)
        devices[new_name] = info
    return redirect("list_actuators")

@actuators.route("/edit_state")
def edit_reading():
    return render_template("edit_state.html")

@actuators.route("/edit_state_form", methods=["POST"])
def edit_state_form():
    if request.method == "POST":
        name = request.args.get("name")
        state = request.form.get("state")
        devices[name] = state 
    return redirect("list_actuators")