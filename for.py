______________________________________________________________________
# 1- Pide un numero al usuario y muestra la cantidad de repeticiones

# num=int(input("ingrese  un numero"))
# for i in range(num):
#     print("Repetir",i+1)

#________________________________________________________________________
# 2-Pide un numero al usuario y muestra la tabla de ese numero hasta el 10

# num=int(input("ingrese  un numero"))
# for i in range(5):
#      print(num*(i+1))

#________________________________________________________________________
#3- For dentro de otro for

# for x in range(10):
#      for i in range (11):
#           print(x+1, "x", i+1, "=", (i+1)*(x+1))

#________________________________________________________________________
#4-Pedir al usuario la cantidad de notas ysacar promedio
 
# cant=int(input("ingrese la cantidad de notas "))
# suma=0
# for i in range(cant):
#     print("ingrese nota", i+1)
#     nota=float(input())
#     suma=suma+nota  #suma+=nota (es otra manera de hacerlo)
#     prom=suma/cant
#     print("el promedio es",prom)

#________________________________________________________________________
# 5-Pedir la cantidad de alumnos y luego la cantidad de notas x alumno
 
# cant=int(input("ingrese el numero de alumnos"))
# for x in range (cant):
#     print("ingresa el numero de notas del aumno", x+1)
#     suma=0
#     for i in range(cant):
#      print("ingrese nota", i+1,"del alumno",x+1,"usa decimales")
#      nota=float(input())
#      suma=suma+nota  #suma+=nota (es otra manera de hacerlo)
#      prom=suma/cant
#      print("el promedio es",prom)
#      if prom>=4:
#         print("Aprovaste")
#      else:
#         print("Reprobaste")

#________________________________________________________________________
# 6-Pedir al usuario un numero y suma todos los digitos,desde el 1 hasta ese numero ,mostrando la suma 

# cant=int(input("ingrese cantidad de numero"))

# for i in range(cant):
#     num=int(input("ingrese un numero"))

#     if num % 2==0:
#         print("el nunmero",num," es par")
#     else:
#         print("el numero",num, "es impar")

#___________________________________________________________________________
#7- Designar 2 cantidatos y de votantes  ,pedir voto a cada votante y mostar resultados y verificar quien gano

# c1="Inuy"                # se designa la cantidad de votantes en este caso 2 
# c2="kago"
# cv1=0
# cv2=0

# cant=int(input("Ingrese cantidad de votantes"))

# for i in range(cant):
#     print(f"por quien votara? 1-.{c1},2-.{c2}")
#     voto=int(input())
#     if voto==1:
#        cv1=cv1+1
#     else:
#         cv2=cv2+1

#     print(f"la cantidad e votos de {c1}es {cv1}")
#     print(f"la cantidad e votos de {c2}es {cv2}")

#     if cv1>cv2:
#         print(f"gano {c1}")
#     elif cv1<cv2:
#         print(f"gano {c2}")
#     else:
#         print("Es un empate")
#__________________________________________________________________________
#8-  Vocales

# frase=input("ingrese una frase")
# c=0
# cons=0
# v=0
# for i in frase:
#     if i.lower() in "a e i o u":   # Lower es una funcion convierte los carcteres de una cadena a minunusculasa
    
#         v=v=1 
#     else:
#      cons=cons+1
#      c=c=1
# print("la cantidad de vocales ", v)
# print("la cantidad de caracteres  es ", c)

#______________________________________________________________________________
# Otra manera de hacer el par e impar   

# num=int(input("Ingrese cantidaad de numeros "))

# for i in range(1,num+1)
#     if (i) %2==0:
#       print(f"el numero {i}es par")
#     else:
#       print(f" el numero{i} es impar")
#_______________________________________________________________________________
#Supermercado
# cant=int(input("Cuantos productos llevara?"))
# total=0
# for i in range(cant):
#     print('''
#           que producto llevara?
#           1- frac $600
#           2- Bon o bon $400
#           3-Ramitas $1000
#           ''')
#     op=int(input())
#     if op==1:
#         print("llevas frac")
#         total=total+600

