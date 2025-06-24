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
# def promedio(x,y,z):               #funcion
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



#

# # print(list_prod[0]["nombre"])

# # print(list_prod)

# # # list_prod.insert(0,{"nombre":"paleta", "precio":14000})

# # print(list_prod)

#and: es una palabra clave en Python que verifica si un valor está presente en una lista, string o colección.
#////////////////////////////////////////////////////77
#append: agregar un element al final de la lista
# mi_lista = [1, 2, 4, 5]
# mi_lista.append(6)
# print("Después de append:", mi_lista)
# # Resultado: [1, 2, 4, 5, 6]
# list_prod.append({"nombre": nom, "precio": pre})
# #&////////////////////////////////////////////
# #insert:Inserta un elemento en una posición específica de la lista,Usa insert  si se quiere que lo reciente aparezca primero
# mi_lista.insert(2, 3)  # Insertar el número 3 en la posición 2
# print("Después de insert:", mi_lista)
# # Resultado: [1, 2, 3, 4, 5, 6]

# ist_prod.insert(0,{"nombre":nom, "precio":pre})
#/////////////////////////////////////////
# pop elimina el ultimo elemento de la lista  o se puedo poner la posicion del indice
# frutas = ["manzana", "banana", "cereza"]
# fruta_eliminada = frutas.pop(1)  # Elimina "banana"
# print(fruta_eliminada)  # Salida: banana
# print(frutas)  # Salida: ['manzana', 'cereza']
#////////////////////////////////////////////
# max: Busca el elemento con el mayor valor dentro de una lista, u otro conjunto de datos.

# notas = [5.5, 6.8, 4.2]
# mayor = max(notas)
# print(mayor)  # Resultado: 6.8
#/////////////////////////////////////////////////////
# min: funcion para buscar el numero mas bajo  dentro de una coleccion
# notas = [5.5, 6.8, 4.2]
# menor = min(notas)
# print(menor)  # Resultado: 4.2
#//////////////////////////////////////////7
#islower: verifica que todos los caraterres en ua cadena estan minusculas
#isupper verifica si todo caracteres de una cadena estan en mayuscula 

#/////////////////////////////////////////////
#sum : suma automáticamente todos los elementos numéricos de una colección como una lista o tupla.
# notas = [5.5, 6.0, 4.8]
# resultado = sum(notas)
# print(resultado)
#//////////////////////////////////////////////////
#items:se usa con diccionarios para obtener claves y valores

# producto = {
#     "nombre": "zapato",
#     "precio": 20000,
#     "enOferta": False
# }

# for clave, valor in producto.items():
#     print(clave, ":", valor)

#/////////////////////////////////////////////////////
#enumerate:Con enumerate(cuando sí querés la posición)
#for i, nombre in enumerate(nombres):
   # print(f"{i}: {nombre}")
#Acá i es el índice (posición), y nombre el contenido. ¡Esto te evita tener que poner i = 0 y usar i += 1
#////////////////////////////////////////////////777
#del:elimina clave -valor
# Eliminar un elemento de una lista
# my_list = [1, 2, 3]
# del my_list[1]  # Elimina el elemento en el índice 1 (2)
# print(my_list)  # [1, 3]

# # del: Eliminar una clave de un diccionario
# my_dict = {'a': 1, 'b': 2}
# del my_dict['b']  # Elimina la clave 'b'
# print(my_dict)  # {'a': 1}
# len: cuantos elementos existen en una lista o dicc
#///////////////////////////
# clear: borra todo

# my_list = [1, 2, 3]
# my_list.clear()
# print(my_list)  # []

# # Vaciar un diccionario
# my_dict = {'a': 1, 'b': 2}
# my_dict.clear()
# print(my_dict)  # {}
#/////////////////////////////////////////////////
# productos=["Zapato"]
# precio=[20000]

# list_prod=[
#       {"nombre": "zapato",
#        "precio": 20000,
#        "categoria":"vestuario",
#        "tamaño": "mediano",
#        "enOferta": False}, #False indica que el producto no esta en oferta

#        {"nombre": "pelota",
#         "precio": 24000}
# ]



# def funcion_agregar(list_prod):
#     nom=input("nombre del producto: ")
#     pre=int(input("escribe el precio del producto"))
#     list_prod.insert(0,{"nombre": nom,"precio": pre})
#     print("producto agregado")
# def funcion_mostrar(list_prod):
#    for p in list_prod:#para cada producto que este dentro de la lista list_prod 
#        print(p)

# def funcion_actualizar(list_prod):
#     for n, p in enumerate (list_prod):
#        print(n+1,p)# se suma uno para que empieza a contar en 1 y se pone la p porque contiene los productos de la lista
#     opc=int(input("selecione el producto a actualizar"))
#     print(list_prod[opc-1])

