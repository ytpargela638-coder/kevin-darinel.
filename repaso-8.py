# Repaso - problema 8
# Almacenes "El harapiento distinguido" tiene una promoción: 
# a todos los trajes que tienen un precio superior a $2500.00 se les 
# aplicará un descuento de 15%, a todos los demás se les aplicará sólo 8%. 
# Realice un algoritmo para determinar el precio final que debe pagar una persona 
# por comprar un traje y de cuánto es el descuento que obtendrá.
#-----------------------------------------------------------------------------
print("El herapiento distinguido")
val_traje=int(input("Ingresa el valor del traje: "))
if(val_traje>2500.00):
	des=val_traje*0.15
	total=val_traje-des
else:
	
	des=val_traje*0.08
	total=val_traje-des

print("El descuento es: ",des)
print("El total con descuento: ",total)