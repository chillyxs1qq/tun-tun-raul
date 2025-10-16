import json
from datetime import datetime, timedelta
from Sistema_de_Gestion_de_Biblioteca.models.usuario import Usuario

class UsuarioService:
    def __init__(self):
        # Limpiar diccionario de usuarios antes de cargar
        Usuario._Usuario__usuarios = {}
        Usuario._Usuario__contador = 0
        self.usuarios = []
        self.ids_libres = []  # Lista de IDs disponibles
        self.cargar_desde_json()

    # ------------------ USUARIOS ------------------
    def agregar_usuario(self, nombre, apellido, email):
        id_usuario = self.obtener_siguiente_id()
        usuario = Usuario(nombre, apellido, email)
        usuario._Usuario__id = id_usuario
        if id_usuario > Usuario._Usuario__contador:
            Usuario._Usuario__contador = id_usuario
        self.usuarios.append(usuario)
        self.guardar_en_json()
        return usuario

    def buscar_usuario_por_id(self, id_usuario):
        return Usuario.buscar_por_id(int(id_usuario))

    def buscar_usuario_por_nombre(self, nombre):
        resultados = []
        nombre = nombre.strip().lower()
        for u in self.usuarios:
            if nombre in u.getNombre().lower() or nombre in u.getApellido().lower():
                resultados.append(u)
        return resultados

    def modificar_usuario(self, id_usuario, nuevo_nombre, nuevo_apellido, nuevo_email):
        usuario = self.buscar_usuario_por_id(id_usuario)
        if usuario:
            usuario.setNombre(nuevo_nombre)
            usuario.setApellido(nuevo_apellido)
            usuario.setEmail(nuevo_email)
            self.guardar_en_json()
            return True
        return False

    def eliminar_usuario(self, id_usuario):
        usuario = self.buscar_usuario_por_id(id_usuario)
        if usuario:
            self.usuarios.remove(usuario)
            Usuario._Usuario__usuarios.pop(int(id_usuario), None)
            self.ids_libres.append(int(id_usuario))  # Guardar ID libre
            self.guardar_en_json()
            return True
        return False

    def suspender_usuario(self, id_usuario, dias):
        usuario = self.buscar_usuario_por_id(id_usuario)
        if usuario and usuario.getEstado() == "activo":
            fecha_fin = datetime.now() + timedelta(days=dias)
            usuario.setEstado("suspendido")
            usuario.setSuspensionHasta(fecha_fin)
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

    # ------------------ ID ------------------
    def obtener_siguiente_id(self):
        if self.ids_libres:
            return self.ids_libres.pop(0)  # Reutilizar ID libre
        if self.usuarios:
            return max(u.getId() for u in self.usuarios) + 1
        return 1

    # ------------------ JSON ------------------
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
                ids_cargados = set()
                for d in lista_dicts:
                    uid = d["id"]
                    if uid in ids_cargados:
                        continue
                    ids_cargados.add(uid)

                    usuario = Usuario(d["nombre"], d["apellido"], d.get("email"))
                    usuario._Usuario__id = uid
                    if uid > Usuario._Usuario__contador:
                        Usuario._Usuario__contador = uid
                    usuario.setEstado(d.get("estado", "activo"))
                    if d.get("suspension_hasta"):
                        usuario.setSuspensionHasta(datetime.fromisoformat(d["suspension_hasta"]))
                    self.usuarios.append(usuario)
        except FileNotFoundError:
            pass
