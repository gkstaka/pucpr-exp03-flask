from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Conteudo da pagina inicial:"

@app.route("/")
def sensors():
    return "Listar sensores"

@app.route("/")
def actuators():
    return "Listar atuadores"


if __name__ == "__main__":
    app.run('0.0.0.0', port=80, debug=True)