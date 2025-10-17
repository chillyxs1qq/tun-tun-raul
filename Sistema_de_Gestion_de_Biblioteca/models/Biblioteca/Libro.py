from ...services.Cola import Cola


class Libro:
    __contador = 0

    def __init__(self, titulo, autor, anio, genero=None):
        Libro.__contador += 1
        self.id = str(Libro.__contador)
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.genero = genero
        self.prestamohabilitado = True
        self.cola_espera = Cola()  # Cola de usuarios esperando el libro

    #Metodos para mostrar los atributos:
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

    def verCola(self):
        return self.cola_espera.toLista()

    #Modificadores Atributos:
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

    #Metodos de cola:
    def encolar_usuario(self, id_usuario):
        if not self.cola_espera.contiene(id_usuario):
            self.cola_espera.encolar(id_usuario)

    def desencolar_usuario(self):
        if not self.cola_espera.estaVacia():
            return self.cola_espera.desencolar()
        return None

    def retirar_usuario(self, id_usuario):
        lista = self.cola_espera.toLista()
        if id_usuario in lista:
            lista.remove(id_usuario)
            self.cola_espera.limpiar()
            for uid in lista:
                self.cola_espera.encolar(uid)
            return True
        return False

    # Metodo para añadirlo al JSON
    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "autor": self.autor,
            "anio": self.anio,
            "genero": self.genero,
            "prestamohabilitado": self.prestamohabilitado,
            "cola_espera": self.verCola()
        }

    def cargar_cola(self, lista_ids):
        self.cola_espera.limpiar()
        for uid in lista_ids:
            self.cola_espera.encolar(uid)

    def __str__(self):
        return f"[Libro] ID: {self.id}, Título: {self.titulo}, Autor: {self.autor}, Año: {self.anio}, Género: {self.genero}, Préstamo: {self.getPrestamohabilitado()}, En espera: {self.verCola()}"
