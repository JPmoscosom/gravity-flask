import os

from flask import Flask
from flask import jsonify, request

from models.AvionModel import AvionModel
from models.entities.Avion import Avion
from routes import Aviones, Vuelos

app = Flask(__name__)


def page_not_found(e):
    return "<h1>404 Page not found</h1>", 404


@app.route('/add', methods=['POST', 'GET'])
def add_avion():
    try:
        if request.method == "POST":
            matricula = request.json['matricula']
            fabricante = request.json['fabricante']
            modelo = request.json['modelo']
            fecha_fabricacion = request.json['fecha_fabricacion']
            capacidad_pasajeros = request.json['capacidad_pasajeros']
            rango = request.json['rango']
            estado = request.json['estado']
            propietario = request.json['propietario']
            avion = Avion(matricula, fabricante, modelo, fecha_fabricacion, capacidad_pasajeros
                          , rango, estado, propietario)
            print(avion.matricula)
            affected_rows = AvionModel.add_avion(avion)
            if affected_rows == 1:
                return jsonify({'message': 'Ok'}, 200)
            else:
                return jsonify({'message': 'Error'}, 500)
        else:
            return 'Esperando una entrada.....'

    except Exception as e:
        return jsonify({'error': str(e)}), 500


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
