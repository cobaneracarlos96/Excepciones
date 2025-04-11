# Escribe un programa que intente acceder a una clave que no existe en un
# diccionario. Si se produce una excepción KeyError, captura la excepción y muestra

datos = {
    "nombre" : "Diego",
    "edad" :30
}

try:
    valor = datos ["direccion"]
    print (f"la direccion es: {valor}")

except KeyError:
    print ("'Error': direccion NO existe en el diccionario")