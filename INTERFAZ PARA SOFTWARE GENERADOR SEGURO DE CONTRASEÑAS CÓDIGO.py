import tkinter as tk
import string
import secrets
from tkinter import messagebox

# Función para generar la contraseña segura
def generar_contraseña(longitud):
    if longitud < 10:
        return "La longitud mínima de la contraseña debe ser 10 caracteres."

    caracteres_mayusculas = string.ascii_uppercase
    caracteres_minusculas = string.ascii_lowercase
    caracteres_numeros = string.digits
    caracteres_especiales = string.punctuation

    contraseña = ''.join(secrets.choice(caracteres_mayusculas + caracteres_minusculas + caracteres_numeros + caracteres_especiales) for _ in range(longitud))

    tiene_mayuscula = any(c in caracteres_mayusculas for c in contraseña)
    tiene_minuscula = any(c in caracteres_minusculas for c in contraseña)
    tiene_numero = any(c in caracteres_numeros for c in contraseña)
    tiene_especial = any(c in caracteres_especiales for c in contraseña)

    errores = []

    if not tiene_mayuscula:
        errores.append("Falta al menos una letra mayúscula.")
    if not tiene_minuscula:
        errores.append("Falta al menos una letra minúscula.")
    if not tiene_numero:
        errores.append("Falta al menos un número.")
    if not tiene_especial:
        errores.append("Falta al menos un carácter especial.")

    if errores:
        return errores
    else:
        return contraseña


# Función para manejar el botón de "Generar Contraseña"
def generar():
    try:
        longitud = int(entry_longitud.get())  # Obtener la longitud de la contraseña desde el campo de texto

        if longitud < 10:
            result_label.config(text="La longitud mínima de la contraseña debe ser 10 caracteres.", fg="red")
        else:
            contraseña = generar_contraseña(longitud)

            if isinstance(contraseña, list):  # Si hay errores en la contraseña
                result_label.config(text="\n".join(contraseña), fg="red")
            else:
                result_label.config(text="Contraseña generada: " + contraseña, fg="green")
                # Guardar la contraseña en un archivo
                guardar_contraseña(contraseña)
    except ValueError:
        result_label.config(text="Por favor, ingresa un número válido.", fg="red")


# Función para guardar la contraseña en un archivo de texto
def guardar_contraseña(contraseña):
    try:
        with open("contraseñas_guardadas.txt", "a") as archivo:
            archivo.write(contraseña + "\n")
        # Mostrar un mensaje de confirmación al guardar
        messagebox.showinfo("Contraseña Guardada", "La contraseña se ha guardado correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo guardar la contraseña: {e}")


# Función para mostrar el repertorio de contraseñas generadas
def mostrar_repertorio():
    try:
        with open("contraseñas_guardadas.txt", "r") as archivo:
            contraseñas = archivo.readlines()
            if contraseñas:
                repertorio_texto = "".join([f"{i+1}. {contraseña.strip()}\n" for i, contraseña in enumerate(contraseñas)])
                result_label.config(text=repertorio_texto, fg="blue")
            else:
                result_label.config(text="No hay contraseñas guardadas aún.", fg="red")
    except FileNotFoundError:
        result_label.config(text="No se ha creado ningún archivo de contraseñas aún.", fg="red")


# Función para eliminar una contraseña específica
def eliminar_contraseña():
    try:
        with open("contraseñas_guardadas.txt", "r") as archivo:
            contraseñas = archivo.readlines()
        
        if contraseñas:
            # Mostrar al usuario un listado de contraseñas guardadas
            index = int(entry_longitud.get()) - 1
            if 0 <= index < len(contraseñas):
                contraseñas.pop(index)  # Eliminar la contraseña seleccionada

                # Guardar el nuevo listado sin la contraseña eliminada
                with open("contraseñas_guardadas.txt", "w") as archivo:
                    archivo.writelines(contraseñas)

                messagebox.showinfo("Contraseña Eliminada", "La contraseña ha sido eliminada correctamente.")
            else:
                messagebox.showerror("Error", "Índice de contraseña no válido.")
        else:
            messagebox.showerror("Error", "No hay contraseñas guardadas para eliminar.")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa un índice numérico válido.")


# Crear la ventana principal
root = tk.Tk()
root.title("Generador de Contraseñas Seguras")
root.geometry("500x400")
root.config(bg="#f2f2f2")  # Fondo gris claro

# Etiqueta de título
title_label = tk.Label(root, text="Generador de Contraseñas", font=("Arial", 18), bg="#f2f2f2")
title_label.pack(pady=10)

# Campo de entrada para longitud de la contraseña
entry_label = tk.Label(root, text="Ingresa la longitud de la contraseña (mínimo 10):", bg="#f2f2f2")
entry_label.pack(pady=5)

entry_longitud = tk.Entry(root, width=20, font=("Arial", 12))
entry_longitud.pack(pady=5)

# Botón para generar la contraseña
generate_button = tk.Button(root, text="Generar Contraseña", command=generar, bg="#4CAF50", fg="white", font=("Arial", 12))
generate_button.pack(pady=10)

# Botón para mostrar el repertorio de contraseñas generadas
repertorio_button = tk.Button(root, text="Ver Repertorio", command=mostrar_repertorio, bg="#FF9800", fg="white", font=("Arial", 12))
repertorio_button.pack(pady=10)

# Botón para eliminar una contraseña específica
eliminar_button = tk.Button(root, text="Eliminar Contraseña", command=eliminar_contraseña, bg="#F44336", fg="white", font=("Arial", 12))
eliminar_button.pack(pady=10)

# Etiqueta para mostrar el resultado
result_label = tk.Label(root, text="", font=("Arial", 12), justify="left", bg="#f2f2f2")
result_label.pack(pady=10)

# Ejecutar la interfaz
root.mainloop()

