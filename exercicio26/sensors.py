from flask import Flask, Blueprint, render_template, request, url_for, current_app, redirect, url_for, flash

sensors = Blueprint("sensors", __name__, template_folder="templates")
devices = {
    "Umidade": 2,
    "Temperatura": 23,
    "Luminosidade": 1034
}


@sensors.route("/register_sensor")
def register_sensor():
    return render_template("register_sensor.html", privilege=current_app.config["privilege"])


@sensors.route("/add_sensor", methods=["POST", "GET"])
def add_sensor():
    global devices
    if request.method == "POST":
        sensor = request.form["sensor"]
        reading = request.form["reading"]
    else:
        sensor = request.args.get("sensor", None)
        reading = request.args.get("reading", None)
    if sensor not in devices.keys():
        devices[sensor] = reading
    else: 
        flash("Sensor ja existente")
    return render_template("list_sensors.html", dictionary=devices, dict_type="Sensores", privilege=current_app.config["privilege"])


@sensors.route("/list_sensors")
def list_sensors():
    return render_template("list_sensors.html", dictionary=devices, dict_type="Sensores", privilege=current_app.config["privilege"])


@sensors.route("/remove_sensor")
def remove_sensor():
    return render_template("remove_sensor.html", privilege=current_app.config["privilege"], dictionary=devices)


@sensors.route("/del_sensor", methods=["GET", "POST"])
def del_sensor():
    global devices
    if request.method == "POST":
        sensor = request.form["sensor"]
    else:
        sensor = request.args.get("name")
    devices.pop(sensor)
    return redirect('list_sensors')

@sensors.route("/edit_sensor")
def edit_sensor():
    return render_template("edit_sensor.html")
    
@sensors.route("/edit_sensor_form", methods=["POST"])
def edit_sensor_form():
    global devices
    if request.method == "POST":
        new_name = request.form.get('sensor')
        old_name = request.args.get('name')
        info = devices.pop(old_name)
        devices[new_name] = info
    return redirect("list_sensors")

@sensors.route("/edit_reading")
def edit_reading():
    return render_template("edit_reading.html")

@sensors.route("/edit_reading_form", methods=["POST"])
def edit_reading_form():
    if request.method == "POST":
        name = request.args.get("name")
        reading = request.form.get("reading")
        devices[name] = reading 
    return redirect("list_sensors")