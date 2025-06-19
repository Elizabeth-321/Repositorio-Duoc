# def suma():             #funcion
#     n1=int(input("ingrese un numero"))
#     n2=int(input("ingrese un numero"))
#     print("la suma es", n1, n2)

# def resta():             #funcion
#     n1=int(input("ingrese un numero"))
#     n2=int(input("ingrese un numero"))
#     print("la resta es", n1, n2)
# def multiplicacion():             #funcion
#     n1=int(input("ingrese un numero"))
#     n2=int(input("ingrese un numero"))
#     print("la multiplicacion es", n1, n2)
# def division():             #funcion
#     n1=int(input("ingrese un numero"))
#     n2=int(input("ingrese un numero"))
#     print("la division es", n1, n2)


#     try:
#         resultado=n1/n2
#         print("la division es", resultado)
#     except ZeroDivisionError:
#         print("la division por cero no esta permitida")

# def calcu():  
#     while True:
#       op=int(input('''seleccione una opcion
#                  1.- suma
#                  2.- Resta
#                  3.- multiplicacion
#                  4.- division
#                  5.- salir 
#                      '''))
# match op: #estructura de control que permite comparar un valor con múltiples patrones y ejecutar un bloque de código específico basado en la coincidencia
#         case 1:
#           print("Suma")
#           suma()
     
#         case 2:
#           print("Resta")
#           resta()
#         case 3:
#           print("Multiplicacion")
#           multiplicacion()
#         case 4:
#           print("Division")
#           division()
#           break
    


    #realizar programa que incluya match y llame a otras 3 funciones estas funciones deben incluir
    #if ,if else for y/0 while el programa debe ser recursivo
 #//////////////////////////////////////////////
# def promedio(x,y,z):
#     return (x+y+z)/3
# print(promedio(40, 17,22))
# if promedio(40, 17,22) >=40:
#     print("El alumno aprobó")
# else:
#     print("El alumno reprobó")


# 
# '''Crear un programa para calcular un porcetaje descuento
# Pedir al usuario  el precio , y el descuento 
# a aplicar. Mostar los resultados

# Hacer otro para calcular el IVA

# '''
#               1000   20%
# def calc_desc(precio, desc):
#     return precio*(desc/100)

# p=int(input("Ingrese el precio: "))
# d=int(input("Ingrese el descuento: "))
# midesc=calc_desc(p,d)
# print( "El descuento es de ", midesc)
# print("El precio a pagar es ", p-midesc )



# productos=["Zapato"]
# precio=[20000]

# list_prod=[
#     {"nombre":"zapato", 
#      "precio":20000, 
#      "categoria": "vestuario",
#      "tamaño": "mediano",
#      "enOferta": False},

#     {"nombre":"pelota", 
#      "precio":24000}
# ]

# # print(list_prod[0]["nombre"])

# # print(list_prod)

# # # list_prod.insert(0,{"nombre":"paleta", "precio":14000})

# # print(list_prod)




# while True:
#     try:
#         print('''
#             1.- Agregar producto
#             2.- Mostrar Productos
#             3.- Actualizar producto
#             4.- Borrar Producto
#             5.- Salir
#             ''')
#         op=int(input("Seleccione una opcion: "))
#         match op:
#             case 1:
#                 nom=input("Ingrese el nombre del producto: ")
#                 pre=int(input("Ingrese el precio: "))
#                 list_prod.insert(0,{"nombre":nom, "precio":pre})
#             case 2:
#                 for p in list_prod:
#                     print(p)        
#             case 3:
#                 # for n, p in enumerate(list_prod):
#                 #     print(n+1, ".- ", p)
#                 for i in range(len(list_prod)):
#                     print(i+1, ".-", list_prod[i])
#                 opc=int(input("Seleccione el producto a actualizar"))
#                 print(list_prod[opc-1])
#                 nn=input("Ingrese nuevo Nombre")
#                 np=int(input("Ingrese nuevo Precio"))
#                 list_prod[opc-1]["nombre"]=nn
#                 list_prod[opc-1]["precio"]=np
#                 print("Articulo actualizado!")
#             case 5:
#                 break
#             case _:
#                 print("Opcion invalida")
#     except Exception:
#         print("Solo numeros enteros")

# #///////////////////////////////////////////////////////////


# '''Crear un programa para calcular un porcetaje descuento
# Pedir al usuario  el precio , y el descuento 
# a aplicar. Mostar los resultados

