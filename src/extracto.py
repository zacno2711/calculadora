ingresos = []
egresos = []

accion = 0
totalIngresos = 0
totalEgresos = 0

while accion!= 3:
    accion = int(input("Ingrese una opcion: \n1. Ingresos \n2. Egresos \n3. Salir \n"))
    if accion == 1:
        ingresos.append(float(input("Ingrese un ingreso: ")))
    elif accion == 2:
        egresos.append(float(input("Ingrese un egreso: ")))
    elif accion == 3:
        for ingreso in ingresos:
          totalIngresos += ingreso

        for egreso in egresos:
          totalEgresos += egreso

        print( totalIngresos - totalEgresos)  
        break