from services.usuariosService import UsuarioService
from services.LibroService import LibroService
from services.PrestamoService import PrestamoService

# ------------------ MENÚS ------------------

def print_menu():
    print("\n=== Menú Principal ===")
    print("1) Gestión de usuarios")
    print("2) Gestión de libros")
    print("3) Gestión de préstamos")
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

def print_menu_prestamos():
    print("\n=== Menú de Préstamos ===")
    print("1) Crear préstamo")
    print("2) Listar préstamos")
    print("3) Marcar devolución")
    print("4) Calcular sanción")
    print("5) Ver colas de espera")
    print("6) Retirarse de la cola de espera")
    print("0) Volver")

# ------------------ PROGRAMA PRINCIPAL ------------------

def main():
    service_usuarios = UsuarioService()
    service_libros = LibroService()
    service_prestamos = PrestamoService(service_usuarios, service_libros)

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
                    u = service_usuarios.agregar_usuario(nombre, apellido, email)
                    print("Usuario creado:", u)

                elif opt_u == "2":
                    if service_usuarios.usuarios:
                        for u in service_usuarios.usuarios:
                            print(u)
                    else:
                        print("No hay usuarios registrados.")

                elif opt_u == "3":
                    nombre = input("Nombre a buscar: ").strip()
                    encontrados = service_usuarios.buscar_usuario_por_nombre(nombre)
                    if encontrados:
                        print("\nUsuarios encontrados:")
                        for u in encontrados:
                            print(u)
                    else:
                        print("No se encontraron usuarios con ese nombre o parte del nombre.")

                elif opt_u == "4":
                    try:
                        id_u = int(input("ID: "))
                        u = service_usuarios.buscar_usuario_por_id(id_u)
                        print(u if u else "Usuario no encontrado")
                    except ValueError:
                        print("ID inválido")

                elif opt_u == "5":
                    try:
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
                    except ValueError:
                        print("ID inválido")

                elif opt_u == "6":
                    try:
                        id_u = int(input("ID a eliminar: "))
                        if service_usuarios.eliminar_usuario(id_u):
                            print("Usuario eliminado")
                        else:
                            print("No encontrado")
                    except ValueError:
                        print("ID inválido")

                elif opt_u == "7":
                    try:
                        id_u = int(input("ID a suspender: "))
                        dias = int(input("Cantidad de días: "))
                        if service_usuarios.suspender_usuario(id_u, dias):
                            print("Usuario suspendido")
                        else:
                            print("No encontrado o ya suspendido")
                    except ValueError:
                        print("Entrada inválida")

                elif opt_u == "8":
                    try:
                        id_u = int(input("ID a reactivar: "))
                        if service_usuarios.reactivar_usuario(id_u):
                            print("Usuario reactivado")
                        else:
                            print("No encontrado o no suspendido")
                    except ValueError:
                        print("ID inválido")

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
                    if service_libros.libros:
                        print("\nLista de libros:")
                        for l in service_libros.libros:
                            print(l)
                    else:
                        print("No hay libros registrados.")

                elif opt_l == "3":
                    titulo = input("Título (o parte del título) a buscar: ").strip()
                    encontrados = service_libros.buscar_por_titulo(titulo)
                    if encontrados:
                        print("\nLibros encontrados:")
                        for l in encontrados:
                            print(l)
                    else:
                        print("No se encontraron libros con ese título o parte del título.")

                elif opt_l == "4":
                    autor = input("Autor (o parte del autor) a buscar: ").strip()
                    encontrados = service_libros.buscar_por_autor(autor)
                    if encontrados:
                        print("\nLibros encontrados:")
                        for l in encontrados:
                            print(l)
                    else:
                        print("No se encontraron libros con ese autor o parte del autor.")

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

        # ---------- Gestión de préstamos ----------
        elif opt == "3":
            while True:
                print_menu_prestamos()
                opt_p = input("Opción: ").strip()

                if opt_p == "1":
                    id_usuario = input("ID del usuario: ").strip()
                    id_libro = input("ID del libro: ").strip()
                    dias = int(input("Días de préstamo (por defecto 7): ") or "7")
                    print(service_prestamos.crear_prestamo(id_usuario, id_libro, dias))

                elif opt_p == "2":
                    prestamos = service_prestamos.listar_prestamos()
                    if prestamos:
                        for p in prestamos:
                            print(p)
                    else:
                        print("No hay préstamos registrados.")

                elif opt_p == "3":
                    id_prestamo = input("ID del préstamo a marcar como devuelto: ").strip()
                    print(service_prestamos.marcar_devuelto(id_prestamo))

                elif opt_p == "4":
                    id_prestamo = input("ID del préstamo: ").strip()
                    print(service_prestamos.calcular_sancion(id_prestamo))

                elif opt_p == "5":
                    print("\n=== Colas de espera activas ===")
                    colas = service_prestamos.ver_colas_de_espera()
                    if colas:
                        for titulo, lista_usuarios in colas.items():
                            print(f"Libro '{titulo}': en espera -> {lista_usuarios}")
                    else:
                        print("No hay colas de espera activas.")

                elif opt_p == "6":
                    id_usuario = input("ID del usuario: ").strip()
                    id_libro = input("ID del libro: ").strip()
                    if service_prestamos.retirar_de_cola(id_usuario, id_libro):
                        print(f"Usuario {id_usuario} retirado de la cola del libro {id_libro}")
                    else:
                        print("Usuario o libro no encontrado en la cola.")

                elif opt_p == "0":
                    break

        elif opt == "0":
            print("Saliendo...")
            break

if __name__ == "__main__":
    main()
