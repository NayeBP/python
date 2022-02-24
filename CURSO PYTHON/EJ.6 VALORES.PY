#Obtener valores para: a, b y c. Calcular la fórmula general.
#ENTRADAS
import math

a = float (input("Escribe el valor de a: "))
b = float(input("Escribe el valor de b: "))
c = float(input("Escribe el valor de c: "))

#PROCESOS
x1 = (-b+((b*b)-(4*a*c))**1/2)/(2*a)
x2 = (-b-((b*b)-(4*a*c))**1/2)/(2*a)

#SALIDAS
print(f"El valor de x1 es: {x1}")
print(f"El valor de x2 es: {x2} ")
