
registro_compras = float(input("Ingrese la cantidad de artículos: "))   
if registro_compras < 0:
    print("Error: La cantidad de artículos no puede ser negativa.") 
else:
    print (f"La cantidad de artículos es: {registro_compras}")  


registro_compras = float(input("Ingrese el monto total de la compra: "))
if registro_compras < 0:
    print("Error: El monto no puede ser negativo.") 
else:
    print(f"El monto de la compra es: ${registro_compras:.2f}") 

    #acumulador de compras
    acumulador_compras = 0  
    acumulador_compras += registro_compras
    print(f"El total acumulado de compras es: ${acumulador_compras:.2f}")   

    
    monto_definido = 100.00
    if registro_compras > monto_definido:   
        print(f"La compra de ${registro_compras:.2f} supera el monto definido de ${monto_definido:.2f}.")

while True:
    continuar = input("¿Desea registrar otra compra? (s/n): ").lower()
    if continuar == 's':
        registro_compras = float(input("Ingrese la cantidad de artículos: "))   
        if registro_compras < 0:
            print("Error: La cantidad de artículos no puede ser negativa.") 
        else:
            print (f"La cantidad de artículos es: {registro_compras}")  

        registro_compras = float(input("Ingrese el monto total de la compra: "))
        if registro_compras < 0:
            print("Error: El monto no puede ser negativo.") 
        else:
            print(f"El monto de la compra es: ${registro_compras:.2f}") 

            acumulador_compras += registro_compras
            print(f"El total acumulado de compras es: ${acumulador_compras:.2f}")   

            if registro_compras > monto_definido:   
                print(f"La compra de ${registro_compras:.2f} supera el monto definido de ${monto_definido:.2f}.")
    elif continuar == 'n':
        break
    else:
        print("Opción inválida. Por favor, ingrese 's' para sí o 'n' para no.")

print(f"Resumen de compras: \nCantidad de artículos: {registro_compras}\nMonto total: ${registro_compras:.2f}\nTotal acumulado: ${acumulador_compras:.2f}")     
