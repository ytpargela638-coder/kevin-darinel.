#Repaso - problema 7
# Determina cuánto pagará finalmente una persona por un artículo equis, 
# considerando que tiene un descuento de 20%, y debe pagar 15% de 
# IVA (debe mostrar el precio con descuento y el precio final).
# Crea un menú para que el usuario elija entre 2 productos y el que elija, 
# despliegua el nombre de producto, precio, precio con descuento y precio final.
#-------------------------------------------------------------------------------
print("=== MENÚ DE PRODUCTOS ===")
print("1. computadora ($22,000)")
print("2. celular ($9,000)")

opcion = input("\nElige una opción (1 o 2): ")

if opcion == "1":
    nombre = "computadora"
    precio = 22000
elif opcion == "2":
    nombre = "celular"
    precio = 9000
else:
    nombre = None
    print("Opción no válida.")

if nombre:
    # Cálculos sencillos
    precio_descuento = precio * 0.80      # Aplicar el 20% de descuento
    precio_final = precio_descuento * 1.15  # Agregar el 15% de IVA

    # Resultados
    print(f"\nProducto: {nombre}")
    print(f"Precio original: ${precio}")
    print(f"Precio con descuento (20%): ${precio_descuento}")
    print(f"Precio final con IVA (15%): ${precio_final}")