#     elif op==2:
#         print("llevas Bon o bon")
#         total=total+400
#     elif op==3:
#          print("llevas ramitas")
#          total=total+1000

#     else:
#         print("escoga una opcion valida")     
#______________________________________________________________________________________
#otros ejercicios de for
#perros de caza
#pida al usuario la cantidad de perros
#muestre cual es la cuota minima de conejos
#luego consulte cuantos conejos trajo
#si el perro trajo la cantidad minima
#cumplio la cuota,sino se queda sin filete
#mostrar resumen de perro que cumplieron y los que no 

# import random


        
# cuotC=3
# cumple =0
# while True:
#     try:

#         cant=int(input("ingrese la cantidad de perritos"))
#         for i in range (cant):
#           cone=random.randint (0,4)
#           print(f"el perrito {i+1} trajo {cone} conejito")

#           if cone>=cuotC:
#              print("tienes filete perrito, buen chico c:")
#              cumple+=1
#           else:
#              print("Se queda sin filete, perdon perrito :c")

# #resumen de perro que cumplieron y los que no ///////////////////////

# #los que cumplieron 
#         print("los perritos que cumplieron la cuota son ", cumple)
# #los que no cumplieron
#         print(f"los perritos que no cumplieron la cuota :c  son {cant-cumple}")
#         break 

#     except:
#        print("ingrese solo nuneros enteros")



# try:
#     #codigo a aejecutar
#     print("Ejecuta algo")
# except Exception:
#     # mensaje de error
#     print("Error")



#___________________________________________________________
# PASAR EL RAMO                             #prueba uso de for,condicionantes,try ,except

#Pregunta la cantidad de rojos en el curso
#los talleres que hay en el semestre son 4
# por cada taller asisitido obtiene 0.3 decimas 
# Si el alumno  tiene mas de 1 punto obtiene la bendicion del profe,sino no se le puede ayudar
# ingrese la nota final y sume las decimas acumuladas
# muestre si aprueba o reprueba



# rojos=int(input("Diga la cant de rojos: "))
# talleres=4
# tDecimas=0

# for r in range(rojos):
#     for t in range(talleres):
#         asist=input(f"Asistio al taller numero {t+1}? si/no: ")
#         if asist.lower()=="si":
#             tDecimas+=0.3
#     if tDecimas>=1:
#         print(" Tiene la bendicion del profe")
#     else:
#         print("Nada mas que hacer ")
#     nf=float(input("Ingrese su nota final"))
#     nf+=tDecimas
#     print(f"su nota final es {nf}")
#     if nf>=4:
#         print("El alumno aprobó")
#     else:
#         print("El alumno reprobó")




# ______________________________________________________________________________________________
# #LAVADO DE AUTO

#Crear un menu para lavar autos


# 1.-Cursar pago del lavado
# 2.- ver ventas diarias
# 3.- Salir

#el lavado tiene 3 niveles:
#1.- Full $15.000 2.- standard 10.000. 3.- Basico $7.000
#al mostrar las ventas diarias,debe mostrar la cantidad de autos que han ingresado y el monto total
#recaudado.Tambien debe mostrar el monto mas alta pagado


# basico=0
# standard=0
# full=0
# canta=0
# top=0

# while True:
#         op=int(input('''ingrese una opcion
#          1.-Cursar pago del lavado
#          2.-ver ventas diarias
#          3.- Salir              
#                      '''))

#         match op:
#             case 1: 
#                 while True:
#                      try:
#                         op=int(input('''ingrese una opcion de lavado
#                         1.- Basico $7000
#                         2.- standard $10000
#                         3.- Full $15000
#                         4.- volver al menu prinicipal
                                                    
#                                     '''))
                    
