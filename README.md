# PROYECTO-INTEGRADOR- SOFTWARE GENERADOR SEGURO DE CONTRASEÑAS
La creciente inseguridad en la web y la urgente necesidad de garantizar una protección informática efectiva resaltan la importancia de contar con contraseñas seguras. Este sencillo pero fundamental paso puede ser determinante para proteger nuestra información contra ciberdelitos y accesos no autorizados. En este contexto, se ha desarrollado un software generador de contraseñas seguras.
El objetivo de este proyecto es diseñar y documentar un sistema capaz de generar contraseñas robustas, siguiendo estrictos estándares de seguridad. Este sistema no solo proporcionará mayor protección a los datos, sino que también garantizará la integridad y confidencialidad de la información almacenada. Basado en una arquitectura cliente-servidor, el sistema utiliza algoritmos criptográficos avanzados para asegurar contraseñas únicas y fuertes. A continuación, se presentarán los diagramas funcionales y arquitectónicos.
En un mundo cada vez más digitalizado, la seguridad de la información personal y profesional se ha convertido en una prioridad crítica. Las contraseñas, aunque constituyen la primera línea de defensa contra accesos no autorizados, siguen siendo un punto vulnerable para muchos usuarios. El uso de contraseñas débiles, repetidas o fácilmente adivinables es un riesgo constante que pone en peligro nuestra privacidad y seguridad en línea.
La solución radica en la creación de contraseñas fuertes y únicas para cada servicio que utilizamos. Sin embargo, esto representa un desafío debido a la gran cantidad de plataformas y la dificultad para recordar tantas contraseñas distintas. Aquí es donde un generador seguro de contraseñas se convierte en una herramienta esencial. No solo genera contraseñas robustas y aleatorias, sino que también facilita su gestión, garantizando una mayor seguridad sin complicaciones.


# EXPLICACIÓN DE LAS PRINCIPALES FUNCIONALIDADES DEL CÓDIGO DEL SOFWARE GENERADOR SEGURO DE CONTRASEÑAS

# 1.	Importación de librerías 
import string
import secrets
 
- string: Proporciona funciones que permiten trabajar con cadenas de caracteres predefinidas como letras, números y caracteres especiales.
- secrets: Un módulo que ofrece funciones para generar números aleatorios criptográficamente seguros, lo cual es ideal para tareas de seguridad como la generación de contraseñas.
  
from colorama import init, Fore
Es una biblioteca que permite dar color a los textos que se imprimen en la terminal o consola.
 -Se debe instalar previamente en python con pip install colorama-
 
# 2.	Definir la función
generar_contraseña(longitud)
Esta función se encarga de generar contraseñas seguras basadas en los requisitos establecidos por el programa.
 def generar_contraseña(longitud):
Recibe como parámetro la longitud deseada para la contraseña.
# 3.	Validación de longitud mínima 
if longitud < 10:
    raise ValueError("La longitud mínima de la contraseña debe ser 10 caracteres.")
