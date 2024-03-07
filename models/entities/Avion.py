class Avion:
    def __init__(self, matricula, fabricante, modelo, fecha_fabricacion, capacidad_pasajeros, rango, estado,
                 propietario):
        self.matricula = matricula
        self.fabricante = fabricante
        self.modelo = modelo
        self.fecha_fabricacion = fecha_fabricacion
        self.capacidad_pasajeros = capacidad_pasajeros
        self.rango = rango
        self.estado = estado
        self.propietario = propietario

    def to_JSON(self):
        return {
            'matricula': self.matricula,
            'fabricante': self.fabricante,
            'modelo': self.modelo,
            'fecha_fabricacion': self.fecha_fabricacion,
            'capacidad_pasajeros': self.capacidad_pasajeros,
            'rango': self.rango,
            'estado': self.estado,
            'propietario': self.propietario
        }
