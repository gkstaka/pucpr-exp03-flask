from flask import Flask, render_template, request

app = Flask(__name__)

users = {
    "user1": "1234",
    "user2": "1234"
}
rooms = {
    "Quarto": "/bedroom",
    "Banheiro": "/bathroom"
}

devices = {
    "Sensores": "/bedroom/sensors",
    "Atuadores": "/bedroom/actuators"
}


@app.route("/")
def login():
    return render_template("login.html")


@app.route("/validate_user", methods=["POST"])
def validate_user():
    if request.method == "POST":
        user_id = request.form["user"]
        password = request.form["password"]
        print(user_id, password)
        if user_id in users and users[user_id] == password:
            return render_template("home.html", rooms=rooms)
        else:
            return "<h1>Login invalido</h1>"
    else:
        return render_template("login.html")


@app.route("/home")
def home():

    return render_template("home.html", rooms=rooms)


@app.route("/bedroom")
def bedroom():
    return render_template("bedroom.html", devices=devices)


@app.route("/bedroom/sensors")
def bedroom_sensors():
    sensors = {
        "Temperatura": 23,
        "Luminosidade": 1052
    }
    return render_template("bedroom_sensor.html", sensors=sensors, last_page="/bedroom")


@app.route("/bedroom/actuators")
def bedroom_actuators():
    actuators = {
        "Interruptor": 0,
        "Ar-condicionado": 1
    }
    return render_template("bedroom_actuators.html", actuators=actuators, last_page="/bedroom")


@app.route("/bathroom")
def bathroom():
    devices = {
        "Sensores": "/bathroom/sensors",
        "Atuadores": "/bathroom/actuators"
    }
    return render_template("bathroom.html", devices=devices)


@app.route("/bathroom/sensors")
def bathroom_sensors():
    sensors = {"Umidade": 80}
    return render_template("bathroom_sensors.html", sensors=sensors, last_page="/bathroom")


@app.route("/bathroom/actuators")
def bathroom_actuators():
    actuators = {
        "Lampada": 1,
        "Ventoinha": 1
    }
    return render_template("bathroom_actuators.html", actuators=actuators, last_page="/bathroom")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
    app.run(debug=True)
