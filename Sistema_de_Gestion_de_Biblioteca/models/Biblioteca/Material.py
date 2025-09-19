# Se crea la clase material que será la base para agregar Libros/Revistas/ETC...
class Material:
    __contador = 0
    def __init__(self, tipo, titulo, autor, anio, plazo):
        self.__idmaterial = self.__generarIDMa() # Este ID deberá generarse automáticamente y será unico para cada material
        self.__tipo = tipo # Necesario indicar el tipo antes de crear para saber si es Libro u otro tipo de material
        self.__titulo = titulo # Pues aca va el título bro que esperabas
        self.__autor = autor
        self.__anio = anio
        self.__ejemplarestotales = 0 #Ejemplares totales se declara 0 acá en el codigo, pero después hay q ver como calcular
        self.__ejemplaresdisp = 0 #La cantidad de ejemplares que están disponibles para prestar
        self.__plazoprestamo = plazo #El plazo deberá indicarse en dias
        self.__prestamohabilitado = False #La habilitación se declara False pero luego hay que modificar al crear

    #Genera un ID automatico cuando se crea una instancia de Material
    def __generarIDMa(self):
        return f"IDMA{self.__contador:04d}"

    # Metodos get
    def getPlazoPrestamo(self):
        return self.__plazoprestamo #Este metodo sirve para ver cual es el plazo establecido para el material indicado
    #Este metodo podría ser eliminado en proximas versiones dependiendo de como hagamos la función del plazo

    def getInfo(self):
        if self.__prestamohabilitado is True:
            hab = "Prestamo habilitado"
        else:
            hab = "Prestamo no habilitado"
        return f"[Info-{self.__tipo}] Titulo: {self.__titulo}, Autor: {self.__autor}, Año: {self.__anio}, {hab}"
    #Este metodo sirve para ver en pantalla la información del material, y el IF lo que hace es cambiar el
    #Valor de la ultima variable para saber si está o no habilitado su prestamo

    def getEjemplaresTotales(self):
        return self.__ejemplarestotales
    #Este metodo es para ver los ejemplares totales existentes de un material indicado
    #De momento no funciona ya que no está creada la funcion para acumular los materiales

    def getEjemplaresDisp(self):
        return self.__ejemplaresdisp
    #Este es como el anterior pero en lugar de mostrarte todos los ejemplares, solom muestra los disponibles

    def getEstado(self):
        return self.__prestamohabilitado
    #Este metodo devuelve si el material tiene o no el prestamo habilitado con True o False

    # Metodos set (modificadores)

    def setTitulo(self, titulo):
        self.__titulo = titulo
    #Este metodo sirve para cambiar el titulo de un material

    def setAutor(self, autor):
        self.__autor = autor
    #Lo mismo que el anterior pero para el Autor

    def setPlazo(self, plazo):
        self.__plazoprestamo = plazo
    #Este sirve para modificar el plazo de prestamo de un material (posiblemente lo borre)

    def setEjemplaresDisp(self, ejemplaresdisp): #Este es solo para pruebas
        self.__ejemplaresdisp = ejemplaresdisp


    def setEjemplaresTotales(self, ejemplarestotales): #Este es solo para pruebas
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