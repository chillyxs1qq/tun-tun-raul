#Estudiantes
import re
import random

#Esta biblioteca arregla el problema de Circulación de Importación
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Prestamo import Prestamo


class Estudiante:
    #Con este metodo de clase cada vez que se cree un Estudiante se guarde en la biblioteca.
    @classmethod
    def set_biblioteca(cls, biblioteca):
        cls.__biblioteca = biblioteca

    __biblioteca = None
    __contador = 0

    #Diccionario para almacenar todos los Estudiantes.
    __estudiantes = {}

    #Metodo de clase para buscar un Estudiante por su ID.
    @classmethod
    def buscarID(cls, id_estudiante):
        return cls.__estudiantes.get(id_estudiante)

    def __init__(self, nombre, estado = "Activo", email = None):

        #Si el nombre esta vacío, salta un error.
        if not nombre or nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacío")
        else:
            self.__nombre = nombre.strip()

        #Por defecto los recién registrados tienen como estado "Activos"
        self.__estado = estado.strip()

        #Genera un ID de Estudiante cada vez que se registra un nuevo Estudiante.
        self.__IDEstudiante = self.__generarID()

        #Guarda la información del Estudiante en el diccionario.
        self.__estudiantes[self.__IDEstudiante] = self

        #Condiciones para el Email.
        if email is None or email.strip() == "": #En el caso de que el Email este vacío.
            self.__email = None #Se Guardara como Email nulo.
        else:
            email = email.lower()
            if not self.__email_Valido(email): #De lo contrario deber seguir las reglas establecidas por el metodo estatico o saltara un error.
                raise ValueError("El formato del email no es valido")
            self.__email = email.strip()

    #Genera un ID cuando se registra un nuevo nombre
    def __generarID(self):
        Estudiante.__contador += 1
        #Genera 3 números aleatorios entre 0 y 999
        num_aleatorio = random.randint(1, 9999)
        return f"ES{num_aleatorio:04d}{self.__contador:01d}"

    #Sistema de Suspension para los Estudiantes
    @property
    def SuspendidoHasta(self):
        if self.__estado == "Suspendido":
            #Importación local para evitar la circulación de importación
            from Prestamo import Prestamo

            #Esta parte lo que hace es, ir al diccionario e ir uno por uno los préstamos realizados.
            #Toma un prestamo realizado y luego pregunta si dicho prestamo está afiliado a un ID de un Estudiante, y después pregunta si el Prestamo está Vencido.
            prestamos_vencidos = [p for p in Prestamo._Prestamo__Prestamos.values() if p.IDEstudiante == self.__IDEstudiante and p.estado == "Vencido"]

            #Si el prestamo está vencido genera que el Estudiante sea suspendido por un tiempo.
            if prestamos_vencidos:
                prestamos_mas_reciente = max(prestamos_vencidos, key = lambda p: p.fechaVencimiento)

                #Los días suspendido dependeran de cuantos días el Estudiante se demoró en devolver el prestamo.
                dias_suspension = prestamos_mas_reciente.dias_de_retraso
                return f"El Estudiante esta suspendido por {dias_suspension} días"
        return None

    #@staticmethod sirve para hacer un metodo de clase que no necesite ni instancias (self) Ni a la clase (cls).
    @staticmethod
    def __email_Valido(email):
        i =  r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(i, email))

    #Propiedad de la clase, para dar bien los nombres de las instancias cuando se lo requiere.
    @property
    def nombre(self):
        return self.__nombre
    @property
    def estado(self):
        return self.__estado
    @property
    def IDEstudiante(self):
        return self.__IDEstudiante
    @property
    def email(self):
        return self.__email

    #Esta parte no es importante, solo está para poder llamar a la instancia de clase y que muestre toda la información en orden.
    def __str__(self):
        email_str = f"Email: {self.__email}" if self.__email else ""
        if self.__estado == "Activo":
            return f"Estudiante_:|{self.__IDEstudiante}: {self.__nombre}|Estado: {self.__estado}|{email_str}|"
        else:
            return f"|{self.__IDEstudiante}: {self.__nombre}|Estado: {self.__estado}|Suspendido Hasta: {self.SuspendidoHasta}|{email_str}|"