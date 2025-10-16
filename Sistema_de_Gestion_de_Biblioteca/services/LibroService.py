import json
from Sistema_de_Gestion_de_Biblioteca.models.Biblioteca.Libro import Libro
from Sistema_de_Gestion_de_Biblioteca.utils.validation import validar_titulo, validar_autor, validar_anio

class LibroService:
    def __init__(self):
        self.libros = []
        self.cargar_desde_json()

    # --- CRUD ---

    def agregar_libro(self, titulo, autor, anio, genero=None):
        titulo = validar_titulo(titulo)
        autor = validar_autor(autor)
        anio = validar_anio(anio)
        libro = Libro(titulo, autor, anio, genero=genero)
        self.libros.append(libro)
        self.guardar_en_json()
        return libro

    def eliminar_libro(self, id_libro):
        libro = self.buscar_por_id(id_libro)
        if libro:
            self.libros.remove(libro)
            self.guardar_en_json()
            return True
        return False

    def modificar_libro(self, id_libro, nuevo_titulo, nuevo_autor, nuevo_anio, nuevo_genero):
        libro = self.buscar_por_id(id_libro)
        if libro:
            libro.setTitulo(validar_titulo(nuevo_titulo))
            libro.setAutor(validar_autor(nuevo_autor))
            libro.setAnio(validar_anio(nuevo_anio))
            libro.setGenero(nuevo_genero)
            self.guardar_en_json()
            return True
        return False

    def buscar_por_id(self, id_libro):
        id_libro = id_libro.upper()
        for l in self.libros:
            if l.getId().upper() == id_libro:
                return l
        return None

    def buscar_por_titulo(self, titulo):
        titulo = titulo.strip().lower()
        return [l for l in self.libros if titulo in l.getTitulo().strip().lower()]

    def buscar_por_autor(self, autor):
        autor = autor.strip().lower()
        return [l for l in self.libros if autor in l.getAutor().strip().lower()]

    # --- NUEVO MÉTODO REQUERIDO ---
    def listar_libros(self):
        """
        Devuelve la lista completa de libros.
        Este método es utilizado por PrestamoService.
        """
        return self.libros

    # --- JSON ---

    def guardar_en_json(self):
        lista_dicts = []
        for l in self.libros:
            lista_dicts.append({
                "id": l.getId(),
                "titulo": l.getTitulo(),
                "autor": l.getAutor(),
                "anio": l.getAnio(),
                "genero": l.getGenero(),
                "prestamo": l.getPrestamohabilitado()
            })
        with open("data/libros.json", "w", encoding="utf-8") as f:
            json.dump(lista_dicts, f, indent=4, ensure_ascii=False)

    def cargar_desde_json(self):
        try:
            with open("data/libros.json", "r", encoding="utf-8") as f:
                lista_dicts = json.load(f)
                for d in lista_dicts:
                    libro = Libro(d["titulo"], d["autor"], d["anio"], genero=d.get("genero"))
                    self.libros.append(libro)
        except FileNotFoundError:
            pass
