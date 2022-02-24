dias = float(input("Escriba los días laborados: "))
pago = float(input("Escriba el pago por día: "))

#PROCESOS
pagobruto = dias * pago 
ivatraslado = pagobruto * 0.16
subtotal = pagobruto + ivatraslado
ivaretenido = pagobruto * 0.106666
isrretenido = pagobruto * 0.1
Pagoneto = subtotal - ivaretenido - isrretenido
#SALIDAS
print("El desglose del salario es el siguiente:")
print(f"El pago bruto es de= {pagobruto}")
print(f"El iva trasladado es de= {ivatraslado}")
print(f"El subtotal es de= {subtotal}")
print(f"El subtotal es de= {ivaretenido}")
print(f"El subtotal es de= {isrretenido}")
print(f"Su pago neto es de= {Pagoneto}")