import csv


##################################################################### 1

def conseguir_productos(nombre_archivo):
    with open(nombre_archivo, "r", encoding = "utf-8") as archivo:
        listado = []
        archivo.readline().strip("\n").split(",")     
        for linea in archivo.readlines():
            producto = {}
            linea = linea.strip("\n").split(",")
            id, nombre_producto, precio, unidades_vendidas,stock = linea
            producto["id"] = int(id)
            producto["producto"] = nombre_producto
            producto["precio"] = float(precio)
            producto["unidades_vendidas"] = int(unidades_vendidas)
            producto["stock"] = int(stock)
            listado.append(producto)
    return listado



##################################################################### 2


def mostrar_listado(listado):
    tam = len(listado)
    print("                   ***lista de productos***")
    print()
    print("|ID|      |producto|            |precio|      |unidades vendidas|     |stock|")
    print("------------------------------------------------------------------------------------------")
    for i in range(tam):
        mostrar_producto(listado[i])
    print()

def mostrar_producto(producto: list):
    print(f"{producto['id']:<6}    {producto['producto']:<24}  {producto['precio']:<14}  {producto['unidades_vendidas']:<16} {producto['stock']:.2f}")



##################################################################### 3



############# stock



def asignar_stock(listado):
    from random import randint
    lista_con_stock = []
    for producto in listado:
        producto["stock"] = randint(50, 300)
        lista_con_stock.append(producto["stock"])
    return lista_con_stock
    

def mostrar_stock(lista, dato):
    print(f"id                               {dato}")
    for i in lista:
        print(f"{i['id']:<30}       {i[dato]} en stock")




############ ventas



def asignar_ventas(listado):
    from random import randint
    lista_con_ventas = []
    for producto in listado:
        producto["unidades_vendidas"] = randint(1, 100)
        lista_con_ventas.append(producto["unidades_vendidas"])
    return lista_con_ventas
    

def mostrar_ventas(lista, dato):
    print(f"id                               {dato}")
    for i in lista:
        print(f"{i['id']:<30}       {i[dato]} vendidas")



###########  precios

def asignar_precio(listado):
    from random import randint
    lista_con_precio = []
    for producto in listado:
        producto["precio"] = randint(1000, 10000)
        lista_con_precio.append(producto["precio"])
    return lista_con_precio
    

def mostrar_precio(lista, dato):
    print(f"id                               {dato}")
    for i in lista:
        print(f"{i['id']:<30}       {i[dato]} pesos")



##################################################################### 4

def mas_vendidos(listado):
    lista_filtrada = []
    for producto in listado:  
        if producto["unidades_vendidas"] >= 50:
            lista_filtrada.append(producto)  
    return lista_filtrada



def crear_archivo_mas_vendidos(lista):
    

    with open('mas vendidos', 'w', newline='') as archivo_csv:
        escritor = csv.writer(archivo_csv)
        
        for elemento in lista:
            escritor.writerow([elemento])

    print("Archivo -mas vendidos- creado exitosamente.\n")



def mostrar_mas_vendidos(lista, dato):
    print(f"producto                              {dato}")
    for i in lista:
        print(f"{i['producto']:<30}       {i[dato]}")





##################################################################### 5




def bajo_stock(listado):
    lista_filtrada = []
    for producto in listado:  
        if producto["stock"] <= 200:
            lista_filtrada.append(producto)  
    return lista_filtrada



def crear_archivo_bajo_stock(lista):
    

    with open('bajo stock', 'w', newline='') as archivo_csv:
        escritor = csv.writer(archivo_csv)
        
        for elemento in lista:
            escritor.writerow([elemento])

    print("Archivo -bajo stock- creado exitosamente.\n")



def mostrar_bajo_stock(lista, dato):
    print(f"producto                              {dato}")
    for i in lista:
        print(f"{i['producto']:<30}       {i[dato]}")



##################################################################### 6


def mostrar_promedio(listado):
    cantidad = 0
    total = 0 
    for producto in listado:
        precio = producto["precio"]
        id = producto["id"]

        if id in listado:
            cantidad += 1
            total += precio 
        else:
            cantidad += 1
            total += precio 
        
    promedio = total/cantidad
    
    print("\n el promedio de precios es: " + str(promedio)+ " pesos")


##################################################################### 7  


def ordenar_alfabeticamente(listado):
    listado_ordenado = sorted(listado, key=lambda x: (x['producto']))
    return listado_ordenado




##################################################################### 8


def producto_mas_vendido(listado, valor):
    mas_vendido = 0
    producto_mas_vendido = None
    producto = True
    for i in listado:
        if producto or i[valor] > mas_vendido:
            mas_vendido = i[valor]
            producto_mas_vendido = i
            producto = False
    return producto_mas_vendido

def mostrar_mas_exitoso(listado, valor):
    print("\n")
    print("producto mas vendido")
    print(f"producto: {listado['producto']} | {valor}: {listado[valor]}")
