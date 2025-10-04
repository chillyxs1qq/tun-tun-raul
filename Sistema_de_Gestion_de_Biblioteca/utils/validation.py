# utils/validation.py
import re

# ---------------------
# Validación de correo
# ---------------------
def validar_correo(correo):
    """
    Valida que el correo tenga formato válido y dominios comunes.
    Permite: gmail, yahoo, hotmail, outlook, .com/.net/.org
    """
    pattern = r'^[\w\.-]+@[\w\.-]+\.(com|net|org)$'
    if not re.match(pattern, correo):
        raise ValueError("Correo inválido. Debe tener formato correcto y dominio .com/.net/.org")
    return correo

# ---------------------
# Validación de strings
# ---------------------
def validar_titulo(titulo):
    if not titulo or not titulo.strip():
        raise ValueError("Título vacío")
    return titulo.strip()

def validar_autor(autor):
    if not autor or not autor.strip():
        raise ValueError("Autor vacío")
    return autor.strip()

def validar_nombre(nombre):
    if not nombre or not nombre.strip():
        raise ValueError("Nombre vacío")
    return nombre.strip()

def validar_apellido(apellido):
    if not apellido or not apellido.strip():
        raise ValueError("Apellido vacío")
    return apellido.strip()

# ---------------------
# Validación de año
# ---------------------
def validar_anio(anio):
    try:
        anio_int = int(anio)
    except ValueError:
        raise ValueError("Año inválido")
    if anio_int <= 0:
        raise ValueError("Año debe ser mayor que 0")
    return anio_int
