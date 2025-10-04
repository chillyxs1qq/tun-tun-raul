from models.Biblioteca.Material import Material

# Clase Libro que hereda de Material
class Libro(Material):
    def __init__(self, titulo, autor, anio, genero=None):
        # Usamos "Libro" como tipo y delegamos a Material
        super().__init__("Libro", titulo, autor, anio)
        self.__genero = genero  # campo extra solo para libros


    # Getter y Setter del género
    def getGenero(self):
        return self.__genero

    def setGenero(self, genero):
        self.__genero = genero

    # Sobreescribimos __str__ para mostrar también el género
    def __str__(self):
        estado = self.getPrestamohabilitado()
        return f"[Libro] ID: {self.getId()}, Título: {self.getTitulo()}, Autor: {self.getAutor()}, Año: {self.getAnio()}, Género: {self.__genero}, Préstamo: {estado}"
