import re
from datetime import datetime, timedelta

class Usuario:
    __usuarios = {}  # Diccionario interno de usuarios
    __contador = 0   # Contador para generar IDs únicos

    def __init__(self, nombre, apellido, email, estado="activo"):
        if not nombre or nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombre = nombre.strip()

        if not apellido or apellido.strip() == "":
            raise ValueError("El apellido no puede estar vacío.")
        self.__apellido = apellido.strip()

        self.__estado = estado.lower()
        self.__suspension_hasta = None

        # Generar ID automático
        Usuario.__contador += 1
        self.__id = Usuario.__contador

        # Validar email
        if email is not None and self.__email_valido(email):
            self.__email = email.strip()
        else:
            self.__email = None

        # Guardar en diccionario
        Usuario.__usuarios[self.__id] = self

    # --- GETTERS / SETTERS ---
    def getId(self):
        return self.__id

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        if nombre.strip():
            self.__nombre = nombre.strip()

    def getApellido(self):
        return self.__apellido

    def setApellido(self, apellido):
        if apellido.strip():
            self.__apellido = apellido.strip()

    def getEmail(self):
        return self.__email

    def setEmail(self, email):
        if email and self.__email_valido(email):
            self.__email = email.strip()

    def getEstado(self):
        return self.__estado

    def setEstado(self, estado):
        self.__estado = estado.lower()

    def getSuspensionHasta(self):
        return self.__suspension_hasta

    def setSuspensionHasta(self, fecha):
        self.__suspension_hasta = fecha

    # --- MÉTODOS DE CLASE ---
    @classmethod
    def buscar_por_id(cls, id_usuario):
        return cls.__usuarios.get(int(id_usuario))

    @classmethod
    def listar_usuarios(cls):
        return list(cls.__usuarios.values())

    @classmethod
    def actualizar_contador(cls, valor):
        """Actualizar el contador si se cargan IDs desde JSON"""
        cls.__contador = max(cls.__contador, valor)

    # --- VALIDACIÓN DE EMAIL ---
    @staticmethod
    def __email_valido(email):
        regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(regex, email))

    # --- REPRESENTACIÓN ---
    def __str__(self):
        email_str = f"Email: {self.__email}" if self.__email else ""
        if self.__estado == "activo":
            return f"|{self.__id}: {self.__nombre} {self.__apellido}|Estado: {self.__estado}|{email_str}|"
        else:
            fecha_str = self.__suspension_hasta.strftime("%Y-%m-%d") if self.__suspension_hasta else "Desconocida"
            return f"|{self.__id}: {self.__nombre} {self.__apellido}|Estado: {self.__estado}|Suspendido hasta: {fecha_str}|{email_str}|"
