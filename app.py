from flask import Flask
from config import configuration
from routes import Aviones, Vuelos

app = Flask(__name__)


def page_not_found(e):
    return "<h1>404 Page not found</h1>", 404


# Set-Ups
if __name__ == '__main__':
    # app.config.from_object(configuration['development'])
    # Blueprints
    app.register_blueprint(Aviones.main, url_prefix='/api/aviones')
    app.register_blueprint(Vuelos.main, url_prefix='/api/vuelos')
    app.register_error_handler(404, page_not_found)
    app.run(debug=True, use_reloader=False, host='0.0.0.0')