#                         match op:
#                             case 1: 
#                                 print("has seleccionado basico")
#                                 basico+=7000
#                                 canta+=1
#                                 if 7000>top:
#                                     top=7000

#                             case 2:
#                                 print("has seleccionado standard ")
#                                 standard+=10000
#                                 canta+=1
#                                 if 10000>top:
#                                     top=10000
#                             case 3:
#                                 print("has seleccionado full")
#                                 full+=15000
#                                 canta+=1  #para saber cantidad autos
#                                 if 15000>top:
#                                      top=15000
#                             case 4:
#                                     print("volviendo al menu principal...")
#                                     break
#                             case _:
#                                     print("opcion invalida")
#                      except Exception:
#                           print("ingrese solo numeros enteros")


#             case 2: 
             
#                         op=input("sleccione una opcion")
#                          #resumen de ventas diarias
#                         print("su total por lavado basico es :", basico)
#                         print("su total por lavado standard es :", standard)
#                         print("su total por lavado full es :", full)
#                         print("la cantidad de autos atendidos es", canta)
#                         print("el total recaudado entre todos los servicios es $ :", basico + standard + full )
#                         print("el monto mas alto pagado es", top)
#             case 3:
#                   print("saliendo...")
#                   break
#             case _:
#                   print("opcion oncorrecta")

            
























 

#_____________________________________________________________________________________

# El programa debe tener un menú de opciones de donde se pueda realizar el pago
# del cupo de la tarjeta de crédito, como también simular nuevas compras, y estas
# una vez sumadas se resten al cupo disponible.
# Las opciones disponibles deben estar construidas de la siguiente forma:

# 1. Pago de Tarjeta de Crédito:
# a. El usuario comienza con una deuda de $100.000
# b. El usuario puede ingresar un monto para realizar un pago en la
# tarjeta de crédito.
# c. Se debe verificar que el monto ingresado sea mayor o igual a cero.
# d. Se debe verificar que el monto a pagar no exceda el saldo actual de
# la tarjeta.
# e. Al pagar el sistema debe descontar de la deuda total
# f. Si las verificaciones son exitosas, se realiza el pago y se actualiza el
# saldo de la tarjeta.

# 2. Simulación de Compras:
# a. El usuario puede simular realizar un número ilimitado de compras.
# b. Para cada compra, se solicita al usuario ingresar el monto de la
# compra. El programa suma los montos de cada compra.
# c. Se verifica que el monto de la compra sea mayor o igual a cero.
# d. Se realiza la compra y se actualiza el saldo de la tarjeta para cada
# iteración del bucle for.

# 3. Salir:
# a. Al seleccionar esta opción, el programa debe cerrarse o finalizar.
# A considerar:
# 1. Manejo de Errores:
# a. Se utilizan bloques try y except para manejar posibles errores al
# ingresar datos, validar valores no numéricos y errores inesperados.

# deuda=100000

# while True:
#     op=int(input('''
# seleccione una opción
#      1.- pago
#      2.- compra            
#      3.- salir            
# '''))
    
#     match op:
#         case 1:
#             print(f"la deuda actual es {deuda}")
#             while True:
#                 try:
#                     pago=int(input("ingrese el monto a pagar"))
#                     break
#                 except Exception:
#                     print("solo se a admiten numeros enteros")
#             if pago>0 and pago<=deuda:
#                 deuda=deuda-pago

#             else:
#                 print(f"el pago debe ser mayor a cero y no exceder {deuda}")        

            

#         case 2:
#             print("comprando")
#             monto=int(input("ingrese el monto de la compra: "))
#             deuda+=monto
#             print(f"la deuda actual es {deuda}")


#         case 3:
#             print ("saliendo...")
#             break


#         case _:
#             print("opcion invalida")




#_____________________________________________________________________________________