# Hacer otro para calcular el IVA

# '''



# # print(prod_sport[0]["nombre"])

# # print(prod_sport)

# # # prod_sport.insert(0,{"nombre":"paleta", "precio":14000})

# # print(prod_sport)

# prod_college=[
#     {"nombre":"lapiz", 
#      "precio":400},

#     {"nombre":"goma", 
#      "precio":300} ,
     
#     {"nombre":"estuche", 
#      "precio":2000} 
# ]
# prod_sport=[
#     {"nombre":"zapato", 
#      "precio":20000},

#     {"nombre":"pelota", 
#      "precio":24000} ,
     
#     {"nombre":"raqueta", 
#      "precio":74000} 
# ]
# prod_sport[0]["nombre"]

# def mostrar_art(lista):
#     for n, p in enumerate(lista):
#         print(n+1, ".- ", p["nombre"], "$", p["precio"] )
# def insertar(lista):
#     nom=input("Ingrese el nombre del producto: ")
#     pre=int(input("Ingrese el precio: "))
#     lista.insert(0,{"nombre":nom, "precio":pre})
# def actualizar(lista):
#     mostrar_art(lista) 
#     opc=int(input("Seleccione el producto a actualizar"))
#     print(lista[opc-1])
#     nn=input("Ingrese nuevo Nombre")
#     np=int(input("Ingrese nuevo Precio"))
#     lista[opc-1]["nombre"]=nn
#     lista[opc-1]["precio"]=np
#     print("Articulo actualizado!")
# def borrar(lista):
#     mostrar_art(lista) 
#     opc=int(input("Seleccione el producto a borrar"))
#     lista.pop(opc-1)

# def menu(lista):
#     while True:
#         try:
#             print('''
#                 1.- Agregar producto
#                 2.- Mostrar Productos
#                 3.- Actualizar producto
#                 4.- Borrar Producto
#                 5.- Salir
#                 ''')
#             op=int(input("Seleccione una opcion: "))
#             match op:
#                 case 1:
#                     insertar(lista)
#                 case 2:
#                     mostrar_art(lista)      
#                 case 3:
#                     actualizar(lista)
#                 case 4:
#                     borrar(lista)
#                 case 5:
#                     break
#                 case _:
#                     print("Opcion invalida")
#         except Exception:
#             print("Solo numeros enteros")

# # menu(prod_college)

# #////////////////////////// materia 18/06/25
# '''
# crear programa CRUD del siguiente 
# diccionario
# '''

# personas={
#     1:{"nombre": " eli lagos",
#        "numeros":[7565434,97834231],
#        "estadoCivil": "Casado",
#        "trabajando": True,
#        "edad": 27},
#     2:{"nombre": " ana pino",
#        "numeros":[7565434,97834231],
#        "estadoCivil": "Casado",
#        "trabajando": True,
#        "edad": 57},
#     3:{"nombre": " alejandra lagos",
#        "numeros":[7565434,97834231],
#        "estadoCivil": "Casado",
#        "trabajando": True,
#        "edad": 27}
# }


# while True:
#     try:
#         print('''
#         1.- Ingresar Persona
#         2.- Mostrar listado
#         3.- Actualizar persona
#         4.- Borrar persona
#         5.- Salir
#         ''')
#         op=int(input("Seleccione una opcion"))
#         match op:
#             case 1:
#                 nombre=input("Ingrese el nombre: ")
#                 numero=int(input("Ingrese el numero: "))
#                 est=int(input("estado Civil 1.- Casado, 2.- Soltero: "))
#                 if est==1:
#                     estCivil="Casado"
#                 else:
#                     estCivil="Solterin"
#                 edad=int(input("Ingrese la edad: "))
#                 nextkey=len(personas)
#                 personas[nextkey+1]={"nombre": nombre,
#                 "numeros":[numero],
#                 "estadoCivil": estCivil,
#                 "trabajando": True,
#                 "edad": edad}
#                 print("Persona ingresada con exito")
#             case 2:
#                 for persona, val in personas.items():
#                     print(persona, val)
#             case 4:
#                 for persona, val in personas.items():
#                     print(persona, val)
#                 dell=int(input("Seleccione cual desea borrar"))
#                 del personas[dell]
#             case 5:
#                 break
#             case _:
#                 print("Opcion invalida")
#     except Exception as e:
#         print("EL error es: ", e)