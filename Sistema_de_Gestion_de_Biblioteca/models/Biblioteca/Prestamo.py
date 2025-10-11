from datetime import datetime, timedelta
from models.usuario import Usuario

class Prestamo:

    __prestamos = 0  # contador de préstamos automáticos

    def __init__(self, id_usuario, id_libro, dias=7):
        self.id_prestamo = f"PRE{Prestamo.__prestamos + 1:04d}"
        Prestamo.__prestamos += 1

        self.id_usuario = int(id_usuario)  # referencia al usuario
        self.id_libro = id_libro

        self.fecha_prestamo = datetime.now()
        self.fecha_devolucion = self.fecha_prestamo + timedelta(days=dias)
        self.devuelto = False

    def marcar_devuelto(self):
        self.devuelto = True

    def calcular_sancion(self):
        if self.devuelto:
            return 0
        hoy = datetime.now()
        retraso = (hoy - self.fecha_devolucion).days
        return max(0, retraso * 5)  # ejemplo: 5 unidades por día de retraso

    def __str__(self):
        return (f"|Prestamo: {self.id_prestamo}|Usuario ID: {self.id_usuario}|Libro ID: {self.id_libro}|"
                f"Fecha préstamo: {self.fecha_prestamo.strftime('%Y-%m-%d')}|"
                f"Vencimiento: {self.fecha_devolucion.strftime('%Y-%m-%d')}|Devuelto: {self.devuelto}|")
