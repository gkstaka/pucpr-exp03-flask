from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
    
   

@app.route("/sensors")
def sensors():
    sensores = ['Umidade', 'Temperatura', 'Luminosidade']
    return render_template("sensors.html", sensores=sensores)
    
    

@app.route("/actuators")
def actuators():
    return render_template("actuators.html")
    


if __name__ == "__main__":
    app.run('0.0.0.0', port=80, debug=True)