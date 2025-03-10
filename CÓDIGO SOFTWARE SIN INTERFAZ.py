import string
import secrets
from colorama import init, Fore # type: ignore

# Inicializar colorama
init(autoreset=True)

def generar_contraseña(longitud):
    if longitud < 10:
        raise ValueError("La longitud mínima de la contraseña debe ser 10 caracteres.")

    caracteres_mayusculas = string.ascii_uppercase  # Letras mayúsculas
    caracteres_minusculas = string.ascii_lowercase  # Letras minúsculas
    caracteres_numeros = string.digits  # Números
    caracteres_especiales = string.punctuation  # Caracteres especiales

    while True:
        # Generar una contraseña inicial de la longitud solicitada
        contraseña = ''.join(secrets.choice(caracteres_mayusculas + caracteres_minusculas + caracteres_numeros + caracteres_especiales) for _ in range(longitud))

        # Validar si cumple con los requisitos mínimos
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

        # Calcular el nivel de seguridad y agregar colores
        if errores:
            print(Fore.RED + "Error: La contraseña generada no cumple con los requisitos de seguridad.")
            for error in errores:
                print(Fore.RED + f"- {error}")
            print(Fore.YELLOW + f"Faltan {len(errores)} requisitos que deben cumplirse.")  # Mejor descripción
            return None  # Retornar None si la contraseña no es segura
        else:
            # Contraseña segura
            print(Fore.GREEN + "Contraseña generada con éxito. Cumple con todos los requisitos de seguridad.")
            return contraseña

def main():
    while True:  # Bucle que permite repetir el proceso de generación de contraseñas
        try:
            longitud = int(input("Ingrese la longitud de la contraseña deseada (mínimo 10 caracteres): "))

            if longitud < 10:
                print(Fore.RED + "Error: La contraseña debe tener al menos 10 caracteres.")
            else:
                contraseña_segura = generar_contraseña(longitud)
                if contraseña_segura:
                    print(Fore.GREEN + "Contraseña segura generada:", contraseña_segura)

                # Opción para previsualizar la contraseña antes de aceptarla
                previsualizar = input("¿Desea previsualizar otra contraseña antes de aceptarla? (s/n): ").strip().lower()
                if previsualizar == 's':
                    print(Fore.YELLOW + "Aquí tienes una nueva previsualización de la contraseña:", contraseña_segura)
                    continue  # Si desea ver otra previsualización, se vuelve a generar una contraseña

                # Si está conforme con la contraseña, la acepta
                aceptar = input("¿Está conforme con esta contraseña? (s/n): ").strip().lower()
                if aceptar == 's':
                    print(Fore.GREEN + "Contraseña aceptada:", contraseña_segura)
                else:
                    print(Fore.YELLOW + "Generando una nueva contraseña...")

            otra = input("¿Desea generar otra contraseña? (s/n): ").strip().lower()  # Pregunta para repetir el proceso
            if otra != 's':  # Si el usuario no quiere continuar, el bucle termina
                print(Fore.CYAN + "¡Gracias por usar el generador de contraseñas!")
                break

        except ValueError:
            print(Fore.RED + "Error: Ingrese un número válido.")

if __name__ == "__main__":
    main()

