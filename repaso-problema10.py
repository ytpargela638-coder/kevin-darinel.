#Repaso - problema 10
# Determina cuánto se debe pagar por equis cantidad de lápices considerando que 
# si son 1000 o más el costo es de $0.85; de lo contrario, el precio es de $0.90. 
#---------------------------------------------------------------------------------
#Ingresa la cantidad de lapices
lap=int(input("Cantidad de lapices: "))
#si cantidad de lapices es mayor o igual a 1000 cambia el valor a $0.85 y si no a $0.90
if(lap>=1000):
	total=lap*0.85
else:
	total=lap*0.90
#total
print(f"El total es :{total} ")