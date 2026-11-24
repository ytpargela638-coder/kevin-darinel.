#Repaso - problema 12
# "La langosta ahumada" es una empresa dedicada a ofrecer banquetes; 
# sus tarifas son las siguientes: el costo de platillo por persona es 
# de $95.00, pero si el número de personas es mayor a 200 pero menor o igual a 300, 
# el costo es de $85.00. Para más de 300 personas el costo por platillo es de $75.00. 
# Se requiere un algoritmo que ayude a determinar el presupuesto que se debe presentar 
# a los clientes que deseen realizar un evento.  
#--------------------------------------------------------------------------------------

#Ingresa la cantidad de personas
pers=int(input("Ingresa el numero de personas: "))
#si son mayor de 200 personas o menor o igual a 300 el platillo vale $85
if(pers>200 or pers<=300):
	total=pers*85
#si son mayor a 300 personas el platillo vale $75
if(pers>300):
	total=pers*75
	# y si es menor a 200 a $95
else:
	total=pers*95
#resultado
print("El presupuesto es de: ",total)