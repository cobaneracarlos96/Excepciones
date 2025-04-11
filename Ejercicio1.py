# Escribe un programa que intente dividir dos números. Si el segundo número es cero,
# captura la excepción ZeroDivisionError y muestra un mensaje de error al usuario.

try: 
    # Se le pide al usuario que ingrese dos números
    num1 = float (input("Ingrese el primer número:"))
    num2 = float (input("Ingrese el segundo número:"))

 
    resultado = num1 / num2 
    print (f" EL resultado de la división es: {resultado}")

except ZeroDivisionError:
    print ("'Error': No se puede dividir por cero.")
