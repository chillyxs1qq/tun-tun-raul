from Sistema_de_Gestion_de_Biblioteca.models.Biblioteca.Libro import Libro

class Material:
    def __init__(self, idmaterial, titulo, autor, anio):
        self.__idmaterial = idmaterial
        self.__titulo = titulo
        self.__autor = autor
        self.__anio = anio
        self.__ejemplarestotales = ejemplarestotales
        self.__ejemplaresdisp = ejemplaresdisp
        self.__plazoprestamo = plazo
        self.__prestamohabilitado = prestamohabilitado

    def plazoPrestamo(self):
        return self.__plazoprestamo

    def puedePrestar(self):
        if self.__ejemplarestotales > 0:
            print(f"{self.__titulo} se puede prestar, ejemplares disponibles: {self.__ejemplaresdisp}.")
            self.__prestamohabilitado = True
        else:
            print("No hay ejemplares disponibles para prestar.")
            self.__prestamohabilitado = False

    def retirarEjemplar(self, idmaterial):
        if idmaterial == self.__idmaterial:
            self.__ejemplaresdisp -= 1
            return "Ejemplar retirado"
        else:
            return "El material con el ID especificado no se encuentra disponible o no existe."

    def devolverEjemplar(self, idmaterial):
        if idmaterial == self.__idmaterial:
            self.__ejemplaresdisp += 1
            return "Ejemplar devuelto."
        else:
            return "El material con el ID especificado no se encuentra o no existe."