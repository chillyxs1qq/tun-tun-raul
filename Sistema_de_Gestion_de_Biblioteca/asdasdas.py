# no sirve.py
from models.usuario import Usuario


# Crear servicio
servicio = UsuarioService()

# Agregar usuarios
servicio.agregar_usuario(1, "Ana")
servicio.agregar_usuario(2, "Luis")
servicio.agregar_usuario(3, "María")

print("Usuarios cargados:")
for u in servicio.usuarios:
    print(u)

# Modificar usuario
servicio.modificar_usuario(2, "Luis Pérez")

# Suspender a un usuario
servicio.suspender_usuario(1, dias=3)

print("\nUsuarios después de suspensión y modificación:")
for u in servicio.usuarios:
    print(u)

# Reactivar usuario (intento antes de que pase el plazo → debe fallar)
print("\nReactivar usuario 1:")
print(servicio.reactivar_usuario(1))  # debería dar False todavía

# Buscar por nombre
print("\nBuscar 'Luis':")
encontrados = servicio.buscar_usuario_por_nombre("Luis")
for e in encontrados:
    print(e)