#     nuevopro=input("ingrese el nuevo producto")
#     nuevopre=int(input("ingrese el precio"))

#     list_prod[opc-1]["nombre"]=nuevopro #actualiza el camp onombre del producto 
#     list_prod[opc-1]["precio"]=nuevopre#actualiza datos
#     print("articulo actualizado")
# while True:
#    #  try:
#         print('''
#             1.- Agregar producto y precio
#             2.- Mostrar producto
#             3.- Actualizar producto
#             4.- Borrar producto
#             5.- Salir
#             ''')
#         op=int(input("seleccione una opcion"))
#         match op:
#             case 1:
#                funcion_agregar(list_prod)
#             case 2: 
#                funcion_mostrar(list_prod)
#             case 3:#i / i es el inidice 0-1-2 y p el producto en esa posicion
#                funcion_actualizar(list_prod)
# #             case 5:
#                 break
#             case _:
#                 print("Opcion invalida")
#     except Exception:
#         print("Solo numeros enteros")

# #///////////////////////////////////////////////////////////


# # print(prod_sport[0]["nombre"])

# # print(prod_sport)

# # # prod_sport.insert(0,{"nombre":"paleta", "precio":14000})

# # print(prod_sport)
#/////////////////////////////////////7
# validaciones para agregar un producto  
# que se un numero entero:
# if not precio.isdigit():#validacion para que sea solo numero entero
   #    print("solo numeros enteros")  # sirve solo si no tuviera un input 
   #    return 
   # precio=int(precio)
#validacion para que no ingrese un numero negativo
   # if precio<0:           
   #     print("no puede ingresar un numero negativo") 
   #     return

#///////////////////////////////////////////////////////
# Gestion de productos
list_prod=[
         {"nombre": "Silla",
           "precio": 2500},

         {"nombre": "mesa",
           "precio": 5000}
         
]
def funcion_agregar_productos(list_prod):
#validaciones 
 
   nombre=input("ingrese el producto que desea agregar")
   if not nombre:
      print("el nombre no puede estar vacio")
      return
   
     
   precio=int(input("ingrese el precio  del producto"))
   if precio == 0:
    print(" El precio no puede ser cero.")
    return
   # if not precio.isdigit():#validacion para que sea solo numero entero
   #    print("solo numeros enteros")  # sirve solo si no tuviera un input 
   #    return 
   # precio=int(precio)
   # if precio<0:            #no se usario negativo en cuando a un precio 
   #     print("no puede ingresar un numero negativo") 
   #     return
   list_prod.insert(0,{"nombre": nombre, "precio": precio})
   print("producto agregado correctamente,lista actual", list_prod)


def funcion_mostrar_productos(list_prod):
     
     if not list_prod:
         print("la lista esta vacia")
   #   if len(list_prod)==0:
   #      print("vacia") #otra manera de hacerlo1
     for p in list_prod:
       print(p)
def funcion_actualizar_productos(list_prod):
   if not list_prod:
      print("no hay productos para actualizar")
      return
   
   for c,p in enumerate(list_prod):
      print(c+1,p)
   act=int(input("ingrese el producto que desea actualizar: "))
   
   
   print(list_prod[act-1])#se ajusta la eleccion del usuario para coincida con el indice 
 
   
   nuevoname=input("como desea llamar al nuevo producto: ")
   if not  nuevoname:
      print("Debe ingresar un nombre ")
   nuevoprecio=int(input("ingresa su precio : "))
   if nuevoprecio<=0:
      print("De ingresar un precio mayor a 0")
      print(f" Se actualizo {c+1} producto ")

      list_prod[act -1]["precio"]=nuevoprecio
      list_prod[act -1]["nombre"]=nuevoname


   #validacion 
def funcion_borrar_productos(list_prod): 
   if not list_prod:
     print("no hay productos para eliminar")
     return 
  
   for cada, producto in enumerate(list_prod):
      print(f"{cada + 1}. {producto['nombre']} - ${producto['precio']}")

   elim=int(input("ingrese el producto que desea eliminar"))

   list_prod.pop(elim -1)
   print("se a eliminado este producto", list_prod)



while True: 
   
   try:
         print('''
               
      1.-Agregar producto
      2.-Mostrar productos
      3.-actualizar
      4.-borrar
      5.-salir
    
               ''')
         op=int(input("seleccione una opcion"))

         match op:
               
            case 1:
               funcion_agregar_productos(list_prod)
            case 2:
               funcion_mostrar_productos(list_prod)
            case 3:
               funcion_actualizar_productos(list_prod)
            case 4:
               funcion_borrar_productos(list_prod)
                                       

            case 5:
               print("Saliendo")
               break
            case _:
               print("opcion invalida") 
   except Exception as e :
         print("el error es:" ,e)






