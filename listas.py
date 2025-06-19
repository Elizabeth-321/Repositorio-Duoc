#uso ejemplo listas
#######################################################
# lista=[2,2,4,1,5]
# print(lista)

         #-5-4-3-2-1
# numeros=[2,3,4,5,6]   #Se debe poner corchete para ver el numero comienza en 0 ej: 2:0 3:1 4:2  5:3 como en este caso 6:4
#         #0,1,2,3,4

# print(numeros[3])
         #-5-4-3-2-1
# numeros=[2,3,4,5,6]   #Se debe poner corchete para ver el numero comienza en 0 ej: 2:0 3:1 4:2  5:3 
# #         #0,1,2,3,4
# # print(numeros[-3])
# for numero in numeros :
#     print("numero",numero*2)

# nombres=["eli", "ale", "ana","victor"]
# print(nombres[-2]) # si pones 2 igual sale lo mismo
#######################################################
#funciones para listas
#append   #append siempre agrega un elemnt0 al final de la lista

# nombres=["eli", "ale", "ana","victor"]
# print(nombres)
# nombres.append("eli")   #append siempre agrega un elemnt0 al final de la lista
# print(nombres)

#////////////////////////////////////////////////////////////
#hacer un programa donde se deba ingresar un nombre y mostrar nombre (en menu)debe ser la misma cantidad de nombre y apellidos
#print nombres
# n=["eli","ale", "ana"]
# a=["lagos", "pino","teran"]

# c=0  #contador
# for i in a:
#   print(n[c], a[c])

# name=[] 
# ape=[]
# while True:
#     print('''

#     1.-Ingresar nombre
#     2.-Mostrar nombre y apellido
#     3.-salir
#             ''')
    
#     op=int(input())
#     match op:
#         case 1:
#             nombres=input("ingrese su name")
#             name.append(nombres)
#             apellido=input("ingrese su apellido")
#             ape.append(apellido)

#         case 2 :
#             c=0
#             for i in name:
#                 print(name[c], ape[c])
#                 c+=1
#         case 3: 
#             print("saliendo")
#             break
#         case _:
#             print("invalido")
        

#///////////////////////////////////////////////////////
# n=["eli","ale", "ana"]
# a=["lagos", "pino","teran"]

# c=0  #contador
# for i in a:
#   print(n[c], a[c])

# name=[] 
# ape=[]
# while True:
#     print('''

#     1.-Ingresar nombre
#     2.-Mostrar nombre y apellido
#     3.-Buscar name
#     4.-salir
#             ''')
    
#     op=int(input())
#     match op:
#         case 1:
#             nombres=input("ingrese su name")
#             name.append(nombres)
#             apellido=input("ingrese su apellido")
#             ape.append(apellido)

#         case 2 :
#             c=0
#             for i in name:
#                 print(name[c], ape[c])
#                 c+=1
#         case 3: 
#             busca=int(input("ingrese el name que buscara"))
#             if busca in nombres:
#                 print(f"el nombre {busca} esta en la lista ")
#                 print(f"el nombre {busca}no esta en la lista")
#         case 4:
#             print("saliendo")
#             break
#         case _:
#             print("invalido")
#///////////////////////////////////////////////////////////////////
#selecciona una opcin
#agregar productos (nombre producto y precio)
#comprar (submenu mostrando productos y precios)
#crear boleta
#salir

# productos=["Disco SSD 1TB", "Memoria Ram 8GB", "Mouse"]
# precios=[70000, 30000, 15000]
# carrito=[]

# while True:
#     print('''
#         1.- Ingresar productos a la tienda
#         2.- Comprar
#         3.- Crear Boleta
#         4.- Salir
#           ''')
#     op=int(input("Ingese una opcion: "))
#     match op:
#         case 1:
#             pro=input("Ingrese el nombre del Producto: ")
#             productos.append(pro)
#             pre=int(input("Ingrese el Precio: "))
#             precios.append(pre)
#         case 2:
#                 for i in range(len(productos)):
#                     print(i+1, ".-", productos[i], "$", precios[i] )
#                 pro=int(input("Selecione que quiere comprar: "))
#                 carrito.append(pro-1)
#                 print(carrito)
#         case 3:
#             total=0
#             print("---------------0----------------")
#             print("Bienvenido a PC House ")
#             for i in carrito:
#                   print( productos[i], "----- $", precios[i] )
#                   total=total+precios[i]
#             print("Es total de articulos es", len(carrito))
#             print("Su total neto es ", total)
#             print("Su total mas iva es ", total*1.19)
#             print("---------------0----------------")

#         case 4:
#             print("Saliendo")
#             break
#         case _:
#             print("opcion invalida")
    

#///////////////////////////////////////////////////////

# Tarea
# Crear programa de manejo de notas
# 1.- Ingresar nota
# 2.- Borrar nota
# 3.- Mostar notas
# 4.- Sacar promedio, nota mayor y nota menor
# 5.- Limpiar todas las notas
# 6.- Salir
# '''
# notas=[7.0,4.6,4.9, 7.0,5.6]

# while True:
#     while True:
#         try:
#             print('''   

#                 1.- ingresar notas
#                 2.- borrar nota
#                 3.- ver notas colocadas
#                 4.- promedio de notas, nota mayor y nota menor
#                 5.- borrar toda las notas
#                 6.- salir
#                     ''')
#             op=int(input())
#             break
#         except Exception:
#             print("Debe ingreser un numero entero valido")
    

#     match op:
#         case 1:
#             nota=float(input("ingrese la nota del alumno: "))
#             notas.append(nota)
#         case 2:
#             for num, n in enumerate(notas):
#                 print(num+1,".- ",n)
#             elim=int(input("ingrese cual quiere eliminar: "))
#             notas.pop(elim-1)
#         case 3:
#             print(notas)
#         case 4:
#             if len(notas) == 0:
#                 print("No hay notas para calcular el promedio.")
#             else:
#                 promedio=sum(notas)/len(notas)
#                 print(f"El promedio de las notas es: {round(promedio, 1)}")
#                 print("la nota mayor es", max(notas))
#                 print("la nota menor es", min(notas))
#         case 5:
#             notas.clear()
#         case 6:
#             print("saliendo...")
#             break
#         case _:
#             print("ya wey escoge algo valido")

