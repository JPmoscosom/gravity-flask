class Vuelo:
    def __init__(self, numero_vuelo, origen, destino, hora_salida, hora_llegada, estado, puerta_embarque, avion):
        self.numero_vuelo = numero_vuelo
        self.origen = origen
        self.destino = destino
        self.hora_salida = str(hora_salida)
        self.hora_llegada = str(hora_llegada)
        self.estado = estado
        self.puerta_embarque = puerta_embarque
        self.avion = avion

    def to_JSON(self):
        return {
            'numero_vuelo': self.numero_vuelo,
            'origen': self.origen,
            'destino': self.destino,
            'hora_salida': self.hora_salida,
            'hora_llegada': self.hora_llegada,
            'estado': self.estado,
            'puerta_embarque': self.puerta_embarque,
            'avion': self.avion
        }
