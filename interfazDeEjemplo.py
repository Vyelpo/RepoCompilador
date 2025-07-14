from tkinter import *
from tkinter import ttk

def imprimir(*args):
    print(user.get() + " " + password.get())

# Inicializamos la interfaz
root = Tk()
root.title("App")

# Modificamos la interfaz para que el programa lo "vea" como un tablero 3x3
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Creamos textos y los colocamos en la ventana
ttk.Label(mainframe, text="Usuario").grid(column=2, row=1, sticky=(W, E))
ttk.Label(mainframe, text="Contraseña").grid(column=3, row=1, sticky=(W, E))

# Creamos un campo rellenable para usuario y contraseña respectivamente y los colocamos debajo de los textos
user = StringVar() 
user_entry = ttk.Entry(mainframe, width=12, textvariable=user)
user_entry.grid(column=2, row=2, sticky=(W, E))

password = StringVar()
password_entry = ttk.Entry(mainframe, width=12, textvariable=password)
password_entry.grid(column=3, row=2, sticky=(W, E))

# Botón que simula el ingresar las credenciales
ttk.Button(mainframe, text="Ingresar", command=imprimir).grid(column=3, row=3, sticky=W)

# Espaciado entre los textos y demás objetos dentro de la ventana
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

user_entry.focus()
root.mainloop()