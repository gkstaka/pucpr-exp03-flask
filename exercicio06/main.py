from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/bedroom")
def bedroom():
    return render_template("bedroom.html")


@app.route("/bedroom/sensors")
def bedroom_sensors():
    sensores = ["Temperatura", "Luminosidade"]
    return render_template("bedroom_sensor.html", sensores=sensores)


@app.route("/bedroom/actuators")
def bedroom_actuators():
    atuadores = ["Interruptor", "Ar-condicionado"]
    return render_template("bedroom_actuators.html", atuadores=atuadores)


@app.route("/bathroom")
def bathroom():
    return render_template("bathroom.html")


@app.route("/bathroom/sensors")
def bathroom_sensors():
    sensores = ["Umidade"]
    return render_template("bathroom_sensors.html", sensores=sensores)


@app.route("/bathroom/actuators")
def bathroom_actuators():
    atuadores=["Lampada", "Ventoinha"]
    return render_template("bathroom_actuators.html", atuadores=atuadores)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
    app.run(debug=True)
