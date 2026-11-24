#Repaso - problema 14
# La política de la compañía telefónica "chimefón” es: "Chismea + x -". 
# Cuando se realiza una llamada, el cobro es por el tiempo que ésta dura, 
# de tal forma que los primeros cinco minutos cuestan $1.00 peso c/u,
# los siguientes tres, 80 centavos de peso c/u, los siguientes dos 
# minutos, 70¢ centavos de peso c/u, y a partir del décimo minuto, 50 centavos de peso c/u.
# Además, se carga un impuesto de 3% cuando es domingo, y si es día hábil, 
# en turno matutino, 15%, y en turno vespertino, 10 %. Realice un algoritmo para 
# determinar cuánto debe pagar por cada concepto una persona que realiza una llamada en 
# moneda nacional mexicana (MXN).   
#--------------------------------------------------------------------------------------
print("Chimefon")
minutos=int(input("Ingrese los minutos de llamada: "))
dia=str(input("Ingrese el dia: (domingo o habil)"))
if minutos <= 5:
	costo=minutos*1
elif minutos > 5 and minutos <= 8:
	costo=(3*0.80)+5
elif minutos > 8 and minutos <=10:
	costo=(2*0.70)+2.4+5
elif minutos > 10:
	costo=(minutos*0.50)+2.4+5-7

if dia == "domingo":
	impuesto=costo*0.03
	costototal=impuesto+costo

if dia == "habil":
	turno=str(input("Ingrese el turno (matutino o vespertino):"))
	if turno=="matutino":
		impuesto=costo*.15
		costototal=costo+impuesto
	elif turno=="vespertino":
		impuesto=costo*.10
		costototal=costo+impuesto

print("El costo es: ",costototal)