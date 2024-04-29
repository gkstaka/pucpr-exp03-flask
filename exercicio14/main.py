from flask import Flask, render_template, request
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

if __name__ == "__main__":
    app.run("0.0.0.0", port=80, debug=True)
