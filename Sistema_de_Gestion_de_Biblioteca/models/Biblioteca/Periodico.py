class Libro:
    def __init__(self, plazoprestamo):
        self.__plazoprestamo = plazoprestamo

    def plazoPrestamo(self, plazo):
        plazo = int(input("Ingrese el plazo del prestamo en días"))
        self.__plazoprestamo = plazo