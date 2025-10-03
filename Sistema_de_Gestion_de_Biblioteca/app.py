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
    print("7) Exportar a JSON")
    print("8) Importar desde JSON")
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
            try:
                u = service.create_user(nombre, apellido, email)
                print("Creado:", u)
            except ValueError as e:
                print("Error:", e)

        elif opt == "2":
            usuarios = service.get_all_users()
            for u in usuarios:
                print(u)

        elif opt == "3":
            nombre = input("Ingrese nombre a buscar: ").strip()
            encontrados = service.find_by_name(nombre)
            for u in encontrados:
                print(u)

        elif opt == "4":
            try:
                id_u = int(input("Ingrese ID: "))
                u = service.get_user_by_id(id_u)
                print(u)
            except Exception as e:
                print("Error:", e)

        elif opt == "5":
            try:
                id_u = int(input("ID a actualizar: "))
                nombre = input("Nuevo nombre: ")
                apellido = input("Nuevo apellido: ")
                email = input("Nuevo email: ")
                u = service.update_user(id_u, nombre, apellido, email)
                print("Actualizado:", u)
            except Exception as e:
                print("Error:", e)

        elif opt == "6":
            try:
                id_u = int(input("ID a eliminar: "))
                service.delete_user(id_u)
                print("Usuario eliminado.")
            except Exception as e:
                print("Error:", e)

        elif opt == "0":
            print("Saliendo...")
            break


if __name__ == "__main__":
    main()
