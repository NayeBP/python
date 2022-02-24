#Calcular el promedio de 3 calificaciones y decir si es aprobado o reprobado.
#ENTRADAS
calificacion1 = int(input("Escriba la primera calificación: "))
calificacion2 = int(input("Escriba la segunda calificación: "))
calificacion3 = int(input("Escriba la tercera calificación: "))

#PROCESOS
multiplicacion = (calificacion1+calificacion2+calificacion3)
calificaciones = 3
promedio= (multiplicacion / calificaciones)

#SALIDAS
print(f"El promedio del alumno es: {promedio}")
if(promedio >= 6):
    print("APROBADO")
else: #elif (calificacion < 6):
    print("REPROBADO")