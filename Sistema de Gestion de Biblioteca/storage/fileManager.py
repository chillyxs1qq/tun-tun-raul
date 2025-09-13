CSV_HEADERS = ["id", "nombre", "email", "estado", "apellido"]

class FileManager:
    """
    Gestiona lectura/escritura de usuarios en un TXT (CSV).
    Guarda el archivo en data/usuarios.txt por defecto.
    """
    def __init__(self, filepath: str = "data/usuarios.txt"):
        self.filepath = filepath
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
        # Crear archivo con cabecera si no existe
        if not os.path.exists(self.filepath):
            with open(self.filepath, mode="w", encoding="utf-8", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=CSV_HEADERS, delimiter=",", quotechar='"')
                writer.writeheader()

    def read_all(self):
        with open(self.filepath, mode="r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f, delimiter=",", quotechar='"')
            return [row for row in reader]

    def write_all(self, rows: List[Dict]):
        with open(self.filepath, mode="w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=CSV_HEADERS, delimiter=",", quotechar='"')
            writer.writeheader()
            for r in rows:
                writer.writerow(r)

    def append(self, row: Dict):
        # Asegura cabecera si alguien borró el archivo
        file_exists = os.path.exists(self.filepath) and os.path.getsize(self.filepath) > 0
        with open(self.filepath, mode="a", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=CSV_HEADERS, delimiter=",", quotechar='"')
            if not file_exists:
                writer.writeheader()
            writer.writerow(row)

    def read_all(self):
    # Abre el archivo en modo lectura ("r").
    # newline="" asegura que los saltos de línea se manejen de forma uniforme.
    with open(self.filepath, mode="r", encoding="utf-8", newline="") as f:

        # Crea un objeto lector CSV que interpreta cada fila como un diccionario.
        # Las claves del diccionario son las cabeceras definidas en la primera fila del archivo (CSV_HEADERS).
        reader = csv.DictReader(
            f,
            delimiter=",",   # Usa coma para separar los campos
            quotechar='"'    # Los textos entre comillas se interpretan como un único valor
        )

        # Convierte todas las filas en una lista de diccionarios y la devuelve.
        return [row for row in reader]

    def write_all(self, rows: List[Dict]):
    # Abre el archivo en modo escritura ("w").
    with open(self.filepath, mode="w", encoding="utf-8", newline="") as f:

        # Crea un objeto registro de CSV basado en diccionarios.
        writer = csv.DictWriter(
            f,
            fieldnames=CSV_HEADERS,  # Cabeceras de las columnas
            delimiter=",",           # Los campos estarán separados por coma
            quotechar='"'            # Para encerrar valores que tienen comas o espacios
        )

        # Escribe primero la fila de cabecera en el archivo.
        writer.writeheader()

        # Recorre cada diccionario en la lista 'rows' y lo escribe como una fila en el archivo.
        for r in rows:
            writer.writerow(r)

        def append(self, row: Dict):
    # Verifica si el archivo existe y no está vacío.
    # Esto es importante porque si el archivo fue borrado o está vacío,
    # habrá que volver a escribir la cabecera (headers).
    file_exists = os.path.exists(self.filepath) and os.path.getsize(self.filepath) > 0

    # Abre el archivo en modo append ("a"), es decir, agrega datos al final sin borrar lo anterior.
    with open(self.filepath, mode="a", encoding="utf-8", newline="") as f:
        # Crea un objeto registro CSV basado en diccionarios.
        writer = csv.DictWriter(
            f,
            fieldnames=CSV_HEADERS,
            delimiter=",",   # Los campos se separan por coma
            quotechar='"'    # Valores que tienen comas o espacios se encierran en comillas
        )

        # Si el archivo no existía o estaba vacío, escribe primero la fila de cabecera.
        if not file_exists:
            writer.writeheader()

        # Escribe la nueva fila (row) al final del archivo.
        writer.writerow(row)