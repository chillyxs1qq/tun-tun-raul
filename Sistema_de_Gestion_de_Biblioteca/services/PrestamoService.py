import json
from datetime import datetime, timedelta
from models.Biblioteca.Prestamo import Prestamo
from services.Cola import Cola

class PrestamoService:
    def __init__(self, service_usuarios, service_libros):
        self.service_usuarios = service_usuarios
        self.service_libros = service_libros
        self.prestamos = []
        self.cola_espera = {}  # clave: id_libro → Cola()
        self._next_id = 1
        self.cargar_desde_json()

    # --- Crear préstamo ---
    def crear_prestamo(self, id_usuario, id_libro, dias_prestamo=7):
        try:
            id_usuario = int(id_usuario)
        except ValueError:
            return "❌ ID de usuario inválido."

        usuario = self.service_usuarios.buscar_usuario_por_id(id_usuario)
        libro = self.service_libros.buscar_por_id(id_libro)

        if not usuario:
            return "❌ Usuario no encontrado."
        if not libro:
            return "❌ Libro no encontrado."
        if usuario.getEstado() == "suspendido":
            return f"❌ Usuario suspendido hasta {usuario.getSuspensionHasta()}"

        # Ver si el libro ya está prestado
        prestado = any(p.id_libro == id_libro and not p.devuelto for p in self.prestamos)
        if prestado:
            # Meter en cola de espera
            if id_libro not in self.cola_espera:
                self.cola_espera[id_libro] = Cola()
            self.cola_espera[id_libro].encolar(id_usuario)
            return f"📚 Libro ya prestado. Usuario {id_usuario} agregado a la cola de espera."

        # Crear préstamo normal
        prestamo = Prestamo(id_usuario, id_libro, dias_prestamo)
        self.prestamos.append(prestamo)
        self.guardar_en_json()
        return f"✅ Préstamo creado: {prestamo}"

    # --- Listar préstamos ---
    def listar_prestamos(self):
        return self.prestamos

    # --- Buscar por ID ---
    def buscar_por_id(self, id_prestamo):
        for p in self.prestamos:
            if p.id_prestamo == id_prestamo:
                return p
        return None

    # --- Marcar devuelto ---
    def marcar_devuelto(self, id_prestamo):
        prestamo = self.buscar_por_id(id_prestamo)
        if not prestamo:
            return "❌ Préstamo no encontrado."
        if prestamo.devuelto:
            return "✅ Ya estaba devuelto."

        prestamo.marcar_devuelto()
        self.guardar_en_json()

        # Si hay cola de espera, darle el libro al siguiente
        if prestamo.id_libro in self.cola_espera and not self.cola_espera[prestamo.id_libro].estaVacia():
            siguiente_usuario = self.cola_espera[prestamo.id_libro].desencolar()
            self.crear_prestamo(siguiente_usuario, prestamo.id_libro)
            return f"✅ Libro devuelto. Nuevo préstamo automático para el usuario {siguiente_usuario}."

        return "✅ Libro devuelto correctamente."

    # --- Calcular sanción ---
    def calcular_sancion(self, id_prestamo):
        prestamo = self.buscar_por_id(id_prestamo)
        if not prestamo:
            return "❌ Préstamo no encontrado."
        sancion = prestamo.calcular_sancion()
        return f"Sanción actual: ${sancion}"

    # --- JSON ---
    def guardar_en_json(self):
        data = []
        for p in self.prestamos:
            data.append({
                "id_prestamo": p.id_prestamo,
                "id_usuario": p.id_usuario,
                "id_libro": p.id_libro,
                "fecha_inicio": p.fecha_inicio.strftime("%Y-%m-%d"),
                "fecha_devolucion": p.fecha_devolucion.strftime("%Y-%m-%d"),
                "devuelto": p.devuelto,
                "sancion": p.sancion
            })
        with open("prestamos.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def cargar_desde_json(self):
        try:
            with open("prestamos.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                for d in data:
                    fecha_inicio = datetime.strptime(d["fecha_inicio"], "%Y-%m-%d").date()
                    dias_prestamo = (datetime.strptime(d["fecha_devolucion"], "%Y-%m-%d").date() - fecha_inicio).days
                    prestamo = Prestamo(d["id_usuario"], d["id_libro"], dias_prestamo)
                    prestamo.id_prestamo = d["id_prestamo"]
                    prestamo.devuelto = d["devuelto"]
                    prestamo.sancion = d.get("sancion", 0)
                    prestamo.fecha_inicio = fecha_inicio
                    prestamo.fecha_devolucion = datetime.strptime(d["fecha_devolucion"], "%Y-%m-%d").date()
                    self.prestamos.append(prestamo)
                self._next_id = len(self.prestamos) + 1
        except FileNotFoundError:
            pass
