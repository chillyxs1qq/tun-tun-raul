from  import

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
    service = usuariosService()
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

if __name__ == "__main__":
    main()
