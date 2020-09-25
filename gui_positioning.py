from tkinter import *
from tkinter import ttk

# Configuración de la ventana principal
root = Tk()
root.geometry('400x400')
root.configure(bg="#2573a1")
root.title('Agenda')

# Elementos gráficos añadidos (widgets)

# Creamos el contenedor para el primer par de datos
frm_name = Frame(root)
frm_name.configure(bg="#2573a1")
frm_name.pack(fill=X)

# Etiqueta para el nombre
ttk.Label(frm_name, width=8, text="Nombre", background="#2573a1", foreground="#edea5a", font=('Arial', 14, 'bold')).pack(
    side=LEFT, anchor=NW, padx=10, pady=20)

# Cuadro de texto para el nombre
txt_name = StringVar()  # txt_name = ""
ttk.Entry(frm_name, textvariable=txt_name, font=('Arial', 14, 'italic')).pack(
    anchor=NW, side=LEFT,  padx=10, pady=20, fill=X, expand=1)

# Creamos el contenedor para el primer par de datos
frm_phone = Frame(root)
frm_phone.configure(bg="#2573a1")
frm_phone.pack(fill=X)

# Etiqueta para el nombre
ttk.Label(frm_phone, width=8, text="Teléfono", background="#2573a1", foreground="#edea5a", font=('Arial', 14, 'bold')).pack(
    side=LEFT, anchor=NW, padx=10, pady=10)

# Cuadro de texto para el nombre
txt_phone = StringVar()  # txt_nombre = ""
ttk.Entry(frm_phone, textvariable=txt_phone, font=('Arial', 14, 'normal')).pack(
    anchor=NW, side=LEFT,  padx=10, pady=10, fill=X, expand=1)

# Creamos el contenedor para el primer par de datos
frm_fb = Frame(root)
frm_fb.configure(bg="#2573a1")
frm_fb.pack(fill=X)

# Etiqueta para el nombre
ttk.Label(frm_fb, width=8, text="Facebook", background="#2573a1", foreground="#edea5a", font=('Arial', 14, 'bold')).pack(
    side=LEFT, anchor=NW, padx=10, pady=10)

# Cuadro de texto para el nombre
txt_fb = StringVar()  # txt_nombre = ""
ttk.Entry(frm_fb, textvariable=txt_fb, font=('Arial', 14, 'normal')).pack(
    anchor=NW, side=LEFT,  padx=10, pady=10, fill=X, expand=1)

# Creamos el contenedor para el primer par de datos
frm_tiktok = Frame(root)
frm_tiktok.configure(bg="#2573a1")
frm_tiktok.pack(fill=X)

# Etiqueta para el nombre
ttk.Label(frm_tiktok, width=8, text="TikTok", background="#2573a1", foreground="#edea5a", font=('Arial', 14, 'bold')).pack(
    side=LEFT, anchor=NW, padx=10, pady=10)

# Cuadro de texto para el nombre
txt_tiktok = StringVar()  # txt_nombre = ""
ttk.Entry(frm_tiktok, textvariable=txt_tiktok, font=('Arial', 14, 'normal')).pack(
    anchor=NW, side=LEFT,  padx=10, pady=10, fill=X, expand=1)

# Creamos el contenedor para el primer par de datos
frm_close = Frame(root)
frm_close.configure(bg="#2573a1")
frm_close.pack(fill=X)


def msgConsole():
    print("Puchaste el botón...")


# Creamos el botón de salida
Button(frm_close, text="Guardar y salir...", font=('Arial', 14, 'normal'),
       command=msgConsole).pack(side=BOTTOM)

root.mainloop()
