#Tarea 1
# El director de una escuela está organizando un viaje de estudios, 
# y requiere determinar cuánto debe cobrar a cada alumno y cuánto debe pagar a la 
# compañía de viajes por el servicio. La forma de cobrar es la siguiente: 
# si son 100 alumnos o más, el costo por cada alumno es de $65.00; de 50 a 99 alumnos, 
# el costo es de $70.00, de 30 a 49, de $95.00, y si son menos de 30, el costo de la renta 
# del autobús es de $4000.00, sin importar el número de alumnos. 
#------------------------------------------------------------------------------------------

# La instrucción 'try' se usa para "probar" un bloque de código y prevenir
# que el programa se detenga drásticamente si el usuario ingresa un dato incorrecto.
try:
    #  Pedimos al usuario el número de alumnos.

    cantidad_alumnos = int(input("¿Cuál es la cantidad de alumnos?: "))

    # verificamos si la cantidad ingresada es válida (mayor a cero)
    if cantidad_alumnos <= 0:
        print("Error: El número de alumnos debe ser mayor a cero.")

    #  si la cantidad es válida, procede a calcular el presupuesto.
    else:
        # si son 100 o más alumnos, cada uno paga $65.
        if cantidad_alumnos >= 100:
            costo_por_alumno = 65
            total = cantidad_alumnos * costo_por_alumno

        # si son entre 50 y 99 alumnos, cada uno paga $70.
        elif cantidad_alumnos >= 50:
            costo_por_alumno = 70
            total = cantidad_alumnos * costo_por_alumno

        # si son entre 30 y 49 alumnos, cada uno paga $95.
        elif cantidad_alumnos >= 30:
            costo_por_alumno = 95
            total = cantidad_alumnos * costo_por_alumno

        # si son menos de 30 alumnos, el costo fijo total del autobús es de $4000,
        # por lo que el costo individual se calcula dividiendo los $4000 entre los alumnos presentes.
        else:
            total = 4000
            costo_por_alumno = total / cantidad_alumnos

        # 4. Imprimimos el resultado formateado en pantalla.
    
        print(f"Costo total del autobús: ${total:,.2f}")
        print(f"Costo a pagar por cada alumno: ${costo_por_alumno:,.2f}")

#si el usuario ingresa un simbolo que no es adecuado marca error
except :
    print("Error: Solo puedes ingresar números enteros positivos.")