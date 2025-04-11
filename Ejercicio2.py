# Escribe un programa que intente sumar un número y una cadena. Si se produce un error
# de tipo, captura la excepción TypeError y muestra un mensaje de error al usuario.

try:
    numero = 100
    cadena = 'Hola Pepito'

    resultado = numero + cadena
    print (f"El resultado es: {resultado}")

except TypeError:
    print ("'Error' : No se puede sumar un numero con una cadena")