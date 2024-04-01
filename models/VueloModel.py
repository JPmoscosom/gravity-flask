from database.db import get_connection
from .entities.Vuelo import Vuelo


class VueloModel:

    @classmethod
    def get_all_vuelos(cls):
        try:
            connection = get_connection()
            vuelos = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM VUELOS")
                result = cursor.fetchall()
                for row in result:
                    vuelo = Vuelo(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                    vuelos.append(vuelo.to_JSON())
            connection.close()
            return vuelos
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_vuelo(cls, matricula_vuelo):
        try:
            connection = get_connection()
            print(matricula_vuelo)
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM AVIONES WHERE matricula = %s", (matricula_vuelo,))
                row = cursor.fetchone()
                vuelo = None
                if row is not None:
                    vuelo = Vuelo(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                    vuelo = vuelo.to_JSON()
            connection.close()
            return vuelo
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_vuelo(cls, vuelo):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO AVIONES (matricula, fabricante, modelo, fecha_fabricacion,
                               capacidad_pasajeros, rango, estado, propietario) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
                               (vuelo.matricula, vuelo.fabricante, vuelo.modelo, vuelo.fecha_fabricacion, vuelo.modelo,
                                vuelo.rango, vuelo.estado, vuelo.propietario))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_vuelo(cls, matricula):
        try:
            conection = get_connection()
            with conection.cursor() as cursor:
                cursor.execute("DELETE FROM AVIONES WHERE matricula = %s", (matricula,))
                affected_rows = cursor.rowcount
                conection.commit()
            conection.close()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_vuelo(cls, vuelo):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE AVIONES SET fabricante = %s, modelo = %s,
                  fecha_fabricacion = %s, capacidad_pasajeros = %s, rango = %s, estado = %s,
                   propietario = %s WHERE matricula = %s""", (vuelo.fabricante, vuelo.modelo, vuelo.fecha_fabricacion,
                                                              vuelo.capacidad_pasajeros, vuelo.rango, vuelo.estado,
                                                              vuelo.propietario, vuelo.matricula))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
