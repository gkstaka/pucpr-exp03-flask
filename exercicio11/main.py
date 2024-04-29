from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    rooms = {
        "Quarto": "/bedroom",
        "Banheiro": "/bathroom" 
    }
    return render_template("index.html", rooms=rooms)

@app.route("/bedroom")
def bedroom():
    devices = {
        "Sensores": "/bedroom/sensors",
        "Atuadores": "/bedroom/actuators"
    }
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
        "Interruptor":0, 
        "Ar-condicionado":1
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