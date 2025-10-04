# Se crea la clase material que será la base para agregar Libros/Revistas/ETC...
class Material:
    __contador = 0
    def __init__(self, tipo, titulo, autor, anio):
        self.__id = self.__generarIDMa() # Este ID deberá generarse automáticamente y será unico para cada material
        self.__tipo = tipo # Necesario indicar el tipo antes de crear para saber si es Libro u otro tipo de material
        self.__titulo = titulo # Pues aca va el título bro que esperabas
        self.__autor = autor
        self.__anio = anio
        self.__prestamohabilitado = True #La habilitación se declara False pero luego hay que modificar al crear

    #Genera un ID automatico cuando se crea una instancia de Material
    def __generarIDMa(self):
        return f"IDMA{self.__contador:04d}"

    # Gets
    def getTitulo(self):
        return self.__titulo

    def getAutor(self):
        return self.__autor

    def getAnio(self):
        return self.__anio

    def getPrestamohabilitado(self):
        if self.__prestamohabilitado == True:
            estado = "Habilitado"
        else:
            estado = "Inhabilitado"
        return f"{estado}"


    # Sets

    def setTitulo(self, titulo):
        self.__titulo = titulo #Este metodo sirve para cambiar el titulo de un material

    def setAutor(self, autor):
        self.__autor = autor    #Lo mismo que el anterior pero para el Autor

    # Metodos

    def __str__(self):
        if self.__prestamohabilitado == True:
            estado = "Habilitado"
        else:
            estado = "Inhabilitado"
        return f"[{self.__tipo}] Titulo: {self.__titulo}, Autor: {self.__autor}, Anio: {self.__anio}, Prestamo: {estado}"
    #Este metodo sirve para ver en pantalla la información del material, y el IF lo que hace es cambiar el Valor de la ultima variable para saber si está o no habilitado su prestamo