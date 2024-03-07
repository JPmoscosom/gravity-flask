from flask import Blueprint, jsonify
from models.AvionModel import AvionModel

main = Blueprint('aviones_blueprint', __name__)


@main.route('/')
def get_aviones():
    try:
        aviones = AvionModel.get_all_aviones()
        return jsonify(aviones)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
