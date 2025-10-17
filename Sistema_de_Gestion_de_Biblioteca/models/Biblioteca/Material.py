class Material:
    __contador = 0  # contador de IDs

    def __init__(self, tipo, titulo, autor, anio):
        Material.__contador += 1
        self.__id = self.__generarIDMa()
        self.__tipo = tipo
        self.__titulo = titulo
        self.__autor = autor
        self.__anio = anio
        self.__prestamohabilitado = True

    def __generarIDMa(self):
        return f"{self.__contador}"

    #Llamados:
    def getId(self):
        return self.__id  # <- Esto es lo que faltaba

    def getTipo(self):
        return self.__tipo

    def getTitulo(self):
        return self.__titulo

    def getAutor(self):
        return self.__autor

    def getAnio(self):
        return self.__anio

    def getPrestamohabilitado(self):
        return "Habilitado" if self.__prestamohabilitado else "Inhabilitado"

    # Modificador de atributos:
    def setTitulo(self, titulo):
        self.__titulo = titulo

    def setAutor(self, autor):
        self.__autor = autor

    def __str__(self):
        return f"[{self.__tipo}] ID: {self.__id}, Título: {self.__titulo}, Autor: {self.__autor}, Año: {self.__anio}, Préstamo: {self.getPrestamohabilitado()}"
