import re

class Socio:
    #Con este metodo de clase cada vez que se cree un socio se guarde en la biblioteca.
    @classmethod
    def set_biblioteca(cls, biblioteca):
        cls.__biblioteca = biblioteca

    __biblioteca = None
    __contador = 0

    #Diccionario para almacenar todos los socios.
    __socios = {}

    #Metodo de clase para buscar un Socio por su ID.
    @classmethod
    def buscarID(cls, id_socio):
        return cls.__socios.get(id_socio)

    def __init__(self, nombre, estado = "Activo", email = None):

        #Si el nombre esta vacío, salta un error.
        if not nombre or not nombre.strip():
            raise ValueError("El nombre del Socio no puede estar vacío")
        self.__nombre = nombre.strip()

        #Por defecto los recién registrados tienen como estado "Activos"
        self.__estado = estado

        #Genera un ID de Socio cada vez que se registra un nuevo Socio.
        self.__IDSocio = self.__generarID()

        #Guarda la información del Socio en el diccionario.
        self.__socios[self.__IDSocio] = self

        self.__email = email.lower()

    #Genera un ID cuando se registra un nuevo nombre
    def __generarID(self):
        Socio.__contador += 1
        return f"SC{self.__contador:04d}"

    #@staticmethod sirve para hacer un metodo de clase que no necesite ni instancias (self) Ni a la clase (cls).
    @staticmethod
    def __email_Valido(email):
        i =  r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(i, email))

    #Propiedad de la clase para dar bien los nombres de las instancias cuando se lo requiere.
    @property
    def nombre(self):
        return self.__nombre
    @property
    def estado(self):
        return self.__estado
    @property
    def IDSocio(self):
        return self.__IDSocio
    @property
    def email(self):
        return self.__email

    #Esta parte no es importante, solo está para poder llamar a la instancia de clase y que muestre toda la información en orden.
    def __str__(self):
        return f"|{self.__IDSocio}: {self.__nombre}|Estado: {self.__estado}|Email: {self.__email}"