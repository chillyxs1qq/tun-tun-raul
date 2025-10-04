class Libro:
    __contador = 0

    def __init__(self, titulo, autor, anio, genero=None):
        Libro.__contador += 1
        self.id = f"IDMA{Libro.__contador:04d}"
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.genero = genero
        self.prestamohabilitado = True

    # --- getters ---
    def getId(self):
        return self.id

    def getTitulo(self):
        return self.titulo

    def getAutor(self):
        return self.autor

    def getAnio(self):
        return self.anio

    def getGenero(self):
        return self.genero

    def getPrestamohabilitado(self):
        return "Habilitado" if self.prestamohabilitado else "Inhabilitado"

    # --- setters ---
    def setTitulo(self, nuevo_titulo):
        self.titulo = nuevo_titulo

    def setAutor(self, nuevo_autor):
        self.autor = nuevo_autor

    def setAnio(self, nuevo_anio):
        self.anio = nuevo_anio

    def setGenero(self, nuevo_genero):
        self.genero = nuevo_genero

    def setPrestamohabilitado(self, estado):
        self.prestamohabilitado = estado

    # --- string ---
    def __str__(self):
        return f"[Libro] ID: {self.id}, Título: {self.titulo}, Autor: {self.autor}, Año: {self.anio}, Género: {self.genero}, Préstamo: {self.getPrestamohabilitado()}"
