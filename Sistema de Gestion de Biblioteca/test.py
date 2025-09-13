#importar tkinter
import tkinter as tk
ventana = tk.Tk()
ventana.title("Sistema de Gestion de Biblioteca")
ventana.geometry("300x200")  # ancho x alto

# 👇 Ruta completa al archivo .ico
ventana.iconbitmap(r"C:\Users\joaca\OneDrive\Desktop\CERP\Segundo Semestre\Programacion II\PROYECTO FINAL\icono tun tun sahur\tun_tun_sahur.ico")

tk.Label(ventana, text="ID del Libro:").pack(pady=5)
entrada_id = tk.Entry(ventana)
entrada_id.pack(pady=5)

tk.Label(ventana, text="Título:").pack(pady=5)
entrada_titulo = tk.Entry(ventana)
entrada_titulo.pack(pady=5)

tk.Label(ventana, text="Autor:").pack(pady=5)
entrada_autor = tk.Entry(ventana)
entrada_autor.pack(pady=5)

# Agregar un mensaje
etiqueta = tk.Label(ventana, text="¡ABUELA XD QUE HACES?!")
etiqueta.pack(pady=20)

# Botón para cerrar
boton = tk.Button(ventana, text="FOCKING PANSA", command=ventana.destroy)
boton.pack()

# Iniciar bucle de la ventana
ventana.mainloop()
