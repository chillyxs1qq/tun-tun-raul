from models.usuario import Usuario
from services.usuariosService import UsuarioService

def print_menu():
    print("\n=== Menú de Usuario ===")
    print("1) Crear usuario")
    print("2) Listar usuarios")
    print("3) Buscar por nombre")
    print("4) Obtener por ID")
    print("5) Actualizar por ID")
    print("6) Eliminar por ID")
    print("7) Suspender usuario")
    print("8) Reactivar usuario")
    print("0) Salir")

def main():
    service = UsuarioService()
    while True:
        print_menu()
        opt = input("Opción: ").strip()

        if opt == "1":
            nombre = input("Nombre: ").strip()
            apellido = input("Apellido: ").strip()
            email = input("Email: ").strip()
            id_usuario = service.obtener_siguiente_id()
            u = service.agregar_usuario(id_usuario, nombre, apellido, email)
            if u:
                print(f"Usuario creado con ID {id_usuario}: {nombre} {apellido} ({email})")
            else:
                print("Error: Ya existe un usuario con ese ID.")

        elif opt == "2":
            usuarios = service.usuarios
            if usuarios:
                for u in usuarios:
                    print(u)
            else:
                print("No hay usuarios registrados.")

        elif opt == "3":
            nombre = input("Ingrese nombre a buscar: ").strip()
            encontrados = service.buscar_usuario_por_nombre(nombre)
            if encontrados:
                for u in encontrados:
                    print(u)
            else:
                print("No se encontraron usuarios.")

        elif opt == "4":
            try:
                id_u = int(input("Ingrese ID: "))
                u = service.buscar_usuario_por_id(id_u)
                if u:
                    print(u)
                else:
                    print("Usuario no encontrado.")
            except:
                print("ID inválido.")

        elif opt == "5":
            try:
                id_u = int(input("ID a actualizar: "))
                usuario = service.buscar_usuario_por_id(id_u)
                if usuario:
                    nombre = input("Nuevo nombre: ")
                    apellido = input("Nuevo apellido: ")
                    email = input("Nuevo email: ")
                    service.modificar_usuario(id_u, nombre, apellido, email)
                    print("Usuario actualizado:", usuario)
                else:
                    print("Usuario no encontrado.")
            except:
                print("ID inválido.")

        elif opt == "6":
            try:
                id_u = int(input("ID a eliminar: "))
                if service.eliminar_usuario(id_u):
                    print("Usuario eliminado.")
                else:
                    print("Usuario no encontrado.")
            except:
                print("ID inválido.")

        elif opt == "7":
            try:
                id_u = int(input("ID a suspender: "))
                dias = int(input("Cantidad de días: "))
                if service.suspender_usuario(id_u, dias):
                    print(f"Usuario suspendido por {dias} días.")
                else:
                    print("Usuario no encontrado o ya suspendido.")
            except:
                print("Entrada inválida.")

        elif opt == "8":
            try:
                id_u = int(input("ID a reactivar: "))
                if service.reactivar_usuario(id_u):
                    print("Usuario reactivado.")
                else:
                    print("Usuario no encontrado o no está suspendido.")
            except:
                print("ID inválido.")

        elif opt == "0":
            print("Saliendo...")
            break

if __name__ == "__main__":
    main()
