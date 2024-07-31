from funciones import *


while True:
    respuesta = input(
        
        "Menu\n"
        "1- Cargar productos.CSV\n"
        "2- Imprimir listado \n"
        "3- Asignar stock/precio/ventas \n"
        "4- Mostrar los mas vendidos \n"
        "5- Mostrar el stock bajo\n"
        "6- Mostrar promedio de precio\n"
        "7- Ordenar alfabeticamente\n"
        "8- Mostrar producto mas vendido\n"
        "9- Salir\n"
        "Ingrese una opcion: "
        
        )
    

    
    if respuesta == "1":
        listado = conseguir_productos("productos.csv")
        print("\n listado cargado correctamente\n" )
    elif respuesta == "2":
        mostrar_listado(listado)
    elif respuesta == "3":
        asignar_stock(listado)
        asignar_ventas(listado)
        asignar_precio(listado)

        mostrar_stock(listado,"stock")
        print("\n")
        print("\n")
        mostrar_precio(listado,"precio")
        print("\n")
        print("\n")
        mostrar_ventas(listado,"unidades_vendidas")
    elif respuesta == "4":
        print("\n")
        lista_mas_vendida = mas_vendidos(listado)
        mostrar_mas_vendidos(lista_mas_vendida, "unidades_vendidas")
        crear_archivo_mas_vendidos(lista_mas_vendida)
    elif respuesta == "5":
        print("\n")
        lista_bajo_stock = bajo_stock(listado)
        mostrar_bajo_stock(lista_bajo_stock, "stock")
        crear_archivo_bajo_stock(lista_bajo_stock)
    elif respuesta == "6":
        mostrar_promedio(listado)
    elif respuesta == "7":
        listado_ordenado = ordenar_alfabeticamente(listado)
        mostrar_listado(listado_ordenado)
    elif respuesta == "8":
        mas_vendido = producto_mas_vendido(listado, "unidades_vendidas")
        mostrar_mas_exitoso(mas_vendido,"unidades_vendidas")
    elif respuesta == "9":
        break


    


