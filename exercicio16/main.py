from flask import Flask, render_template, request, url_for


app = Flask(__name__)


users = {
    "user1": "1234",
    "user2": "1234",
    "123": "123"
}
sensors = {
    "Umidade": 2,
    "Temperatura": 23,
    "Luminosidade": 1034
}

actuators = {
    "Servo": 122,
    "Lampada": 1
}


@app.route("/")
def index():
    return render_template("login.html")


@app.route("/validate_user", methods=["POST"])
def validate_user():
    if request.method == "POST":
        id = request.form["user"]
        password = request.form["password"]
        if id in users and users[id] == password:
            return render_template("home.html")
        else:
            return render_template("invalid_user.html")

    return render_template("login.html")


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/register_user")
def register_user():
    return render_template("register_user.html")


@app.route("/register_user_form", methods=["POST", "GET"])
def register_user_form():
    global users
    if request.method == "POST":
        id = request.form["user"]
        password = request.form["password"]
    else:
        id = request.args.get("user", None)
        password = request.args.get("password", None)
    users[id] = password
    return render_template("list_users.html", dictionary=users, dict_type="Usuarios")


@app.route("/list_users")
def list_users():
    return render_template("list_users.html", dictionary=users, dict_type="Usuarios")


@app.route("/register_sensor")
def register_sensor():
    return render_template("register_sensor.html")


@app.route("/register_sensor_form", methods=["POST", "GET"])
def register_sensor_form():
    global sensors
    if request.method == "POST":
        sensor = request.form["sensor"]
        reading = request.form["reading"]
    else:
        sensor = request.args.get("sensor", None)
        reading = request.args.get("reading", None)
    sensors[sensor] = reading
    return render_template("list_sensors.html", dictionary=sensors, dict_type="Sensores")


@app.route("/list_sensors")
def list_sensors():
    return render_template("list_sensors.html", dictionary=sensors, dict_type="Sensores")


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


@app.route("/remove_user")
def remove_user():
    return render_template("remove_user.html", dictionary=users)


@app.route("/del_user", methods=["GET", "POST"])
def del_user():
    global users
    if request.method == "POST":
        user = request.form["user"]
    else:
        user = request.args.get("user", None)
    users.pop(user)
    return render_template("list_users.html", dict_type="Usuarios", dictionary=users)


@app.route("/remove_sensor")
def remove_sensor():
    return render_template("remove_sensor.html", dictionary=sensors)


@app.route("/del_sensor", methods=["GET", "POST"])
def del_sensor():
    global sensors
    if request.method == "POST":
        sensor = request.form["sensor"]
    else:
        sensor = request.args.get("sensor", None)
    sensors.pop(sensor)
    return render_template("list_sensors.html", dict_type="Sensores", dictionary=sensors)



if __name__ == "__main__":
    app.run("0.0.0.0", port=80, debug=True)
