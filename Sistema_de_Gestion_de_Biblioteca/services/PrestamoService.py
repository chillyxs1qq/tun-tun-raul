import json
from datetime import datetime, timedelta
from models.Biblioteca.Prestamo import Prestamo

class PrestamoService:
    def __init__(self, usuario_service, libro_service):
        self.usuarios = usuario_service
        self.libros = libro_service
        self.prestamos = []
        self.cargar_desde_json()

    def crear_prestamo(self, id_usuario, id_libro, dias_prestamo=7):
        usuario = self.usuarios.buscar_usuario_por_id(int(id_usuario))
        if not usuario:
            raise ValueError(f"No hay un usuario con el ID {id_usuario}")

        libro = self.libros.buscar_por_id(id_libro)
        if not libro:
            raise ValueError(f"No hay un libro con el ID {id_libro}")

        if not libro.prestamohabilitado:
            libro.encolar_usuario(id_usuario)
            self.libros.guardar_en_json()
            return f"Libro ocupado, usuario agregado a la cola ({len(libro.verCola())} en espera)"

        prestamo = Prestamo(int(id_usuario), id_libro, dias_prestamo)
        self.prestamos.append(prestamo)
        libro.prestamohabilitado = False

        self.guardar_en_json()
        self.libros.guardar_en_json()
        return prestamo

    def listar_prestamos(self):
        return self.prestamos

    def marcar_devuelto(self, id_prestamo):
        prestamo = next((p for p in self.prestamos if p.id_prestamo == id_prestamo), None)
        if prestamo and not prestamo.devuelto:
            prestamo.marcar_devuelto()
            libro = self.libros.buscar_por_id(prestamo.id_libro)
            if libro:
                siguiente_usuario = libro.desencolar_usuario()
                if siguiente_usuario:
                    nuevo_prestamo = Prestamo(siguiente_usuario, libro.id, 7)
                    self.prestamos.append(nuevo_prestamo)
                    mensaje = f"Libro asignado automáticamente al usuario ID {siguiente_usuario}"
                else:
                    libro.prestamohabilitado = True
                    mensaje = "Libro devuelto y ahora disponible"

                self.guardar_en_json()
                self.libros.guardar_en_json()
                return mensaje
        return False

    def ver_colas_de_espera(self):
        colas = {}
        for libro in self.libros.listar_libros():
            if libro.verCola():
                colas[libro.titulo] = libro.verCola()
        return colas

    # --- JSON ---
    def guardar_en_json(self):
        lista_dicts = []
        for p in self.prestamos:
            lista_dicts.append({
                "id_prestamo": p.id_prestamo,
                "id_usuario": p.id_usuario,
                "id_libro": p.id_libro,
                "fecha_inicio": p.fecha_inicio.isoformat(),
                "fecha_devolucion": p.fecha_devolucion.isoformat(),
                "devuelto": p.devuelto,
                "sancion": p.sancion
            })
        with open("data/prestamos.json", "w", encoding="utf-8") as f:
            json.dump(lista_dicts, f, indent=4)

        libros_dicts = [libro.to_dict() for libro in self.libros.listar_libros()]
        with open("data/libros.json", "w", encoding="utf-8") as f:
            json.dump(libros_dicts, f, indent=4)

    def cargar_desde_json(self):
        try:
            with open("data/prestamos.json", "r", encoding="utf-8") as f:
                lista_dicts = json.load(f)
                for d in lista_dicts:
                    if not self.usuarios.buscar_usuario_por_id(int(d["id_usuario"])):
                        continue
                    dias = (datetime.fromisoformat(d["fecha_devolucion"]).date() - datetime.fromisoformat(d["fecha_inicio"]).date()).days
                    prestamo = Prestamo(d["id_usuario"], d["id_libro"], dias)
                    prestamo.id_prestamo = d["id_prestamo"]
                    prestamo.fecha_inicio = datetime.fromisoformat(d["fecha_inicio"]).date()
                    prestamo.fecha_devolucion = datetime.fromisoformat(d["fecha_devolucion"]).date()
                    prestamo.devuelto = d["devuelto"]
                    prestamo.sancion = d.get("sancion", 0)

                    libro = self.libros.buscar_por_id(prestamo.id_libro)
                    if libro:
                        libro.prestamohabilitado = prestamo.devuelto

                    self.prestamos.append(prestamo)

            try:
                with open("data/libros.json", "r", encoding="utf-8") as f:
                    libros_dicts = json.load(f)
                    for d in libros_dicts:
                        libro = self.libros.buscar_por_id(d["id"])
                        if libro and d.get("cola_espera"):
                            libro.cargar_cola(d["cola_espera"])
            except FileNotFoundError:
                pass

        except FileNotFoundError:
            pass
