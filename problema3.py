#Repaso - problema 3
# Un estacionamiento requiere determinar el cobro que debe aplicar 
# a las personas que lo utilizan. Considere que el cobro es con base 
# en las horas que lo disponen y que las fracciones de hora se toman como completas.
#-------------------------------------------------------------------------------------- 
import math

minutos_estancia=float(input("Ingresa los minutos de estancia:  "))
precio_hora=20
redondeo=math.ceil(minutos_estancia/60)
cobro=precio_hora*redondeo
print(f"Su pago es: {cobro}")
