productos = [ "pera" , "manzana" , "kiwi"]

while True:
    fruta_nueva = input("Ingrese nueva fruta o SALIR: ")
    if fruta_nueva.upper() == "SALIR":
        break
    else:
        productos.append(fruta_nueva)

while True:
    print("\nMENU: "
        "\n'L' - listar productos" \
        "\n'A' - agregar producto" \
        "\n'X' - remover productos por nombre" \
        "\n'R' - remover productos por posicion" \
        "\n'P' - ver un producto en particular " \
        "\n'B' - Buscar un producto")

    tecla = input("\nIngrese una Tecla: ")
    
    if tecla.upper() == "L":
        print(productos)
    elif tecla.upper() == "A":
        fruta = input("Ingrese fruta a agregar: ")
        productos.append(fruta)
    elif tecla.upper() == "X":
        elemento = (input("Ingrese una elemento a quitar: "))
        productos.remove(elemento)      
    elif tecla.upper() == "R":
        posicion = int(input("Ingrese una posicion: "))
        productos.pop(posicion)
    elif tecla.upper() == "P":
        posicion = int(input("Ingrese una posicion: "))
        print(f"producto en posicion {posicion} es {productos[posicion]}")
    elif tecla.upper() == "B":
        buscar = input("Ingrese fruta a buscar: ")
        if buscar in productos:
            print(f"{buscar} esta dentro de la lista")
        else:
            print(f"{buscar} no esta dentro de la lista")
    else:
        break