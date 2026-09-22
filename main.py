#Menu con 5 opciones: Listar, Remover, Agregar, Salir y Buscar
productos = ["Cerveza", "Pepsi", "Coca", "Fanta"]
contador_de_errores = 0

while True:
    opciones = input("-----------------------------\n"
                    "**** Menu de opciones **** \n\n"
                    "       'L' - Listar\n"
                    "       'R' - Remover por nombre\n"
                    "       'X' - Remover por indice\n"
                    "       'A' - Agregar\n"
                    "       'B' - Buscar\n"
                    "       'S' - Salir\n"
                    "-----------------------------\n"
                    "Ingrese una letra: ")
    
    #Comienza menu de opciones
    #Opcion para Listar
    if opciones.strip().upper() == "L":
            contador_de_errores = 0
            print("\nListado de productos:")
            for i, producto in enumerate(productos):
                print(f"{i}.{producto}")

    #Opcion para Remover un producto por nombre
    elif opciones.strip().upper() == "R":
        contador_de_errores = 0
        producto_removido = input("Ingrese producto a remover:\n")
        producto_removido_limpio = producto_removido.strip().capitalize()
        if producto_removido_limpio in productos:
            productos.remove(producto_removido_limpio)
            print(f"{producto_removido_limpio} removido con exito.\n")
        else:
            print(f"No se pudo remover {producto_removido_limpio} porque no pertenecia a la lista.\n")

    # #Opcion para Remover un producto por posicion
    elif opciones.strip().upper() == "X":
        contador_de_errores = 0
        entrada = input("Ingrese indice a remover:\n").strip()
        if not entrada.isdigit():
            print("Por favor ingrese un número válido.\n")
        else:
            indice_removido = int(entrada)
            if indice_removido < len(productos):
                producto_removido_limpio = productos[indice_removido]
                productos.pop(indice_removido)
                print(f"producto '{indice_removido}.{producto_removido_limpio}' removido con exito.\n")
            else:
                print(f"No se pudo remover '{indice_removido}' porque no pertenecia a la lista.\n")    

    #Opcion para Agregar un producto
    elif opciones.strip().upper() == "A":
        contador_de_errores = 0
        producto_agregado = input("Ingrese producto a agregar:\n")
        producto_agregado_limpio = producto_agregado.strip().capitalize()
        if producto_agregado_limpio in productos:
            print(f"El producto {producto_agregado_limpio} ya pertenece a la lista.\n")
        else:
            productos.append(producto_agregado_limpio)
            print(f"{producto_agregado_limpio} agregado con exito.\n")

    #Opcion para Buscar un producto
    elif opciones.strip().upper() == "B":
        contador_de_errores = 0
        producto_buscado = input("Ingrese producto a buscar:\n")
        producto_buscado_limpio = producto_buscado.strip().capitalize()
        if producto_buscado_limpio in productos:
            print(f"Producto encontrado, hay {producto_buscado_limpio}.\n")
        else:
            print(f"Perdon, no tenemos {producto_buscado_limpio}.\n")

    #Opcion para Salir
    elif opciones.strip().upper() == "S":
        print("Saliendo...")
        break

    #Opcion por si no ingresa una opcion dentro del menu
    else:
        print("Por favor ingrese alguna de la opciones dentro del menu.\n")
        contador_de_errores += 1
        if contador_de_errores > 5:
            print(f"contador de errores: {contador_de_errores}")
            print("Si ingresa varios errores seguidos el programa se cerrara.\n")
            if contador_de_errores == 10:
                print("Saliendo...")
                break
print(f"Gracias por usar nuestra aplicacion.")
