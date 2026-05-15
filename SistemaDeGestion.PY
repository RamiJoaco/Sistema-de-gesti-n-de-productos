# Proyecto- Listas, sublistas, while, for, if, validaciones, menus, funciones basicas de logica.

#Aca se guardan todos los productos que van a ser agregados a la lista grande y sublistas. 
#para hacer la lista grande se crea una variable productos = [] y dentro de los dos corchetes se escribe el nombre del producto, la categoria y el precio. 
#cada producto esta adentro de cada [] y se separan con comas.
productos = [
    ["mouse", "periferico", 120000],
    ["teclado", "periferico", 150000], 
    ["monitor", "pantalla", 200000],
    ["gabinete", "torre", 500000],
    ["parlantes", "audio", 65000],
    ["auriculares", "periferico", 100000],
    ["camara", "periferico", 30000],
    ["microfono", "periferico", 80000],
    ["impresora", "periferico", 250000],
    ]
#Así queda la lista de productos, cada producto tiene su nombre, su categoria y su precio elevado.

#abajo se crea un menú con un while True para que el programa se ejecute hasta que el usuario decida salir.
#Se crean 5 opciones para el usuario, Agregar, Mostrar, Buscar, Eliminar y Salir.
#Esto para que sea mas practico para el usuario y sea mas orientativo al usar el programa.

while True:
    print ("1. Mostrar productos")
    print ("2. Buscar productos")
    print ("3. Agregar producto")
    print ("4. Eliminar producto")
    print ("5. Salir")

#se le pide al usuario que elija una opcion y se guarda en la variable opcion.

    opcion = input ("Elegi una opcion: ")

# sigue un if para validar la opcion elegida por el usuario, si elige 1 se muestra la lista de productos, si elige 2 se muestra un mensaje y si elige 3 se sale del programa
# si elige una opcion no valida se muestra un mensaje de error.
# se crea el contador para mostrar el numero de cada producto en la lista, asi facilitándole al usuario la eliminación de un producto.    
    if opcion == "1":
        contador = 1
# el for recorre toda la lista de productos para mostrar uno por uno al usuario.
        for producto in productos:
            print (f"{contador}. Producto: {producto[0]}, Categoria: {producto[1]}, Precio: {producto[2]}")
            contador += 1
# el contador va incrementando de 1 en 1 para mostrar el numero de cada producto en la lista.


    elif opcion == "2":
        buscar = input ("Ingrese el nombre del producto que desea buscar: ")

# La variable encontrado se crea para verificar si el producto que el usuario esta buscando exista en la lista.
        
        encontrado = False
        for producto in productos:
            if producto[0].lower() == buscar.lower(): 
# El .lower() se utiliza para convertir el nombre del producto a minusculas, esto para que el usuario pueda buscar el producto sin importar si lo escribe con mayusculas o minusculas.
                print(f"producto encontrado: {producto[0]}")
                print(f"Categoria: {producto[1]}")
                print(f"Precio: {producto[2]}")
                encontrado = True
                break

        if encontrado == False:
            print ("Producto no encontrado")
    
    elif opcion == "3":
        nombre = input ("Ingresa el nombre del producto: ")
        categoria = input ("Ingresa la categoria del producto: ")
        precio = int(input ("Ingresa el precio del producto: "))
        productos.append([nombre, categoria, precio])
# El .append() agrega una nueva sublista con los datos del producto final al final de la lista principal

        print ("Producto agregado correctamente")

    elif opcion == "4":
        contador = 1
        for producto in productos:
            print (f"{contador}. Producto: {producto[0]}, Categoria: {producto[1]}, Precio: {producto[2]}")
            contador += 1
        numero = int(input ("Ingrese el numero del producto que desea eliminar: "))
        productos.pop(numero - 1)
#El .pop() elimina un producto de la lista usando el número elegido por el usuario
#Se resta 1 porque las listas en python comienzan en la posicion 0
        print ("Producto eliminado correctamente")

    elif opcion == "5":
        print("Saliendo del programa")
        break

    else:
        print ("Opcion no valida")

