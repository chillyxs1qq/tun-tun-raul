import json
from models.usuario import Usuario
from datetime import datetime, timedelta

class UsuarioService:
    def __init__(self):
        self.usuarios = []
        self._next_id = 1
        self.cargar_desde_json()  # cargamos usuarios al iniciar

    def obtener_siguiente_id(self):
        id_actual = self._next_id
        self._next_id += 1
        return id_actual

    # --- CRUD de usuarios ---
    def agregar_usuario(self, id_usuario, nombre, apellido, email):
        if self.buscar_usuario_por_id(id_usuario):
            return False
        nuevo = Usuario(id_usuario, nombre, apellido, email)
        self.usuarios.append(nuevo)
        self.guardar_en_json()
        return nuevo

    def eliminar_usuario(self, id_usuario):
        usuario = self.buscar_usuario_por_id(id_usuario)
        if usuario:
            self.usuarios.remove(usuario)
            self.guardar_en_json()
            return True
        return False

    def modificar_usuario(self, id_usuario, nuevo_nombre, nuevo_apellido, nuevo_email):
        usuario = self.buscar_usuario_por_id(id_usuario)
        if usuario:
            usuario.setNombre(nuevo_nombre)
            usuario.setApellido(nuevo_apellido)
            usuario.setEmail(nuevo_email)
            self.guardar_en_json()
            return True
        return False

    # --- Búsquedas ---
    def buscar_usuario_por_id(self, id_usuario):
        for u in self.usuarios:
            if u.getId() == id_usuario:
                return u
        return None

    def buscar_usuario_por_nombre(self, nombre):
        return [u for u in self.usuarios if nombre.lower() in u.getNombre().lower()]

    # --- Suspensiones ---
    def suspender_usuario(self, id_usuario, dias=7):
        usuario = self.buscar_usuario_por_id(id_usuario)
        if usuario:
            usuario.setEstado("suspendido")
            usuario.setSuspensionHasta(datetime.now() + timedelta(days=dias))
            self.guardar_en_json()
            return True
        return False

    def reactivar_usuario(self, id_usuario):
        usuario = self.buscar_usuario_por_id(id_usuario)
        if usuario and usuario.getEstado() == "suspendido":
            if usuario.getSuspensionHasta() and usuario.getSuspensionHasta() <= datetime.now():
                usuario.setEstado("activo")
                usuario.setSuspensionHasta(None)
                self.guardar_en_json()
                return True
        return False

    # --- JSON ---
    def guardar_en_json(self):
        lista_dicts = []
        for u in self.usuarios:
            lista_dicts.append({
                "id": u.getId(),
                "nombre": u.getNombre(),
                "apellido": u.getApellido(),
                "email": u.getEmail(),
                "estado": u.getEstado(),
                "suspension_hasta": u.getSuspensionHasta().isoformat() if u.getSuspensionHasta() else None
            })
        with open("usuarios.json", "w", encoding="utf-8") as f:
            json.dump(lista_dicts, f, indent=4)

    def cargar_desde_json(self):
        try:
            with open("usuarios.json", "r", encoding="utf-8") as f:
                lista_dicts = json.load(f)
                for u_dict in lista_dicts:
                    u = Usuario(
                        u_dict["id"],
                        u_dict["nombre"],
                        u_dict["apellido"],
                        u_dict["email"]
                    )
                    u.setEstado(u_dict.get("estado", "activo"))
                    suspension = u_dict.get("suspension_hasta")
                    if suspension:
                        u.setSuspensionHasta(datetime.fromisoformat(suspension))
                    self.usuarios.append(u)
                # Actualizamos _next_id para no repetir IDs
                if self.usuarios:
                    self._next_id = max(u.getId() for u in self.usuarios) + 1
        except FileNotFoundError:
            pass  # si no existe el archivo, no pasa nada
