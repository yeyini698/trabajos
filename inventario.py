
productos_futbol = []
balon_de_futbol = {"nombre": "Balón de fútbol", "precio": 25.00, "cantidad": 10, "codigo": "BF001"}
productos_futbol.append(balon_de_futbol)
tacos_de_futbol = {"nombre": "Tacos de fútbol", "precio": 50.00, "cantidad": 5, "codigo": "TF002"}
productos_futbol.append(tacos_de_futbol)   
jersey_de_futbol = {"nombre": "Jersey de fútbol", "precio": 30.00, "cantidad": 8, "codigo": "JF003"}
productos_futbol.append(jersey_de_futbol)  

productos_basquetbol = []
balon_de_basquetbol = {"nombre": "Balón de básquetbol", "precio": 28.00, "cantidad": 12, "codigo": "BB001"}
productos_basquetbol.append(balon_de_basquetbol) 
tenis_de_basquetbol = {"nombre": "Tenis de básquetbol", "precio": 60.00, "cantidad": 6, "codigo": "TB002"}
productos_basquetbol.append(tenis_de_basquetbol)        
camiseta_de_basquetbol = {"nombre": "Camiseta de básquetbol", "precio": 35.00, "cantidad": 10, "codigo": "CB003"}
productos_basquetbol.append(camiseta_de_basquetbol) 

productos_NFL = []
balon_de_NFL = {"nombre": "Balón de NFL", "precio": 30.00, "cantidad": 15, "codigo": "BN001"}
productos_NFL.append(balon_de_NFL)  
tacos_de_futbol_americano = {"nombre": "Tacos de fútbol americano", "precio": 55.00, "cantidad": 7, "codigo": "TF002"}
productos_NFL.append(tacos_de_futbol_americano) 
jersey_de_NFL = {"nombre": "Jersey de NFL", "precio": 40.00, "cantidad": 9, "codigo": "JN003"}
productos_NFL.append(jersey_de_NFL) 


mostar_inventario = input("¿Desea mostrar el inventario inicial? (s/n): ").lower()
if mostar_inventario == 's':
    print("\nInventario de productos de fútbol:")
    for producto in productos_futbol:
        print(f"Código: {producto['codigo']}, Nombre: {producto['nombre']}, Precio: ${producto['precio']:.2f}, Cantidad: {producto['cantidad']}")

    print("\nInventario de productos de básquetbol:")
    for producto in productos_basquetbol:
        print(f"Código: {producto['codigo']}, Nombre: {producto['nombre']}, Precio: ${producto['precio']:.2f}, Cantidad: {producto['cantidad']}")

    print("\nInventario de productos de NFL:")
    for producto in productos_NFL:
        print(f"Código: {producto['codigo']}, Nombre: {producto['nombre']}, Precio: ${producto['precio']:.2f}, Cantidad: {producto['cantidad']}")


while True:
    agregar_producto = input("¿Desea agregar un producto? (s/n): ").lower()
    if agregar_producto == 's':
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))
        codigo = input("Ingrese el código del producto: ")
        categoria = input("Ingrese la categoría del producto (futbol, basquetbol, NFL): ").lower()

        nuevo_producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad, "codigo": codigo}

        if categoria == "futbol":
            productos_futbol.append(nuevo_producto)
        elif categoria == "basquetbol":
            productos_basquetbol.append(nuevo_producto)
        elif categoria == "nfl":
            productos_NFL.append(nuevo_producto)
        else:
            print("Categoría inválida. El producto no se agregó.")

    elif agregar_producto == 'n':
        break   

    eliminar_producto = input("¿Desea eliminar un producto? (s/n): ").lower()
    if eliminar_producto == 's':    
        
        codigo_eliminar = input("Ingrese el código del producto a eliminar: ")
        encontrado = False

        for categoria in [productos_futbol, productos_basquetbol, productos_NFL]:
            for producto in categoria:
                if producto["codigo"] == codigo_eliminar:
                    categoria.remove(producto)
                    encontrado = True
                    print(f"Producto con código {codigo_eliminar} eliminado.")
                    break
            if encontrado:
                break

        if not encontrado:
            print(f"No se encontró un producto con código {codigo_eliminar}.")

            modificar_producto = input("¿Desea modificar un producto? (s/n): ").lower()
            if modificar_producto == 's':   
                
                codigo_modificar = input("Ingrese el código del producto a modificar: ")
                encontrado = False

                for categoria in [productos_futbol, productos_basquetbol, productos_NFL]:
                    for producto in categoria:
                        if producto["codigo"] == codigo_modificar:
                            nuevo_nombre = input("Ingrese el nuevo nombre del producto: ")
                            nuevo_precio = float(input("Ingrese el nuevo precio del producto: "))
                            nueva_cantidad = int(input("Ingrese la nueva cantidad del producto: "))

                            producto["nombre"] = nuevo_nombre
                            producto["precio"] = nuevo_precio
                            producto["cantidad"] = nueva_cantidad

                            encontrado = True
                            print(f"Producto con código {codigo_modificar} modificado.")
                            break
                    if encontrado:
                        break

                if not encontrado:
                    print(f"No se encontró un producto con código {codigo_modificar}.")

reportar_inventario = input("¿Desea reportar el inventario? (s/n): ").lower()
if reportar_inventario == 's':  

    print("\nInventario de productos de fútbol:")
    for producto in productos_futbol:
        print(f"Código: {producto['codigo']}, Nombre: {producto['nombre']}, Precio: ${producto['precio']:.2f}, Cantidad: {producto['cantidad']}")

    print("\nInventario de productos de básquetbol:")
    for producto in productos_basquetbol:
        print(f"Código: {producto['codigo']}, Nombre: {producto['nombre']}, Precio: ${producto['precio']:.2f}, Cantidad: {producto['cantidad']}")

    print("\nInventario de productos de NFL:")
    for producto in productos_NFL:
        print(f"Código: {producto['codigo']}, Nombre: {producto['nombre']}, Precio: ${producto['precio']:.2f}, Cantidad: {producto['cantidad']}")

