
nivel = int(input("Escriba el nivel de agua en metros: "))
if(nivel < 0 ):
    print("fuga de cisterna")
elif(nivel == 0):
    print("encender boomba de agua")
elif(nivel > 0 and nivel <= 2):
    print("acelerar bomba de agua")
elif(nivel > 2 and nivel <= 4):
    print("bomba de agua trabajando")
elif(nivel > 4 and nivel< 6):
    print("desacelerar bomba de agua")
elif(nivel == 6):
    print("apagar bomba de agua")
elif(nivel > 6):
    print("desbordamiento de agua de cistena")