#//////////////////////////////////////////////////////7
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

#//////////////////////////////////////// repaso
#verificacion si el caracter @ existe en mi variable

# email=input("ingrese su email")
# if "@"in email:
#    print("la variable tiene formato email")
# else:
#    print("la variable no tiene formato email")
# while True:
#     try:
#       pin=int(input("ingrese su pin"))
#       break
#     except Exception:
#       print("solo numeros ")
     # maipular lista donde  se cree un dato,actualizar,boraar

 #validar que la clave tenga solo numeros enteros
#la funcion len verifica el largo de un objeto
# while True:
#     try:
#       pin=int(input("ingrese su clave"))
#       break
#     except Exception:
#       print("solo numeros ")

#///////////////////////////////////7
#validar una clave por su largo por lo menos 5 caracteres
# clave=(input("ingrese su clave"))

# if len(clave)>=5 and len(clave)<=12:
#    print("la clave tiene el largo correcto")
# else:
#    print("la clave ebe tener al menos 5 caracteres y menos de 12")

#///////////////////////////////////////////////////////////77
#verifico si tengo mayusculos o minusculas
#isupper()
#islower()

# tienemayus=False
# tieneminus=False
#haemos un recorrido de cada letra en mi clave 
# for letra in clave:
#     if letra.isupper():
#         tienemayus=True
#     #verifico si la letra es mayuscula o minuscula
#     if letra.islower():
#         tieneminus=True

# if tienemayus:
#     print("tiene por lo menos una mayuscula")
# else:
#     print("no tiene por lo menos uns mayuscula")
# if tieneminus:
#     print("tiene por lo menwos  una minuscula")
# else:
#     print("no tiene por unaminuscula ")

#/////////////////////////////////////////////////7

#Perros de caza

# perros={
#     1:{"nombre": "osito",
#        "raza": "poodle",
#        "codigo" : "Dphsg"},

#     2:{"nombre": "Spike"},
#       "raza" : "bulterrier",
#       "codigo": "dergE"
# }


# while True:
#     try:
#         print  ('''
#             1.-Registrar perros
#             2. Mostrar perros
#             3.-actualizar
#             4.- borrar
#             5-salir
                
                
#         ''')
#         op=int(input("seleccione una opcion"))
                
#         match op:
#             case 1:
#                 nombre=input("ingrese el nombre del perro")
#                 raza=input("ingrese raza")
#                 codigo=input("ingrese el codigo")
#                 if valida_pass(codigo):
#                   largo=list(perros.keys())[-1]
#                 #pasa a una lista .losnperos.keys (has una lista que existe en mi dic perros
#                 #)
#                   perros[largo+1]={"nombre": nombre,
#                                  "raza": raza,
#                                  "codigo": codigo}
#                 else:
#                     print("el parametro de la clave de incorrecto")
#             case 2: 
#                 mostrar_perros(perros)
#             case 3:
#                 mostrar_perros(perros)
#                 actua=int(input("sellecione el perro aactualizar"))
#                 print ('''
#                     1.-nombrre
#                     2.-Dato
#                     3.-codigo
#                        ''')
#                 dato=input("que dato actualizara?")
#                 match dato:
#                     case 1:
#                         nuevo=input("ingrese un nombre nuevo ")
#                         perros[actua]["nombre"]=nuevo
#                     case 2:
#                         nuevo=input("ingrese raza nueva")
#                         perros=

#                 perros[actua]#accedo

#             case 4:
#                 mostrar_perros(perros)
#                 borrar=int(input("seleccione el perro a borrar"))
#                 del perros[borrar]
#             case 5:
#                 break
#             case _:
#                 print("opcion invalida")

#     except Exception as e:
#         print("el error es", e)
        
# '''
# el codigo debe tener ,una mayuscula,una minuscula .un numero y un largo exacto de 6'''



#crear gestion de vehiculos
#crear programa para un parking de autos
#se debe ingresar marca,año,patente,tipo

# Marca:Tipo string,se debe tipear la Marca
# Año:Tipo int,solo de 4 difitos enteros
# patente:debe tener 4 letras minusculas y 2 digitos totaal de un largo de 6
# tipo:S= sedan, c=camioneta, m=Moto 
# se debe validar cada aspecto y tener un mantenedor para todos los vehiculos moyorizados
# 1.- ingresar vehiculo
# 2.- mostrar vehiculo
# 3.- Actualizar vehiculo
# 4.- borrar
#5.- mostrar estadisticas: ulyimo vehiculo ingresado y total en garage
# 6.- Salir

# usar funciones con argumento para validar y para poder llamar 
# las acciones dentro del menu