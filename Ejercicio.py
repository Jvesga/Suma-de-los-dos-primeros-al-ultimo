"""Programa que calcula si la suma de los dos primeros numeros es igual al ultimo """

print("------------------------------------------------------------------------------------")
print("--Programa para calcular si la suma de los dos primeros numeros es igual al ultimo--")
print("------------------------------------------------------------------------------------")

# input

a = int(input("-Ingrese el valor del primer numero:"))
b = int(input("-Ingrese el valor del segundo numero:"))
c = int(input("-Ingrese el valor del ultimo numero:"))

# processing
if c == a + b:
    msj = "-La suma de los dos primeros numeros es ingual al ultimo "
 
else:
    msj = "-La suma de los dos primeros numeros no es igual al ultimo"

# output

print(msj)
