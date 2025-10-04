from services.usuariosService import UsuarioService
from services.LibroService import LibroService

def print_menu():
    print("\n=== Menú Principal ===")
    print("1) Gestión de usuarios")
    print("2) Gestión de libros")
    print("0) Salir")

def print_menu_usuarios():
    print("\n=== Menú de Usuarios ===")
    print("1) Crear usuario")
    print("2) Listar usuarios")
    print("3) Buscar por nombre")
    print("4) Obtener por ID")
    print("5) Actualizar por ID")
    print("6) Eliminar por ID")
    print("7) Suspender usuario")
    print("8) Reactivar usuario")
    print("0) Volver")

def print_menu_libros():
    print("\n=== Menú de Libros ===")
    print("1) Agregar libro")
    print("2) Listar libros")
    print("3) Buscar por título")
    print("4) Buscar por autor")
    print("5) Modificar libro")
    print("6) Eliminar libro")
    print("0) Volver")

def main():
    service_usuarios = UsuarioService()
    service_libros = LibroService()

    while True:
        print_menu()
        opt = input("Opción: ").strip()

        # ---------- Gestión de usuarios ----------
        if opt == "1":
            while True:
                print_menu_usuarios()
                opt_u = input("Opción: ").strip()

                if opt_u == "1":
                    nombre = input("Nombre: ").strip()
                    apellido = input("Apellido: ").strip()
                    email = input("Email: ").strip()
                    id_usuario = service_usuarios.obtener_siguiente_id()
                    u = service_usuarios.agregar_usuario(id_usuario, nombre, apellido, email)
                    print("Usuario creado:", u)

                elif opt_u == "2":
                    for u in service_usuarios.usuarios:
                        print(u)

                elif opt_u == "3":
                    nombre = input("Nombre a buscar: ").strip()
                    encontrados = service_usuarios.buscar_usuario_por_nombre(nombre)
                    if encontrados:
                        for u in encontrados:
                            print(u)
                    else:
                        print("No se encontraron usuarios con ese nombre.")

                elif opt_u == "4":
                    id_u = int(input("ID: "))
                    u = service_usuarios.buscar_usuario_por_id(id_u)
                    print(u if u else "Usuario no encontrado")

                elif opt_u == "5":
                    id_u = int(input("ID a actualizar: "))
                    usuario = service_usuarios.buscar_usuario_por_id(id_u)
                    if usuario:
                        nombre = input("Nuevo nombre: ")
                        apellido = input("Nuevo apellido: ")
                        email = input("Nuevo email: ")
                        service_usuarios.modificar_usuario(id_u, nombre, apellido, email)
                        print("Usuario actualizado:", usuario)
                    else:
                        print("Usuario no encontrado")

                elif opt_u == "6":
                    id_u = int(input("ID a eliminar: "))
                    if service_usuarios.eliminar_usuario(id_u):
                        print("Usuario eliminado")
                    else:
                        print("No encontrado")

                elif opt_u == "7":
                    id_u = int(input("ID a suspender: "))
                    dias = int(input("Cantidad de días: "))
                    if service_usuarios.suspender_usuario(id_u, dias):
                        print("Usuario suspendido")
                    else:
                        print("No encontrado")

                elif opt_u == "8":
                    id_u = int(input("ID a reactivar: "))
                    if service_usuarios.reactivar_usuario(id_u):
                        print("Usuario reactivado")
                    else:
                        print("No encontrado o no suspendido")

                elif opt_u == "0":
                    break

        # ---------- Gestión de libros ----------
        elif opt == "2":
            while True:
                print_menu_libros()
                opt_l = input("Opción: ").strip()

                if opt_l == "1":
                    titulo = input("Título: ").strip()
                    autor = input("Autor: ").strip()
                    anio = input("Año: ").strip()
                    genero = input("Género: ").strip()
                    libro = service_libros.agregar_libro(titulo, autor, anio, genero)
                    print("Libro agregado:", libro)

                elif opt_l == "2":
                    for l in service_libros.libros:
                        print(l)

                elif opt_l == "3":
                    titulo = input("Título a buscar: ").strip()
                    encontrados = service_libros.buscar_por_titulo(titulo)
                    for l in encontrados:
                        print(l)

                elif opt_l == "4":
                    autor = input("Autor a buscar: ").strip()
                    encontrados = service_libros.buscar_por_autor(autor)
                    for l in encontrados:
                        print(l)

                elif opt_l == "5":
                    id_libro = input("ID del libro a modificar: ").strip()
                    libro = service_libros.buscar_por_id(id_libro)
                    if libro:
                        titulo = input("Nuevo título: ")
                        autor = input("Nuevo autor: ")
                        anio = input("Nuevo año: ")
                        genero = input("Nuevo género: ")
                        service_libros.modificar_libro(id_libro, titulo, autor, anio, genero)
                        print("Libro actualizado:", libro)
                    else:
                        print("Libro no encontrado")

                elif opt_l == "6":
                    id_libro = input("ID del libro a eliminar: ").strip()
                    if service_libros.eliminar_libro(id_libro):
                        print("Libro eliminado")
                    else:
                        print("No encontrado")

                elif opt_l == "0":
                    break

        elif opt == "0":
            print("Saliendo...")
            break

if __name__ == "__main__":
    main()