La contraseña generada debe tener al menos 10 caracteres. Si el usuario intenta crear una contraseña más corta, se lanza un error.
# 4. Definición de los caracteres disponibles
caracteres_mayusculas = string.ascii_uppercase
caracteres_minusculas = string.ascii_lowercase
caracteres_numeros = string.digits
caracteres_especiales = string.punctuation
Se definen las categorías de caracteres que se usarán para la generación de contraseñas:
•	Letras mayúsculas (A-Z).
•	Letras minúsculas (a-z).
•	Números (0-9).
•	Caracteres especiales (como !, @, #, etc.).
# 5. Generación de la contraseña aleatoria
contraseña = ''.join(secrets.choice(caracteres_mayusculas + caracteres_minusculas + caracteres_numeros + caracteres_especiales) for _ in range(longitud))
Se genera una contraseña aleatoria de la longitud solicitada utilizando la función secrets.choice(). Esta función elige aleatoriamente un carácter de cada una de las categorías definidas (mayúsculas, minúsculas, números, caracteres especiales).
# 6. Validación de requisitos mínimos de la contraseña
Para que la contraseña sea considerada válida, debe cumplir con ciertos requisitos de seguridad, como la inclusión de:
•	Al menos una letra mayúscula.
•	Al menos una letra minúscula.
•	Al menos un número.
•	Al menos un carácter especial.
Estas validaciones se realizan con las siguientes líneas:
tiene_mayuscula = any(c in caracteres_mayusculas for c in contraseña)
tiene_minuscula = any(c in caracteres_minusculas for c in contraseña)
tiene_numero = any(c in caracteres_numeros for c in contraseña)
tiene_especial = any(c in caracteres_especiales for c in contraseña)
Cada una de estas condiciones verifica si la contraseña contiene al menos un carácter de cada tipo.
# 7. Manejo de errores
Si la contraseña generada no cumple con los requisitos de seguridad, se agrega un mensaje de error a la lista errores. Luego, se imprimen los errores:
if errores:
    print("Error: La contraseña generada no cumple con los requisitos de seguridad.")
    for error in errores:
        print("-", error)
    print(f"Faltan {len(errores)} requisitos que deben cumplirse.")
En caso de que falten uno o más requisitos, el programa informará al usuario qué elementos deben corregirse antes de generar una nueva contraseña.
# 8. Generación de una contraseña válida
Si la contraseña cumple con todos los requisitos, se devuelve:
return contraseña
# 9. Función principal main()
Esta función gestiona el flujo del programa:
def main():
    while True:
        try:
            longitud = int(input("Ingrese la longitud de la contraseña deseada (mínimo 10 caracteres): "))
•	Solicita la longitud de la contraseña: El usuario debe ingresar la longitud de la contraseña, con un mínimo de 10 caracteres.
•	Llama a generar_contraseña(longitud): Si la longitud es válida, se genera la contraseña y se muestra al usuario.
# 10. Ciclo de repetición
Después de generar una contraseña, el programa pregunta si el usuario desea generar otra contraseña:
otra = input("¿Desea generar otra contraseña? (s/n): ").strip().lower()
if otra != 's':
    break
Si el usuario responde 's', el proceso se repite; si responde 'n', el programa termina.
11. Manejo de excepciones
Si el usuario ingresa un valor no numérico, se captura el error con un bloque except:
except ValueError:
    print("Error: Ingrese un número válido.")

# 12. Ejecución del programa
Finalmente, el bloque:
if __name__ == "__main__":
    main()
Se asegura de que el código en la función main() se ejecute cuando el archivo se ejecute directamente.

# FUNCIONALIDADES CLAVE

1.	Generación de contraseñas seguras con caracteres aleatorios y válidos (mayúsculas, minúsculas, números, caracteres especiales).
2.	Validación de requisitos para asegurar que la contraseña sea robusta.
3.	Interactividad con el usuario para definir la longitud y repetir el proceso si se desea.
4.	Manejo de errores para garantizar la correcta entrada de datos y la generación de contraseñas seguras.

# CARACTERISTICAS PRINCIPALES DE PYTHON EN EL CÓDIGO

1.	Importación de librerías: Se utiliza el módulo string para manipular cadenas de caracteres y el módulo secrets para generar contraseñas de manera segura utilizando números aleatorios.
2.	Definición de funciones: Python permite definir funciones como generar_contraseña(longitud) para estructurar el código de manera organizada.
3.	Control de flujo:
- Condicionales (if, else): Usados para validar la longitud de la contraseña y verificar los requisitos de seguridad.
- Ciclos (while): Se emplea un ciclo while True para permitir que el usuario genere múltiples contraseñas hasta que decida salir.
4.	Manejo de excepciones: Utiliza el bloque try/except para capturar errores si el usuario ingresa un valor no numérico al solicitar la longitud de la contraseña.
5.	Entrada/Salida: Utiliza la función input() para recibir información del usuario y print() para mostrar mensajes en consola.
6.	Uso de listas y comprensiones de listas: Python permite trabajar con listas y realizar comprensiones de listas para generar contraseñas aleatorias de forma eficiente.

Este código está diseñado para ayudar a generar contraseñas seguras, validando que cumplan con requisitos como el uso de mayúsculas, minúsculas, números y caracteres especiales

