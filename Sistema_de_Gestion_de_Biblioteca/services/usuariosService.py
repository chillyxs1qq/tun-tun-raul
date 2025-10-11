import json
from models.usuario import Usuario
from datetime import datetime, timedelta

class UsuarioService:
    def __init__(self):
        self.usuarios = []  # Lista interna de usuarios
        self._next_id = 1   # Contador para IDs
        self.cargar_desde_json()  # Carga inicial desde JSON

    # Obtener siguiente ID único
    def obtener_siguiente_id(self):
        id_actual = self._next_id
        self._next_id += 1
        return id_actual

    # --- CRUD ---
    def agregar_usuario(self, id_usuario, nombre, apellido, email):
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
        nombre = nombre.strip().lower()
        resultados = []
        for u in self.usuarios:
            nombre_completo = f"{u.getNombre()} {u.getApellido()}".strip().lower()
            if nombre in nombre_completo:
                resultados.append(u)
        return resultados

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
        with open("data/usuarios.json", "w", encoding="utf-8") as f:
            json.dump(lista_dicts, f, indent=4)

    def cargar_desde_json(self):
        try:
            with open("data/usuarios.json", "r", encoding="utf-8") as f:
                lista_dicts = json.load(f)
                for u_dict in lista_dicts:
                    id_usuario = int(u_dict["id"])
                    u = Usuario(
                        id_usuario,
                        u_dict["nombre"],
                        u_dict["apellido"],
                        u_dict["email"]
                    )
                    u.setEstado(u_dict.get("estado", "activo"))
                    suspension = u_dict.get("suspension_hasta")
                    if suspension:
                        u.setSuspensionHasta(datetime.fromisoformat(suspension))
                    self.usuarios.append(u)
                # Actualizar el próximo ID
                if self.usuarios:
                    self._next_id = max(u.getId() for u in self.usuarios) + 1
        except FileNotFoundError:
            pass
