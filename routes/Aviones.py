from flask import Blueprint, jsonify, request
from models.AvionModel import AvionModel
from models.entities.Avion import Avion

main = Blueprint('aviones_blueprint', __name__)


@main.route('/')
def get_aviones():
    try:
        aviones = AvionModel.get_all_aviones()
        return jsonify(aviones)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@main.route('/<matricula>')
def get_avion(matricula):
    try:
        avion = AvionModel.get_avion(matricula)
        return avion
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@main.route('/add/new', methods=['GET', 'POST'])
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
        avion = Avion(matricula, fabricante, modelo, fecha_fabricacion, capacidad_pasajeros
                      , rango, estado, propietario)
        print(avion.matricula)
        AvionModel.add_avion(avion)

        return jsonify({avion.matricula})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@main.route('/delete/<matricula>', methods=['DELETE'])
def delete_avion(matricula):
    try:
        affected_rows = AvionModel.delete_avion(matricula)
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
        avion = Avion(matricula, fabricante, modelo, fecha_fabricacion, capacidad_pasajeros
                      , rango, estado, propietario)
        print(avion.matricula)
        affected_rows = AvionModel.update_avion(avion)
        if affected_rows == 1:
            return jsonify(avion.matricula)
        else:
            return jsonify({'message': 'Error'}, 500)

    except Exception as e:
        return jsonify({'error': str(e)}), 500
