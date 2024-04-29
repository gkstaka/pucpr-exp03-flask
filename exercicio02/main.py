from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
        <html>

        <head>
            <title>Minha casa</title>
        </head>

        <body>
            <h2>Minha casa</h2>
            <h3>Acesse o menu:</h3>
            <ul>
                <li><a href="/bedroom">Quarto</a></li>
                <li><a href="/bathroom">Banheiro</a></li>
            </ul>
        </body>

        </html>
    """

@app.route("/bedroom")
def bedroom():
    return """
    <html>

    <head>
        <title>Minha casa</title>
    </head>

    <body>
        <h2>Quarto</h2>
        <ul>
            <li><a href="/bedroom/sensors">Sensores</a></li>
            <li><a href="/bedroom/actuators">Atuadores</a></li>
        </ul>

        <a href="/">
            <p>Voltar para pagina inicial</p>
        </a>
    </body>

    </html>
"""

@app.route("/bedroom/sensors")
def bedroom_sensors():
    return """
    <html>

    <head>
        <title>Minha casa</title>
    </head>

    <body>
        <h2>Sensores</h2>
        <ul>
            <li>Temperatura</li>
            <li>Luminosidade</li>
        </ul>

        <a href="/">
            <p>Voltar para pagina inicial</p>
        </a>
    </body>

    </html>
"""

@app.route("/bedroom/actuators")
def bedroom_actuators():
    return """
    <html>

    <head>
        <title>Minha casa</title>
    </head>

    <body>
        <h2>Atuadores</h2>
        <ul>
            <li>Interruptor</li>
            <li>Ar-condicionado</li>
        </ul>

        <a href="/">
            <p>Voltar para pagina inicial</p>
        </a>
    </body>

    </html>


"""

@app.route("/bathroom")
def bathroom():
    return """
    <html>

    <head>
        <title>Minha casa</title>
    </head>

    <body>
        <h2>Banheiro</h2>
        <ul>
            <li><a href="/bathroom/sensors">Sensores</a></li>
            <li><a href="/bathroom/actuators">Atuadores</a></li>
        </ul>

        <a href="/">
            <p>Voltar para pagina inicial</p>
        </a>
    </body>

    </html>
"""    
@app.route("/bathroom/sensors")
def bathroom_sensors():
    return """
    <html>

    <head>
        <title>Minha casa</title>
    </head>

    <body>
        <h2>Sensores</h2>
        <ul>
            <li>Umidade</li>
        </ul>

        <a href="/">
            <p>Voltar para pagina inicial</p>
        </a>
    </body>

    </html>
"""

@app.route("/bathroom/actuators")
def bathroom_actuators():
    return """
    <html>

    <head>
        <title>Minha casa</title>
    </head>

    <body>
        <h2>Atuadores</h2>
        <ul>
            <li>Lampada</li>
            <li>Ventoinha</li>
        </ul>

        <a href="/">
            <p>Voltar para pagina inicial</p>
        </a>
    </body>

    </html>


"""





if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
    app.run(debug=True)