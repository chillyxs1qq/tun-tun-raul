from Socio import Socio
from datetime import date, datetime, timedelta

class Prestamo:

    #Diccionario de Préstamos:
    __Prestamos = {}

    #Contador de préstamos:
    __prestamos = 0


    def __init__(self, SocioID, IDMaterial, estado = "Vigente"):

        #El ID de los préstamos se crean automáticamente cada vez que se registra un nuevo Prestamo.
        self.__IDPrestamo = self.__generarIDPrestamo()

        #Los préstamos que se realicen se guardan en el diccionario de préstamos
        self.__Prestamos[self.__IDPrestamo] = self

        #Acepta tanto un objeto Socio como un ID de Socio.
        if isinstance(SocioID, Socio):
            self.__Socio = SocioID
        else:
            #Si es un ID, busca al Socio correspondiente.
            self.__Socio = Socio.buscarID(SocioID)
            if self.__Socio is None:
                raise ValueError(f"No hay un Socio con el ID: {SocioID}")

        self.__IDMaterial = IDMaterial

        self.__estado = estado

        #Utilizamos la biblioteca datetime para que cuando se haga un prestamo automáticamente se ponga la fecha actual.
        #Las especificación .now() sirve para que me de la fecha actual. Y .date() para quitar horas, minutos y segundo.
        self.__fechaPrestamo = datetime.now().date()

        #Con timedelta podemos especificar una cantidad de días en específico y sumarlo a la actual.
        #Fecha de vencimiento se crea automáticamente sumando una cantidad de días específica para devolver el prestamo.
        self.__fechaVencimiento = self.__fechaPrestamo + timedelta(days=7)

    @property
    def IDSocio(self):
        return self.__Socio.IDSocio

    @property
    def Socio(self):
        return self.__Socio

    def __generarIDPrestamo(self):
        Prestamo.__prestamos += 1
        return f"PR{self.__prestamos:04d}"

    def __str__(self):
        return f"|Prestamo: {self.__IDPrestamo}|Socio: {self.IDSocio}|Fecha del prestamo: {self.__fechaPrestamo}|Fecha de vencimiento: {self.__fechaVencimiento}|Estado: {self.__estado}|"

# Crear un socio
socio = Socio("mogolico1", "Activo", "0902Matheo@gmail.com")

# Crear un préstamo usando el ID del socio
id_socio = socio.IDSocio
prestamo1 = Prestamo( id_socio, "M002")

# Obtener toda la información del socio
print(prestamo1) # Mostrará todos los datos del socio

#Mostramos la información del Socio
print(socio)
