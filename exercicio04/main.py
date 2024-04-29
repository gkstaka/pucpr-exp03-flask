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
    return render_template("bedroom_sensor.html")

@app.route("/bedroom/actuators")
def bedroom_actuators():
    return render_template("bedroom_actuators.html")

@app.route("/bathroom")
def bathroom():
    return render_template("bathroom.html")
@app.route("/bathroom/sensors")
def bathroom_sensors():
    return render_template("bathroom_sensors.html")

@app.route("/bathroom/actuators")
def bathroom_actuators():
    return render_template("bathroom_actuators.html")





if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
    app.run(debug=True)