from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <html>
        <head>
            <title>Minha Casa</title>
        </head>
        <body>
            <h2>Minha Casa</h2>
            <h3>Acesse o menu:</h3>
            <ul>
                <li><a href="/sensors">Listar Sensores</a></li>
                <li><a href="/actuators">Listar Atuadores</a></li>
            </ul>
        </body>
        </html>
    """

@app.route("/sensors")
def sensors():
    return """
    <html>
        <head>
            <title>Minha Casa</title>
        </head>
        <body>
            <h1>Sensores</h1>
            <ul>
                <li>Sensor de Umidade</li>
                <li>Sensor de Temperatura</li>
                <li>Sensor de Luminosidade</li>
            </ul>
            <p>Voltar para <a href="/">página inicial</a>!</p>
        </body>
    </html>
    """

@app.route("/actuators")
def actuators():
    return """
    <html>
        <head>
            <title>Minha Casa</title>
        </head>
    <body>
        <h1>Atuadores</h1>
        <ul>
            <li>Servo motor</li>
            <li>Lampada</li>
        </ul>
        <p>Voltar para <a href="/">página inicial</a>!</p>
    </body>
</html>
"""


if __name__ == "__main__":
    app.run('0.0.0.0', port=80, debug=True)