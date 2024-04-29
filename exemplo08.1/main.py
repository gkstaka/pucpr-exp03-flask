from flask import Flask, render_template, jsonify

app = Flask(__name__)
sensores = {'Umidade': 22, 'Temperatura': 23, 'Luminosidade': 1034}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/sensors")
def sensors():
    return jsonify(sensores)


@app.route("/actuators")
def actuators():
    atuadores = {"Servo motor": 122, "Lampada": 1}
    return render_template("actuators.html", atuadores=atuadores)


if __name__ == "__main__":
    app.run('0.0.0.0', port=80, debug=True)
