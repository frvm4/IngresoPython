import tkinter as tk
from tkinter import messagebox
import re
import os

# ==========================
# FUNCIONES DE VALIDACIÓN
# ==========================

def EnteroValido(valor):
    """Verifica que el valor pueda convertirse a entero y sea positivo."""
    try:
        numero = int(valor)
        if numero <= 0:
            messagebox.showerror("Error Edad", "La edad debe ser mayor a 0")
            return False
        return True
    except ValueError:
        messagebox.showerror("Error Edad", "La edad debe ser un número entero")
        return False


def DecimalValido(valor):
    """Verifica que el valor pueda convertirse a decimal y sea positivo."""
    try:
        numero = float(valor)
        if numero <= 0:
            messagebox.showerror("Error Estatura", "La estatura debe ser mayor a 0")
            return False
        return True
    except ValueError:
        messagebox.showerror("Error Estatura", "La estatura debe ser un número decimal válido")
        return False


def TelefonoValido(valor):
    """Verifica que el teléfono tenga exactamente 10 dígitos numéricos."""
    if valor.isdigit() and len(valor) == 10:
        return True
    messagebox.showerror("Error Teléfono", "El teléfono debe tener 10 dígitos")
    return False


def TextoValido(valor):
    """Permite solo letras y espacios."""
    if bool(re.match("^[a-zA-Z\\s]+$", valor)):
        return True
    messagebox.showerror("Error Texto", "Solo se permiten letras y espacios")
    return False


def GeneroValido(valor):
    """Verifica que se haya seleccionado un género."""
    if valor == 0:
        messagebox.showerror("Error Género", "Debe seleccionar un género")
        return False
    return True


# ==========================
# FUNCIONES PRINCIPALES
# ==========================

def borrar():
    """Limpia todos los campos del formulario."""
    tbNombre.delete(0, tk.END)
    tbApellido.delete(0, tk.END)
    tbEdad.delete(0, tk.END)
    tbTelefono.delete(0, tk.END)
    tbEstatura.delete(0, tk.END)
    rbSeleccionGenero.set(0)


def guardar():
    """Obtiene los datos, valida y guarda en archivo."""
    nombres = tbNombre.get().strip()
    apellidos = tbApellido.get().strip()
    edad = tbEdad.get().strip()
    tel = tbTelefono.get().strip()
    estatura = tbEstatura.get().strip()
    generoSeleccionado = rbSeleccionGenero.get()

    # Diccionario para evitar muchos if/elif
    generos = {
        1: "Masculino",
        2: "Femenino",
        3: "Otro"
    }

    # Validación completa
    if (TextoValido(nombres) and
        TextoValido(apellidos) and
        EnteroValido(edad) and
        DecimalValido(estatura) and
        TelefonoValido(tel) and
        GeneroValido(generoSeleccionado)):

        genero = generos[generoSeleccionado]

        datos = (
            f"Nombre: {nombres}\n"
            f"Apellido: {apellidos}\n"
            f"Edad: {edad}\n"
            f"Teléfono: {tel}\n"
            f"Estatura: {estatura}\n"
            f"Género: {genero}\n"
            "-------------------------\n"
        )

        try:
            with open("Datos3MRegistro.txt", "a", encoding="utf-8") as archivo:
                archivo.write(datos)

            messagebox.showinfo("Información", "Datos guardados correctamente")
            borrar()

        except IOError:
            messagebox.showerror("Error Archivo", "No se pudo guardar el archivo")


# ==========================
# INTERFAZ GRÁFICA
# ==========================

ventana = tk.Tk()
ventana.configure(bg="gray")
ventana.geometry("350x550")
ventana.title("Actividad 04 - Formulario de Registro")

rbSeleccionGenero = tk.IntVar()

# Etiquetas y entradas
tk.Label(ventana, text="Nombre:", font=("Times New Roman", 14)).pack(padx=10, pady=5)
tbNombre = tk.Entry(ventana, width=35, justify="center")
tbNombre.pack(padx=10, pady=5)

tk.Label(ventana, text="Apellido:", font=("Times New Roman", 14)).pack(padx=10, pady=5)
tbApellido = tk.Entry(ventana, width=35, justify="center")
tbApellido.pack(padx=10, pady=5)

tk.Label(ventana, text="Edad:", font=("Times New Roman", 14)).pack(padx=10, pady=5)
tbEdad = tk.Entry(ventana, width=35, justify="center")
tbEdad.pack(padx=10, pady=5)

tk.Label(ventana, text="Estatura:", font=("Times New Roman", 14)).pack(padx=10, pady=5)
tbEstatura = tk.Entry(ventana, width=35, justify="center")
tbEstatura.pack(padx=10, pady=5)

tk.Label(ventana, text="Teléfono:", font=("Times New Roman", 14)).pack(padx=10, pady=5)
tbTelefono = tk.Entry(ventana, width=35, justify="center")
tbTelefono.pack(padx=10, pady=5)

# Grupo de género
gb = tk.LabelFrame(ventana, text="Seleccione género:", padx=10, pady=8)
gb.pack(padx=10, pady=8)

tk.Radiobutton(gb, text="Masculino", value=1, variable=rbSeleccionGenero).grid(column=1, row=1)
tk.Radiobutton(gb, text="Femenino", value=2, variable=rbSeleccionGenero).grid(column=2, row=1)
tk.Radiobutton(gb, text="Otro", value=3, variable=rbSeleccionGenero).grid(column=3, row=1)

# Botones
gb2 = tk.LabelFrame(ventana)
gb2.pack(padx=10, pady=8)

tk.Button(gb2, text="Guardar", width=10, command=guardar).grid(column=1, row=1)
tk.Button(gb2, text="Borrar", width=10, command=borrar).grid(column=2, row=1)

ventana.mainloop()