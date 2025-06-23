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
#             busca=input("ingrese el name que buscara")
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
#salir        #-3--------------- -2- -------------- -3
              #0----------------1------------------2
# productos=["pay limon", "kuchen franbuesa", "Mouse maracuya"]
# precios=[70000,30000,15000]
# carrito=[]
# while True:
#     print('''Bienvenido al carrito de compras,que desea hacer? :
          
#        1.-Ingresar productos a la tienda
#        2.-comprar
#        3.- Crear boleta
#        4.- Salir
#          ''')
#     op=int(input("ingrese una opcion: "))
#     match op:
#         case 1:
#             pro=input("ingrese el nombre del producto: ")
#             productos.append(pro)
#             pre=int(input("ingrese el precio: "))
#             precios.append(pre)
#         case 2:
#             for i in range(len(productos)):#se usa len para saber los productos disponibles en la lista
#                 print(i+1, productos[i], "$" , precios[i])#muestra el producto actual y muestra el precio que le corresponde, en la misma posición.
#             pro=int(input("Seleccione que producto desea comprar"))
#             carrito.append(pro -1)#Esta línea agrega el producto al carrito, pero en forma de índice. se pone-1 para que el usuario maeque 1:kuchen y no que salga 0
#             print(carrito)
#         case 3:#creacion de la boleta
#             total = 0
#             for i in carrito:
#                 print(productos[i], precios[i])
#                 total=total+precios[i]
#                 print("el total de articulos es ", len(carrito))#dice cuantos productos se compraron
#                 print("su total neto es ", total)
#                 print("su total mas iva es", total*1.19)
            
#         case 4:
#             print("saliendo")
#             break
#         case _:
#             print("opcion invalida")


#     

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
notas=[7.0,4.6,4.9, 7.0,5.6]

while True:
    while True:
        try:
            print('''   

                1.- ingresar notas
                2.- borrar nota
                3.- ver notas colocadas                 
                4.- promedio de notas, nota mayor y nota menor
                5.- borrar toda las notas
                6.- salir
                     ''')
            op=int(input())
            break
        except Exception:
            print("Debe ingreser un numero entero valido")
    
    match op:
        case 1: 
            nota=int(input("ingrese la nota del alumno"))
            notas.append(nota)
        case 2: #i :para recorrer  la lista 
            for num ,n in enumerate(notas):#da dos cosas en cada vuelta del bucle num:el indice(0,1,2) y notas n :7.0, 4,5
                print(num+1, n)#le sumás 1 para que el usuario vea:1 .- 7.0-2 .- 4.5-3 .- 6.8
            elim=int(input("seleccione cual desea eliminar"))
            notas.pop(elim-1)#se pone -1 ya que es necesario restar para obtener indice real 
#      #elimina 5.8 (porque está en la posición 1)   si elige:2  indice real: 2 - 1 = 1
        case 3:
               print(notas)
        case 4:
            if len(notas) == 0:#devuelve las notas que hay en la lista
               print("No hay notas para calcular el promedio.")
            else:#sum:suma los valores y len cuenta cuantas notas hay 
               promedio=sum(notas)/ len(notas)
               print("el total de notas es" , promedio)
               print("la nota mayor es: ", max(notas))
               print("la nota menor es: ", min(notas))

        case 5:
            notas.clear()
        case 6:
            print("saliendo...")
            break
        case _:
            print(" escoge una opcion valida")