# ETAPAS:
# Debe crear un menú de inicio de sesión, en el cual se debe mostrar los siguientes campos:
# 1) iniciar sesión
# 2) registrar usuario
# 3) salir
# Para lo cual usted deberá haber creado 3 variables de usuario y 3 variables de contraseña,
# ambas con valor inicial vacío, ejemplo:
# • usuario1= None
# • usuario2=None
# • usuario3=None
# • contrasena1= None
# • contrasena2=None
# • contrasena3= None

# Si se selecciona la opción 1 y no existen registros de usuarios, el sistema deberá indicar que
# es necesario registrar un usuario antes, y volverá al menú principal, en el caso de que
# ingrese el usuario y contraseña correctamente, entonces el sistema mostrará el siguiente
# menú:
# 1) Realizar llamada
# 2) Enviar correo electrónico
# 3) Cerrar sesión
# 2
# Donde la opción 1 debe solicitar un número de celular, éste deberá comenzar con 9 y su
# tamaño es de 9 dígitos (ejemplo: 985447561).
# La opción 2, solicita un correo electrónico, el cual debe tener por lo menos un carácter de
# “@” (validar usando for y while) y lo guardará en una variable llamada “correo”.
# También solicitará el mensaje a enviar y lo guardará en una variable llamada “mensaje”
# Finalmente cerrar sesión, volverá al menú principal.
# El sistema no acepta que se ingresen opciones distintas a 1, 2 y 3 en ambos menús, si ocurre
# esto, entonces el sistema emite un error y vuelve a solicitar la opción.
# Recuerde utilizar try Exception en caso de ser necesario.

# #variables de usuarios
# usuario1= None
# usuario2=None 
# usuario3=None
# #variables de contraseñas 
# contrasena1= None
# contrasena2=None
# contrasena3= None

# while True:
   
#  op=int(input(''' ingrese una opcion :)
              
#  1. iniciar sesión
#  2.-registrar usuario
#  3.- salir
# '''))
 
#  match op:
  
#   case 1:

#     if usuario1==None and usuario2==None and usuario3==None:
#       print("No hay registros")

#     print("Es necesario registrarse antes de continuar...")
#     user=int(input("ingrese un usuario"))
#     print("Debe indicar una contraseña con un minumo de 6 digitos ")
#     cont=int(input("ingrese una contraseña"))
    #  print("su contraseña es correcta")

#_______________________________________________________________________
# # Ejemplo de carrito con categorias  
# total=0
# cantArt=0    

# while True:
#     try:
#         opcion=int(input(''' Carrito de compras
#                         Seleccione una opcion con un numero entero
#                         1.- Comprar Frutas
#                         2.- Comprar Verduras
#                         3.- Pagar
#                         4.- Salir
#                             '''))
#         match opcion:
#             case 1:
#                 while True:
#                     try:
#                         opcion=int(input('''
#                                         Seleccione una opcion con un numero entero
#                                         1.- Frutilla $1500
#                                         2.- Pera $1200
#                                         3.- Manzana $ 1300
#                                         4.- Volver al menu principal
#                                             '''))
#                         match opcion:
#                             case 1:
#                                 print("Has seleccionado Frutilla")
#                                 total+=1500
#                                 cantArt+=1 #para al finalñ de la compra se epa la cantidad de articulos 
#                             case 2:
#                                 print("Has seleccionado Pera")
#                                 total+=1200
#                                 cantArt+=1
#                             case 3:
#                                 print("Has seleccionado Manzana")
#                                 total+=1300
#                                 cantArt+=1
#                             case 4:
#                                 print("Volviendo...")
#                                 break
#                             case _:
#                                 print("Opcion invalida")
#                     except Exception:
#                         print("Solo puede ingresar numeros enteros")   
#                     print(" TU total hasta ahora es ", total)
#             case 2:
#                 while True:
#                     try:
#                         opcion=int(input('''
#                                         Seleccione una opcion con un numero entero
#                                         1.- Papa $1500
#                                         2.- Lechuga $1200
#                                         3.- Cebolla $ 1300
#                                         4.- Volver al menu principal
#                                             '''))
#                         match opcion:
#                             case 1:
#                                 print("Has seleccionado Papa")
#                                 cant=int(input("Cuantas papas llevara?"))
#                                 total+=cant*1500
#                                 cantArt+=cant
#                             case 2:
#                                 print("Has seleccionado Lechuga")
#                                 total+=1200
#                                 cantArt+=1
#                             case 3:
#                                 print("Has seleccionado Cebolla")
#                                 total+=1300
#                                 cantArt+=1
#                             case 4:
#                                 print("Volviendo...")
#                                 break
#                             case _:
#                                 print("Opcion invalida")
#                     except Exception:
#                         print("Solo puede ingresar numeros enteros")   
#                     print(" TU total hasta ahora es ", total)
#             case 3:
#                 print("Has seleccionado pagar")
#                 print(f"El total de articulos es {cantArt}")
#                 print(f"El total a pagar es {total}")
#                 print(f"El total a pagar mas IVA es {round(total*1.19)}")
#             case 4:
#                 print("Saliendo...")
#                 break
#             case _:
#                 print("Opcion invalida")
#     except Exception:
#         print("Solo puede ingresar numeros enteros")  
            
