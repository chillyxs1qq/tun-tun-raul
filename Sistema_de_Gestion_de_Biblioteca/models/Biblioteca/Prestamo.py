#Prestamos
from Estudiante import Estudiante
from Material import Material
from datetime import date, datetime, timedelta
import random

class Prestamo:

    #Diccionario de Préstamos:
    __Prestamos = {}

    #Contador de préstamos:
    __prestamos = 0


    def __init__(self, EstudianteID, IDMaterial, estado = "Vigente"):

        #El ID de los préstamos se crean automáticamente cada vez que se registra un nuevo Prestamo.
        self.__IDPrestamo = self.__generarIDPrestamo()

        #Los préstamos que se realicen se guardan en el diccionario de préstamos
        self.__Prestamos[self.__IDPrestamo] = self

        #Acepta tanto un objeto Estudiante como un ID de Estudiante.
        #isinstance comprueba que EstudianteID sea un instancia de clase de Estudiante.
        if isinstance(EstudianteID, Estudiante):
            self.__Estudiante = EstudianteID
        else:
            #Si es un ID, busca al Estudiante correspondiente.
            self.__Estudiante = Estudiante.buscarID(EstudianteID)
            if self.__Estudiante is None:
                raise ValueError(f"No hay un Estudiante con el ID: {EstudianteID}")

        if self.__Estudiante.estado == "Suspendido":
            raise ValueError(f"No se puede realizar el préstamo. El Estudiante {self.__Estudiante.nombre} está Suspendido.")

        self.__IDMaterial = IDMaterial

        self.__estado = estado

        #Utilizamos la biblioteca datetime para que cuando se haga un prestamo automáticamente se ponga la fecha actual.
        #Las especificación .now() sirve para que me de la fecha actual. Y .date() para quitar horas, minutos y segundo.
        self.__fechaPrestamo = datetime.now().date()

        #Con timedelta podemos especificar una cantidad de días en específico y sumarlo a la actual.
        #Fecha de vencimiento se crea automáticamente sumando una cantidad de días específica para devolver el prestamo.
        self.__fechaVencimiento = self.__fechaPrestamo + timedelta(days=7)

    @property
    def IDEstudiante(self):
        return self.Estudiante.__IDEstudiante

    @property
    def get_estudiante(self):
        return self.__Estudiante

    def __generarIDPrestamo(self):
        num_aleatorio = random.randint(0,9999)
        Prestamo.__prestamos += 1
        return f"PR{num_aleatorio:04d}{self.__prestamos:01d}"

    #Sistema de Suspension
    def Sistema_suspencion(self):
        fecha_actual = datetime.now().date()
        #Si el prestamo está vigente y la fecha actual es posterior a la fecha de vencimiento
        if self.__estado == "Vigente" and fecha_actual > self.__fechaVencimiento:
            #Calculamos los días de retraso
            dias_retraso = (fecha_actual - self.__fechaVencimiento).days

            #Cambiamos el estado del prestamo a "Vencido"
            self.__estado = "Vencido"

            if dias_retraso > 0:
                #Accedemos al estado del Estudiante y los cambiamos a Suspendido
                self.__Estudiante._Estudiante__estado = "Suspendido"
                return f"Alerta: El Estudiante {self.__Estudiante.nombre} esta suspendido por un retraso de {dias_retraso} días en la devolución del material"
        return None

    def __str__(self):
        return f"|Prestamo: {self.__IDPrestamo}|Estudiante: {self.IDEstudiante}|Fecha del prestamo: {self.__fechaPrestamo}|Fecha de vencimiento: {self.__fechaVencimiento}|Estado: {self.__estado}|"

    @property
    def estado(self):
        return self.__estado
    @property
    def fechaVencimiento(self):
        return self.__fechaVencimiento
    @property
    def dias_de_retraso(self):
        fecha_actual = datetime.now().date()
        if fecha_actual > self.__fechaVencimiento:
            return (fecha_actual - self.__fechaVencimiento).days
        return 0