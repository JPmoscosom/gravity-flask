from flask import Blueprint, jsonify, request
from models.VueloModel import VueloModel
from models.entities.Vuelo import Vuelo

main = Blueprint('vuelos_blueprint', __name__)


@main.route('/')
def get_vuelos():
    try:
        vuelos = VueloModel.get_all_vuelos()
        return jsonify(vuelos)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@main.route('/<matricula>')
def get_avion(matricula):
    try:
        avion = VueloModel.get_avion(matricula)
        return avion
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@main.route('/add', methods=['POST'])
def add_avion():
    try:
        matricula = request.json['matricula']
        fabricante = request.json['fabricante']
        modelo = request.json['modelo']
        fecha_fabricacion = request.json['fecha_fabricacion']
        capacidad_pasajeros = request.json['capacidad_pasajeros']
        rango = request.json['rango']
        estado = request.json['estado']
        propietario = request.json['propietario']
        avion = Vuelo(matricula, fabricante, modelo, fecha_fabricacion, capacidad_pasajeros
                      , rango, estado, propietario)
        print(avion.matricula)
        affected_rows = VueloModel.add_avion(avion)
        if affected_rows == 1:
            return jsonify({avion.matricula})
        else:
            return jsonify({'message': 'Error'}, 500)

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@main.route('/delete/<matricula>', methods=['DELETE'])
def delete_avion(matricula):
    try:
        affected_rows = VueloModel.delete_avion(matricula)
        if affected_rows == 1:
            return jsonify(matricula)
        else:
            return jsonify({'message': 'Error'}, 500)

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@main.route('/update/<matricula>', methods=['PATCH'])
def update_avion(matricula):
    try:

        fabricante = request.json['fabricante']
        modelo = request.json['modelo']
        fecha_fabricacion = request.json['fecha_fabricacion']
        capacidad_pasajeros = request.json['capacidad_pasajeros']
        rango = request.json['rango']
        estado = request.json['estado']
        propietario = request.json['propietario']
        avion = Vuelo(matricula, fabricante, modelo, fecha_fabricacion, capacidad_pasajeros
                      , rango, estado, propietario)
        print(avion.matricula)
        affected_rows = VueloModel.update_avion(avion)
        if affected_rows == 1:
            return jsonify(avion.matricula)
        else:
            return jsonify({'message': 'Error'}, 500)

    except Exception as e:
        return jsonify({'error': str(e)}), 500