#__________________________________________________________-
# # ## Domingo de pascua ####
# Preguntar la Cantidad de niños de niños que buscan huevitos de chocolates
# Cuando se termine la busqueda , preguntar cantos huevos encontró cada uno
# y clasificarlos de la siguiente forma
# Menos de una docena : NOOB
# Entre una docena a 24: Master
# 25 huevos o mas :Legend
# Mostrar resumen, y mostrar la mayor cantidad de huevitos encontrados por un solo niño                

# import random    
# while True:
#     try:    
#         cantn=int(input(" cuantos niños buscan huevos? "))
#         #break
#     #except Exception:               puede ir aca el except al igual que break o abajo 
#        # print("solo numeros enteros")
#         noob=0
#         master=0
#         legend=0
#         top=0

#         for n in range(cantn):  #se repite la cant de veces que el usuario decida(cuantos niños buscan huevos)
#             huevos=random.randint(5,30) # incluye la cantiddad de huevos 24,25 o docena
#             if huevos>top: #se verifica cant huevo ej: 6 es mayor a 0?  
#               top=huevos

#             print(f"el niño numero {n+1} encontro {huevos} huevos" )   #mostar numero
#             if huevos<12:
#                 noob+=1# s eusa 1 para aumentar en 1 (sirve para contar articulos,cantidad )
                
#             elif huevos>= 12  and huevos <=24:
#                 master+=1
#             else:
#                 legend+=1
#             #mostrar resumen
#         print("la cantidad del grupo noob es ", noob)
#         print("la cantidad del grupo master es", master)
#         print("la cantidad de niños legend es", legend)
#         print("el mayor numero de huevos encontrados es ", top)
#         break

#     except Exception:
#         print("solo numeros enteros")

# variacion del mismo ejercicio ____________________________________2.1
# Compra de Juguetes en Pascua 🐰 🔹 
# Preguntar la cantidad de niños que comprarán juguetes de Pascua.
# Cada niño elige cuántos juguetes quiere comprar.
# Dependiendo del número de juguetes, se aplican descuentos:
# 1 a 2 juguetes → Sin descuento
# 3 a 5 juguetes → 10% de descuento
# y clasifficarlos de la siguiente manera:
# 1 o 2 juguetes: principiante
# 3 a 5 juguetes: coleccionista
# 6 o mas juguetes: fanatico
# 6 juguetes o más → 20% de descuento 
# Calcular el total a pagar considerando los descuentos y mostrar un resumen.
# También mostrar quién compró más juguetes (el mayor número registrado)

import random

principiante=0
fanatico=0
coleccionista=0
while True:
    cant=int("cuantos niños compraran juguetes?") 
    for n in range(cant):
        juguetes=random.randint(5,16)
        print(f"el niño {n+1} comprara {juguetes} juguetes")
        if juguetes

