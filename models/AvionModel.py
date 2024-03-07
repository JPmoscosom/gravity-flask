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

    @classmethod
    def get_avion(cls, matricula_avion):
        try:
            connection = get_connection()
            print(matricula_avion)
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM AVIONES WHERE matricula = %s", (matricula_avion,))
                row = cursor.fetchone()
                avion = None
                if row is not None:
                    avion = Avion(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                    avion = avion.to_JSON()
            connection.close()
            return avion
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_avion(cls, avion):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO AVIONES (matricula, fabricante, modelo, fecha_fabricacion,
                               capacidad_pasajeros, rango, estado, propietario) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
                               (avion.matricula, avion.fabricante, avion.modelo, avion.fecha_fabricacion, avion.modelo,
                                avion.rango, avion.estado, avion.propietario))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)