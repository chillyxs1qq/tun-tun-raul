class Material:
    def __init__(self,  idmaterial, tipo, titulo, autor, anio, plazo):
        self.__idmaterial = idmaterial
        self.__tipo = tipo
        self.__titulo = titulo
        self.__autor = autor
        self.__anio = anio
        self.__ejemplarestotales = 0
        self.__ejemplaresdisp = 0
        self.__plazoprestamo = plazo
        self.__prestamohabilitado = False

# Metodos get
    def getPlazoPrestamo(self):
        return self.__plazoprestamo

    def getInfo(self):
        if self.__prestamohabilitado is True:
             hab = "Prestamo habilitado"
        else:
            hab = "Prestamo no habilitado"
        return f"[Info-{self.__tipo}] Titulo: {self.__titulo}, Autor: {self.__autor}, Año: {self.__anio}, {hab}"

    def getEjemplaresTotales(self):
        return self.__ejemplarestotales

    def getEjemplaresDisp(self):
        return self.__ejemplaresdisp

    def getEstado(self):
        return self.__prestamohabilitado

# Metodos set (modificadores)

    def setTitulo(self, titulo):
        self.__titulo = titulo

    def setAutor(self, autor):
        self.__autor = autor

    def setPlazo(self, plazo):
        self.__plazoprestamo = plazo

    def setEjemplaresDisp(self, ejemplaresdisp):
        self.__ejemplaresdisp = ejemplaresdisp

    def setEjemplaresTotales(self, ejemplarestotales):
        self.__ejemplarestotales = ejemplarestotales

    '''def plazoPrestamo(self, plazo):
        self.__plazoprestamo = plazo
        return f"Plazo de prestamo asignado en [{self.__plazoprestamo}] dias"

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
            return "El material con el ID especificado no se encuentra o no existe."'''