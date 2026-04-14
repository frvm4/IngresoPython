import tkinter as tk
from tkinter import messagebox
import re
import mysql.connector

def insertarRegistro(nombre, apellido, edad, estatura, telefono,genero):
    try:
        conexion = mysql.connector.connect(
            host="localhost", user="root", password="4444", database="formulario")
        cursor = conexion.cursor()
        query = "INSERT INTO registro (nombre, apellido, edad, estatura, telefono, genero) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (nombre, apellido, edad, estatura, telefono, genero)
        cursor.execute(query, valores)
        conexion.commit()
        cursor.close()
        conexion.close()
        messagebox.showinfo("Información", "Datos guardados en la base de datos con éxito.")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error al insertar los datos:{err}")

def EnteroValido(valor):
    try:
        int(valor)
        return True
    except ValueError:
        messagebox.showerror("Error Edad","Valor de edad equivocado")
        return False
def DecimalValido(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False
def TelefonoValido(valor):
    return valor.isdigit() and len(valor)==10
def TextoValido(valor):
    return bool(re.match("^[a-zA-Z\\s]+$", valor))

def borrar():
    tbNombre.delete(0, tk.END)
    tbApellido.delete(0, tk.END)
    tbEdad.delete(0, tk.END)
    tbTelefono.delete(0, tk.END)
    tbEstatura.delete(0, tk.END)
    rbSeleccionGenero.set(0)

def guardar():
    nombres = tbNombre.get()
    apellidos = tbApellido.get()
    edad = tbEdad.get()
    tel = tbTelefono.get()
    estatura = tbEstatura.get()
    genero = ""

    if rbSeleccionGenero.get()==1:
        genero="Masculino"
    elif rbSeleccionGenero.get()==2:
        genero="Femenino"
    elif rbSeleccionGenero.get()==3:
        genero="Otro"
    if (EnteroValido(edad) and DecimalValido(estatura)and TelefonoValido(tel)and TextoValido(nombres) and TextoValido(apellidos)):
        datos = f"Nombre: {nombres}\nApellido: {apellidos}\nEdad: {edad} \nTelefono: {tel}\nEstatura: {estatura}\nGenero: {genero}"
        with open ("Datos3MRegistro","a") as archivo:
            insertarRegistro(nombres, apellidos, edad, estatura, tel, genero)
            archivo.write(datos+"\n\n")
        messagebox.showinfo("Información", "Datos guardados correctamente\n"
                        +datos)

ventana = tk.Tk()
ventana.configure(bg="gray")
ventana.geometry("350x550")
ventana.title("Actividad 04 - Formulario de Registro")

rbSeleccionGenero = tk.IntVar()

tk.Label(ventana, text="Nombre: ", font=("Times New Roman", 14, "" )).pack(padx=10, pady=5)
tbNombre = tk.Entry(ventana, width=35, justify="center")
tbNombre.pack(padx=10, pady=5)
tk.Label(ventana, text="Apellido: ", font=("Times New Roman", 14, "" )).pack(padx=10, pady=5)
tbApellido = tk.Entry(ventana, width=35, justify="center")
tbApellido.pack(padx=10, pady=5)
tk.Label(ventana, text="Edad: ", font=("Times New Roman", 14, "" )).pack(padx=10, pady=5)
tbEdad = tk.Entry(ventana, width=35, justify="center")
tbEdad.pack(padx=10, pady=5)
tk.Label(ventana, text="Estatura: ", font=("Times New Roman", 14, "" )).pack(padx=10, pady=5)
tbEstatura = tk.Entry(ventana, width=35, justify="center")
tbEstatura.pack(padx=10, pady=5)
tk.Label(ventana, text="Teléfono: ", font=("Times New Roman", 14, "" )).pack(padx=10, pady=5)
tbTelefono = tk.Entry(ventana, width=35, justify="center")
tbTelefono.pack(padx=10, pady=5)

gb = tk.LabelFrame(ventana, text="Seleccione genero: ", padx=10, pady=8)
gb.pack(padx=10,pady=8)

rbMasculino = tk.Radiobutton(gb, text="Masculino", value=1, variable=rbSeleccionGenero)
rbMasculino.grid(column=1, row=1)
rbFemenino = tk.Radiobutton(gb, text="Femenino", value=2, variable=rbSeleccionGenero)
rbFemenino.grid(column=2, row=1)
rbOtro = tk.Radiobutton(gb, text="Otro", value=3, variable=rbSeleccionGenero)
rbOtro.grid(column=3, row=1)

gb2 = tk.LabelFrame(ventana, text="")
gb2.pack(padx=10,pady=8)

btnBorrar = tk.Button(gb2, text="Borrar", width=10, padx=10, pady=8, command=borrar)
btnBorrar.grid(column=2, row=1)
btnGuardar = tk.Button(gb2, text="Guardar", width=10, padx=10, pady=8, command=guardar)
btnGuardar.grid(column=1, row=1)

ventana.mainloop()