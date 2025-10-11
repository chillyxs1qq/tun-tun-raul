import re
from datetime import datetime, timedelta

class Usuario:
    __usuarios = {}  # Diccionario interno de usuarios
    __contador = 0   # Contador para generar IDs únicos

    def __init__(self, nombre, apellido, email, estado="activo"):
        if not nombre.strip() or not apellido.strip():
            raise ValueError("Nombre y apellido no pueden estar vacíos.")

        self.__nombre = nombre.strip()
        self.__apellido = apellido.strip()
        self.__estado = estado.lower()
        self.__suspension_hasta = None

        # Generar ID automático
        Usuario.__contador += 1
        self.__id = Usuario.__contador

        # Validar email
        if email and not self.__email_valido(email):
            raise ValueError("Formato de email inválido.")
        self.__email = email.strip() if email else None

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

    # --- VALIDACIÓN DE EMAIL ---
    @staticmethod
    def __email_valido(email):
        regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(regex, email))

    # --- REPRESENTACIÓN ---
    def __str__(self):
        suspension_str = f"|Suspendido hasta: {self.__suspension_hasta}" if self.__estado == "suspendido" and self.__suspension_hasta else ""
        email_str = f"|Email: {self.__email}" if self.__email else ""
        return f"ID: {self.__id} | {self.__nombre} {self.__apellido} | Estado: {self.__estado}{suspension_str}{email_str}"
