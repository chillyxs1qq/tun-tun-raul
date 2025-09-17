from ..models.usuario import Usuario #importa la clase Usuario desde el archivo usuario.py que está en la carpeta models.
#( va a dar error porque no pusimos nada todavia en usuario py xD )
from datetime import datetime, timedelta #importa funciones de fechas y tiempos:

class UsuarioService:
    def __init__(self):
        self.usuarios = [] #crea una lista privada usuarios que guardará los objetos Usuario

    --- CRUD de usuarios ---
    def agregar_usuario(self, id_usuario, nombre):
        if self.buscar_usuario_por_id(id_usuario): #si ya existe un usuario con ese ID devuelve un mensaje de error y no lo agrega
            return False  # ya existe
        nuevo = Usuario(id_usuario, nombre)
        self.usuarios.append(nuevo)
        return True

    def eliminar_usuario(self, id_usuario):
        usuario = self.buscar_usuario_por_id(id_usuario)
        if usuario:
            self.usuarios.remove(usuario)
            return True
        return False

    def modificar_usuario(self, id_usuario, nuevo_nombre):
        usuario = self.buscar_usuario_por_id(id_usuario)
        if usuario:
            usuario.setNombre(nuevo_nombre)
            return True
        return False

    # --- Búsquedas ---
    def buscar_usuario_por_id(self, id_usuario): #recorre la lista de usuarios y devuelve el que tenga ese ID. Si no encuentra ninguno, devuelve None
        for u in self.usuarios:
            if u.getId() == id_usuario:
                return u
        return None

    def buscar_usuario_por_nombre(self, nombre): #devuelve una lista de usuarios cuyo nombre contenga el texto buscado (ignorando mayúsculas/minúsculas)
        return [u for u in self.usuarios if nombre.lower() in u.getNombre().lower()]

    # --- Suspensiones ---
    def suspender_usuario(self, id_usuario, dias=7): #suspende a un usuario por un número de días (7 puse ese pero se puede cambiar xd)
        usuario = self.buscar_usuario_por_id(id_usuario)
        if usuario:
            usuario.setEstado("suspendido") #Cambia su estado a "suspendido"
            usuario.setSuspensionHasta(datetime.now() + timedelta(days=dias)) #guarda la fecha en que termina la suspensión (hoy + días)
            return True # esto lo puedo cambiar y poner un mensaje de que no se encontr o algo
        return False

    def reactivar_usuario(self, id_usuario): #metodo para reactivar un usuario suspendido
        usuario = self.buscar_usuario_por_id(id_usuario)
        if usuario and usuario.getEstado() == "suspendido": #busca al usuario y comprueba que esté suspendido
            if usuario.getSuspensionHasta() and usuario.getSuspensionHasta() <= datetime.now(): #Si la suspensión ya terminó (la fecha es menor o igual a hoy)
                usuario.setEstado("activo we") #cambia estado a "activo we"
                usuario.setSuspensionHasta(None) #borra la fecha de suspensión aunque podriamos dejar un registro, despues vemos eso
                return True #puedo poner un mensaje de que ya fue reactivado o algo o otro return de que no lo encontro
        return False
