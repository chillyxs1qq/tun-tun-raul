from datetime import datetime, timedelta

class Prestamo:
    def __init__(self, id_prestamo, id_usuario, id_libro, fecha_inicio=None, dias_prestamo=7):
        self.id_prestamo = id_prestamo
        self.id_usuario = id_usuario
        self.id_libro = id_libro
        self.fecha_inicio = fecha_inicio or datetime.today()
        self.fecha_devolucion = self.fecha_inicio + timedelta(days=dias_prestamo)
        self.devuelto = False
        self.sancion = 0

    def marcar_devuelto(self):
        self.devuelto = True

    def calcular_sancion(self):
        if not self.devuelto:
            hoy = datetime.today()
            if hoy > self.fecha_devolucion:
                dias_retraso = (hoy - self.fecha_devolucion).days
                self.sancion = dias_retraso * 5  # $5 por día de retraso
        return self.sancion

    def __str__(self):
        estado = "Devuelto" if self.devuelto else "Pendiente"
        return (f"[{self.id_prestamo}] Usuario: {self.id_usuario} | Libro: {self.id_libro} | "
                f"Fecha límite: {self.fecha_devolucion.date()} | Estado: {estado} | Sanción: ${self.sancion}")
