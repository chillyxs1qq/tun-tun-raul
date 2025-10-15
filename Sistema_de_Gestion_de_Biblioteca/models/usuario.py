import re
from datetime import datetime, timedelta

class Usuario:
    __usuarios = {}  # Diccionario interno de usuarios
    __contador = 0   # Contador para generar IDs únicos

    def __init__(self, nombre, apellido, email, estado="activo"):
        if not nombre or nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacío.")
        else:
            self.__nombre = nombre.strip()

        if not apellido or apellido.strip() == "":
            raise ValueError("El apellido no puede estar vacío.")
        else:
            self.__apellido = apellido.strip()
        #Por defecto Activo.
        self.__estado = estado.lower()

        #Si no tiene préstamos vencido este atributo no cambia, por defecto None.
        self.__suspension_hasta = None

        # Generar ID automático cada vez que se crea una instancía de clase.
        Usuario.__contador += 1
        self.__id = f"ES{Usuario.__contador:02d}"

        # Validar email según el formato establecido, de lo contrario puede ser None.
        if email is not None:
            self.__email = email.strip()
            if not self.__email_valido(email):
                raise ValueError("El formato del Email no es Valido.")
            self.email = email
        else:
            self.email = None

        #Guardar el usuario por su ID en el diccionario
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
        return self.__suspension_hasta.date

    def setSuspensionHasta(self, fecha):
        self.__suspension_hasta.date = fecha

    # --- MÉTODOS DE CLASE ---
    @classmethod
    #Metodo de clase, no depende de la instancía, guarda a los usuarios por su ID en una lista que luego podemos llamar para corroborar la existencia de dicho usuario.
    def buscar_por_id(cls, id_usuario):
        return cls.__usuarios.get(int(id_usuario))

    @classmethod
    #Metodo de clase, no depende de la instancía, guarda cada instancía de la clase en una lista que luego podemos llamar.
    def listar_usuarios(cls):
        return list(cls.__usuarios.values())

    # --- VALIDACIÓN DE EMAIL ---
    #Si el usuario quiere poner su Email, el Email debe cumplir cierto formato.
    @staticmethod
    def __email_valido(email):
        regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(regex, email))

    # --- REPRESENTACIÓN ---
    #Como se guarda/muestra la información de usuario en JSON.
    def __str__(self):
        email_str = f"Email: {self.__email}" if self.__email else ""
        if self.__estado == "activo":
            return f"Estudiante_:|{self.__id}: {self.__nombre}|Estado: {self.__estado}|{email_str}|"
        else:
            return f"|{self.__id}: {self.__nombre}|Estado: {self.__estado}|Suspendido Hasta: {self.__suspension_hasta}|{email_str}|"

