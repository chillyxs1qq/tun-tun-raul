import tkinter as tk

# Crear ventana ahr
ventana = tk.Tk()
ventana.title("Sistema de Gestión de Biblioteca")
ventana.geometry("450x400")
ventana.configure(bg="#f0f0f0")

# Icono .ICO TUN TUN SAHUR XD
ventana.iconbitmap(r"C:\Users\joaca\OneDrive\Desktop\CERP\Segundo Semestre\Programacion II\PROYECTO FINAL\icono tun tun sahur\tun_tun_sahur.ico")

# Formulario con grid
# ID del libro (automático, no editable)
tk.Label(ventana, text="ID del Libro:", font=("Arial", 12, "bold"), bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entrada_id = tk.Entry(ventana, width=5, font=("Arial", 12, "bold"), justify="center")  # más cuadrado y centrado
entrada_id.insert(0, "1")  # por defecto empieza en 1
entrada_id.config(state="readonly", readonlybackground="#d9edf7", fg="#31708f", bd=2)  # solo lectura con color
entrada_id.grid(row=0, column=1, padx=10, pady=5, sticky="w")

tk.Label(ventana, text="Título:", font=("Arial", 12, "bold"), bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=5, sticky="e")
tk.Entry(ventana, width=30).grid(row=1, column=1, padx=10, pady=5)

tk.Label(ventana, text="Autor:", font=("Arial", 12, "bold"), bg="#f0f0f0").grid(row=2, column=0, padx=10, pady=5, sticky="e")
tk.Entry(ventana, width=30).grid(row=2, column=1, padx=10, pady=5)

tk.Label(ventana, text="Descripción:", font=("Arial", 12, "bold"), bg="#f0f0f0").grid(row=3, column=0, padx=10, pady=5, sticky="e")
tk.Entry(ventana, width=30).grid(row=3, column=1, padx=10, pady=5)

# Botones no toquen nada please
tk.Button(ventana, text="Guardar Libro", bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), width=15).grid(row=4, column=0, padx=10, pady=15)
tk.Button(ventana, text="Limpiar Campos", bg="#2196F3", fg="white", font=("Arial", 10, "bold"), width=15).grid(row=4, column=1, padx=10, pady=15)
tk.Button(ventana, text="Salir", bg="#f44336", fg="white", font=("Arial", 10, "bold"), width=15, command=ventana.destroy).grid(row=5, column=0, columnspan=2, pady=10)

# Etiqueta de mensaje
tk.Label(ventana, text="¡Bienvenido al Sistema de Gestion Biblioteca!", font=("Arial", 10), bg="#f0f0f0", fg="green").grid(row=6, column=0, columnspan=2)

# Listbox para mostrar libros /esto hay que ver /
tk.Listbox(ventana, width=60, height=6).grid(row=7, column=0, columnspan=2, padx=10, pady=10)

# Centrar ventana
ventana.update_idletasks()
ancho = ventana.winfo_width()
alto = ventana.winfo_height()
x = (ventana.winfo_screenwidth() // 2) - (ancho // 2)
y = (ventana.winfo_screenheight() // 2) - (alto // 2)
ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

# Iniciar ventana
ventana.mainloop()
