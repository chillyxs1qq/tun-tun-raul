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