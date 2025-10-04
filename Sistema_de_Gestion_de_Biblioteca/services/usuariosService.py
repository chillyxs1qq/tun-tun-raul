import json  # Para guardar y cargar usuarios en formato JSON
from models.usuario import Usuario  # Clase Usuario
from datetime import datetime, timedelta  # Para fechas de suspensión

class UsuarioService:
    def __init__(self):
        self.usuarios = []  # Lista interna que guarda todos los usuarios
        self._next_id = 1  # Contador de IDs para crear nuevos usuarios automáticamente
        self.cargar_desde_json()  # Al iniciar, cargamos usuarios desde el archivo JSON si existe

    def obtener_siguiente_id(self):
        id_actual = self._next_id  # Guardamos el ID que vamos a devolver
        self._next_id += 1  # Aumentamos el contador para el próximo usuario
        return id_actual  # Devolvemos el ID único

    # --- CRUD de usuarios ---
    def agregar_usuario(self, id_usuario, nombre, apellido, email):
        if self.buscar_usuario_por_id(id_usuario):  # Si ya existe un usuario con ese ID
            return False  # No se agrega
        nuevo = Usuario(id_usuario, nombre, apellido, email)  # Creamos el objeto Usuario
        self.usuarios.append(nuevo)  # Lo añadimos a la lista interna
        self.guardar_en_json()  # Guardamos los cambios en el JSON
        return nuevo  # Devolvemos el usuario creado

    def eliminar_usuario(self, id_usuario):
        usuario = self.buscar_usuario_por_id(id_usuario)  # Buscamos al usuario por ID
        if usuario:  # Si existe
            self.usuarios.remove(usuario)  # Lo eliminamos de la lista
            self.guardar_en_json()  # Guardamos cambios en JSON
            return True  # Confirmamos que se eliminó
        return False  # Si no se encontró, devolvemos False

    def modificar_usuario(self, id_usuario, nuevo_nombre, nuevo_apellido, nuevo_email):
        usuario = self.buscar_usuario_por_id(id_usuario)  # Buscamos al usuario
        if usuario:
            usuario.setNombre(nuevo_nombre)  # Actualizamos nombre
            usuario.setApellido(nuevo_apellido)  # Actualizamos apellido
            usuario.setEmail(nuevo_email)  # Actualizamos email
            self.guardar_en_json()  # Guardamos cambios
            return True  # Confirmamos modificación
        return False  # Si no existe el usuario

    # --- Búsquedas ---
    def buscar_usuario_por_id(self, id_usuario):
        for u in self.usuarios:  # Recorremos todos los usuarios
            if u.getId() == id_usuario:  # Si encontramos el ID
                return u  # Devolvemos el usuario
        return None  # Si no existe, devolvemos None

    def buscar_usuario_por_nombre(self, nombre):
        # Buscamos todos los usuarios cuyo nombre contenga el texto (ignorando mayúsculas/minúsculas)
        return [u for u in self.usuarios if nombre.lower() in u.getNombre().lower()]

    # --- Suspensiones ---
    def suspender_usuario(self, id_usuario, dias=7):
        usuario = self.buscar_usuario_por_id(id_usuario)  # Buscamos al usuario
        if usuario:
            usuario.setEstado("suspendido")  # Cambiamos estado a suspendido
            usuario.setSuspensionHasta(datetime.now() + timedelta(days=dias))  # Guardamos fecha de fin de suspensión
            self.guardar_en_json()  # Guardamos cambios
            return True  # Confirmamos suspensión
        return False  # Si no se encontró

    def reactivar_usuario(self, id_usuario):
        usuario = self.buscar_usuario_por_id(id_usuario)
        if usuario and usuario.getEstado() == "suspendido":
            usuario.setEstado("activo")  # Cambiamos a activo
            usuario.setSuspensionHasta(None)  # Quitamos la fecha de suspensión
            self.guardar_en_json()
            return True
        return False


    # --- JSON ---
    def guardar_en_json(self):
        lista_dicts = []  # Lista para guardar cada usuario como diccionario
        for u in self.usuarios:  # Recorremos usuarios
            lista_dicts.append({
                "id": u.getId(),  # Guardamos ID
                "nombre": u.getNombre(),  # Guardamos nombre
                "apellido": u.getApellido(),  # Guardamos apellido
                "email": u.getEmail(),  # Guardamos email
                "estado": u.getEstado(),  # Guardamos estado
                "suspension_hasta": u.getSuspensionHasta().isoformat() if u.getSuspensionHasta() else None  # Guardamos fecha como string ISO o None
            })
        # Abrimos/creamos archivo JSON y escribimos la lista de diccionarios
        with open("usuarios.json", "w", encoding="utf-8") as f:
            json.dump(lista_dicts, f, indent=4)  # indent=4 para que quede legible

    def cargar_desde_json(self):
        try:
            with open("usuarios.json", "r", encoding="utf-8") as f:  # Abrimos archivo en modo lectura
                lista_dicts = json.load(f)  # Convertimos JSON a lista de diccionarios
                for u_dict in lista_dicts:  # Recorremos cada usuario
                    u = Usuario(
                        u_dict["id"],  # ID
                        u_dict["nombre"],  # Nombre
                        u_dict["apellido"],  # Apellido
                        u_dict["email"]  # Email
                    )
                    u.setEstado(u_dict.get("estado", "activo"))  # Estado (por defecto activo)
                    suspension = u_dict.get("suspension_hasta")  # Fecha de suspensión
                    if suspension:
                        u.setSuspensionHasta(datetime.fromisoformat(suspension))  # Convertimos string ISO a datetime
                    self.usuarios.append(u)  # Agregamos a la lista interna
                # Actualizamos el próximo ID para no repetir
                if self.usuarios:
                    self._next_id = max(u.getId() for u in self.usuarios) + 1
        except FileNotFoundError:
            pass  # Si el archivo no existe, no hacemos nada
