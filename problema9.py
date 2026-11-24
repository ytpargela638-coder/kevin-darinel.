#Repaso - problema 9
# Determina el promedio que obtendrá un alumno considerando que realiza tres exámenes, 
# de los cuales el primero y el segundo tienen una ponderación de 25%, mientras que 
# el tercero de 50%. 
#----------------------------------------------------------------------------------------
cal1=float(input("Ingresa la primera calificación"))
cal2=float(input("Ingresa la primera calificación"))
cal3=float(input("Ingresa la primera calificación"))
prom1=cal1*.25
prom=cal2*.25
prom3=cal3*.5
resultado=prom1+prom+prom3
print("Tu promedio es: ",resultado)