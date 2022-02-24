from platform import processor


#Determinar la edad de una persona conociendo el año actual y el año de nacimiento.
#ENTRADAS
nacimiento = int(input("¿En qué año naciste?: "))
añoactual = int(input("¿En qué año te encuentras?: "))

#PROCESOS
edad =  añoactual - nacimiento

#SALIDAS
print(f"Tu edad es de: {edad}")


