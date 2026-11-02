# 1. Solicitar al usuario el nombre del producto, precio, cantidad y porcentaje de impuesto
producto = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese la cantidad: "))
porcentaje_impuesto = float(input("Ingrese el porcentaje de impuesto: "))

# 2. Calcular subtotal, impuesto y total
subtotal = round(precio * cantidad, 2)
impuesto = round(subtotal * (porcentaje_impuesto / 100), 2)
total = round(subtotal + impuesto, 2)

# 3. Imprimir el recibo de compra
print("\n==================================")
print("         RECIBO DE COMPRA         ")
print("==================================")
print(f"Producto:           {producto}")
print(f"Precio unitario:    ${precio:.2f}")
print(f"Cantidad:           {cantidad}")
print("----------------------------------")
print(f"Subtotal:           ${subtotal:.2f}")
print(f"Impuesto ({porcentaje_impuesto}%):    ${impuesto:.2f}")
print(f"TOTAL A PAGAR:      ${total:.2f}")
print("==================================")