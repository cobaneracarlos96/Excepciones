#Escribe un programa que intente abrir un archivo que no existe. Si se produce una excepción
#FileNotFoundError, captura la excepción y muestra un mensaje de error al usuario. Sin embargo,
#tambien intenta crear el archivo si no existe.

nombre_archivo = "archivo_ejemplo.txt"

try: 
    #Intenta abrir el archivo modo lectura
    with open(nombre_archivo, "r")as archivo:
        contenido = archivo.read()
        print ("Contenido del archivo:")
        print(contenido)

except FileNotFoundError:
    print (f"Error: El archivo '{nombre_archivo}'no existe.")

    # Intenta crear el archivo
    try:
        with open(nombre_archivo, "w") as archivo:
            archivo.write("Este archivo ha sido creado porque no existía.\n")
            print(f"Se ha creado el archivo '{nombre_archivo}'exitósamente.")
    except Exception as e:
        print (f"Ocurrió un error al crear el archivo: {e}")


