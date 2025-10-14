from datetime import datetime, timedelta
from Sistema_de_Gestion_de_Biblioteca.models.usuario import Usuario

class Prestamo:
    __prestamos = {}  # Diccionario de todos los préstamos
    __contador = 0    # Contador para IDs automáticos

    def __init__(self, id_usuario, id_libro, dias_prestamo=7):
        usuario = Usuario.buscar_por_id(id_usuario)
        if not usuario:
            raise ValueError(f"No hay un usuario con el ID {id_usuario}")

        Prestamo.__contador += 1
        self.id_prestamo = f"PRE{Prestamo.__contador:04d}"

        self.usuario = usuario
        self.id_usuario = id_usuario
        self.id_libro = id_libro
        self.fecha_inicio = datetime.now().date()
        self.fecha_devolucion = self.fecha_inicio + timedelta(days=dias_prestamo)
        self.devuelto = False
        self.sancion = 0

        # Guardar en diccionario
        Prestamo.__prestamos[self.id_prestamo] = self

    def marcar_devuelto(self):
        self.devuelto = True
        dias_retraso = (datetime.now().date() - self.fecha_devolucion).days
        if dias_retraso > 0:
            self.sancion = dias_retraso * 10  # ejemplo: $10 por día de retraso
        else:
            self.sancion = 0

    def calcular_sancion(self):
        if not self.devuelto:
            dias_retraso = (datetime.now().date() - self.fecha_devolucion).days
            return max(dias_retraso * 10, 0)
        return self.sancion

    @classmethod
    def obtener_todos(cls):
        return list(cls.__prestamos.values())

    @classmethod
    def buscar_por_id(cls, id_prestamo):
        return cls.__prestamos.get(id_prestamo)

    def __str__(self):
        estado = "Devuelto" if self.devuelto else "Vigente"
        return f"{self.id_prestamo} | Usuario: {self.id_usuario} | Libro: {self.id_libro} | Inicio: {self.fecha_inicio} | Vencimiento: {self.fecha_devolucion} | Estado: {estado} | Sanción: ${self.sancion}"
