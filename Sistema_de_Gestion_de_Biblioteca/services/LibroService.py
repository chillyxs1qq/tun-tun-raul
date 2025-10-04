# services/LibroService.py
import json
from models.Biblioteca.Libro import Libro
from utils.validation import validar_correo, validar_titulo, validar_autor, validar_anio

class LibroService:
    def __init__(self):
        self.libros = []
        self.cargar_desde_json()

    # --- CRUD ---
    def agregar_libro(self, titulo, autor, anio, genero=None, correo=None):
        # Validaciones
        titulo = validar_titulo(titulo)
        autor = validar_autor(autor)
        anio = validar_anio(anio)
        if correo:
            correo = validar_correo(correo)

        libro = Libro(titulo, autor, anio, genero=genero, correo=correo)
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

    def modificar_libro(self, id_libro, nuevo_titulo, nuevo_autor, nuevo_anio, nuevo_genero, nuevo_correo=None):
        libro = self.buscar_por_id(id_libro)
        if libro:
            # Validaciones
            nuevo_titulo = validar_titulo(nuevo_titulo)
            nuevo_autor = validar_autor(nuevo_autor)
            nuevo_anio = validar_anio(nuevo_anio)
            if nuevo_correo:
                nuevo_correo = validar_correo(nuevo_correo)

            libro.setTitulo(nuevo_titulo)
            libro.setAutor(nuevo_autor)
            libro.setGenero(nuevo_genero)
            libro.setCorreo(nuevo_correo)
            self.guardar_en_json()
            return True
        return False

    # --- Búsquedas ---
    def buscar_por_id(self, id_libro):
        for l in self.libros:
            if l.getId() == id_libro:
                return l
        return None

    def buscar_por_titulo(self, titulo):
        return [l for l in self.libros if titulo.lower() in l.getTitulo().lower()]

    def buscar_por_autor(self, autor):
        return [l for l in self.libros if autor.lower() in l.getAutor().lower()]

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
                "correo": l.getCorreo(),
                "prestamo": l.getPrestamohabilitado()
            })
        with open("libros.json", "w", encoding="utf-8") as f:
            json.dump(lista_dicts, f, indent=4)

    def cargar_desde_json(self):
        try:
            with open("libros.json", "r", encoding="utf-8") as f:
                lista_dicts = json.load(f)
                for d in lista_dicts:
                    libro = Libro(
                        d["titulo"],
                        d["autor"],
                        d["anio"],
                        genero=d.get("genero"),
                        correo=d.get("correo")
                    )
                    self.libros.append(libro)
        except FileNotFoundError:
            pass
