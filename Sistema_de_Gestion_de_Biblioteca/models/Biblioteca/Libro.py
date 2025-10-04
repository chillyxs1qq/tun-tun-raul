# models/Biblioteca/Libro.py
from models.Biblioteca.Material import Material

class Libro(Material):
    def __init__(self, titulo, autor, anio, genero=None, correo=None):
        super().__init__("Libro", titulo, autor, anio)
        self.__genero = genero
        self.__correo = correo  # correo del usuario

    # Getters y Setters
    def getGenero(self):
        return self.__genero

    def setGenero(self, genero):
        self.__genero = genero

    def getCorreo(self):
        return self.__correo

    def setCorreo(self, correo):
        self.__correo = correo

    # __str__ mostrando género y correo
    def __str__(self):
        return f"[Libro] ID: {self.getId()}, Título: {self.getTitulo()}, Autor: {self.getAutor()}, Año: {self.getAnio()}, Género: {self.__genero}, Correo: {self.__correo}, Préstamo: {self.getPrestamohabilitado()}"
