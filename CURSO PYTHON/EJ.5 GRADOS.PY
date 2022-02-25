#Pedir la cantidad de grados y convertirlos a °C, °F y K.
#ENTRADAS
from pickletools import OpcodeInfo


print("1. De Kelvin a Celsius")
print("2. De Fahrenheit a Celsius")
print("3. De Celsius a Kelvin")
print("4. De Kelvin a Fahrenheit")
print("5. De Fahrenht a Kelvin")
print("6. De Celsius a Fahrenht")
opcion = int(input("Escribe el número dependiendo la opcion que buscas:"))
grados = int(input("Escribe los grados: "))

#SALIDAS
if(opcion == 1):
    c = grados - 273.5
    print(f"°C= {c}")
elif (opcion == 2):
    c = (5 * (grados - 32)) / 9
    print(f"°C= {c}")
elif (opcion == 3):
    k = grados - 273.5
    print(f"°C= {k}")
elif (opcion == 4):
    f = ((9*(grados-273.15))/5)+32
    print(f"°F = {f}")
elif (opcion == 5):
    k =(5*(grados-32)/9)+273.15
    print(f"°K= {k}")
elif (opcion == 6):
    f = (9*grados/5)+32
    print(f"°F= {f}")