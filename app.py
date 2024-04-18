from flask import Flask, jsonify
from routes import Aviones, Vuelos
from flask import Blueprint, jsonify, request
from models.AvionModel import AvionModel
from models.entities.Avion import Avion
import os

app = Flask(__name__)


def page_not_found(e):
    return "<h1>404 Page not found</h1>", 404



@app.route("/health", methods=["GET"])
def health():
    return jsonify({"Status de la API de Aviones": "200 Todo Gucci mi fai"})


@app.route("/", methods=["GET"])
def hello_world():
    return "Esta es la API de avioncitos"


app.register_blueprint(Aviones.main, url_prefix='/api/aviones')
# Set-Ups
if __name__ == '__main__':
    # app.config.from_object(configuration['development'])
    # Blueprints

    app.register_blueprint(Vuelos.main, url_prefix='/api/vuelos')
    app.register_error_handler(404, page_not_found)
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 443)), use_reloader=False)

