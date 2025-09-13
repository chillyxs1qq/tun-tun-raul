def __init__(self, filepath: str = "data/usuarios.txt"):
    # Se recibe como parámetro la ruta del archivo donde se guardarán los datos.
    # Si no se pasa ningún argumento, por defecto se usará "data/usuarios.txt".
    self.filepath = filepath

    # Crea la carpeta 'data' si no existe todavía.
    os.makedirs(os.path.dirname(self.filepath), exist_ok=True)

    # Verifica si el archivo indicado no existe.
    if not os.path.exists(self.filepath):
        # Si no existe, lo crea en modo escritura ("w").
        # Se abre con codificación UTF-8 y con manejo de saltos de línea adecuado.
        with open(self.filepath, mode="w", encoding="utf-8", newline="") as f:
            # Se crea un objeto registro CSV basado en diccionarios,
            # que utilizará como cabeceras los nombres definidos en la lista CSV_HEADERS.
            writer = csv.DictWriter(
                f,
                fieldnames=CSV_HEADERS,  # Lista con las cabeceras/columnas del CSV
                delimiter=",",           # Los campos se separan con coma
                quotechar='"'            # Los textos se encierran entre comillas si es necesario
            )
            # Se escribe la fila de cabecera en el archivo.
            writer.writeheader()
