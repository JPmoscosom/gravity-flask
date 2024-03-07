from database.db import get_connection
from .entities.Avion import Avion


class AvionModel:

    @classmethod
    def get_all_aviones(cls):
        try:
            connection = get_connection()
            aviones = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM AVIONES")
                result = cursor.fetchall()
                for row in result:
                    avion = Avion(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                    aviones.append(avion.to_JSON())
            connection.close()
            return aviones
        except Exception as ex:
            raise Exception(ex)