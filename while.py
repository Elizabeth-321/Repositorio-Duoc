#Uso While
# clave=123
# intentos=0
# password=int(input("ingrese su clave"))

# while clave!=password and intentos<=3:
#     print("erroor ingrese una clave valida")
#     intentos=intentos+1
#     password=int(input("ingrese la pass"))

#______________________________________________________________
# suma = 0
# while True:                                                                      #arreglar porque no muestra el total
#     num=int(input("ingrese un numero, cero para salir:"))
#     if num==0:
#      suma +=num
#     print(suma)
#     print(f"la suma total es{suma}")

# #____________________________________________________________

# #Pida al usuario el limmite inferior y superior de un rango
# genere un numero al azar dentro de ese rango # usar random para generar un numero al azar
# el segundo numero,no debe ser menor que el primeropero debe darle
# la oportunidad al usuario de  ingresar otro

# import random

# print("ingrese 2 numeros")
# n1 =int(input("ingrese el primer numero"))

# n2 =int(input("ingrese otro numero mayor que el anterior"))

# while n2<=n1: 
#     print("El numero debe ser mayor que el anterior")
#     n2=int(input("ingrese otro numero mayor que el anterior"))
# numran=random.randint(n1,n2)

# print(numran)

#_____________________________________________________________  #!!!!!!!usar random,condicional while ////prueba

#adivina el numero entre el 1 y 50

# import random                               #verificar

# numran=random.randint(1,50)
# print("adivine el numero entre 1 y 50")
# num=int(input())
# while numran!=num: #!= distinto de/  igual a ==/ mayor a >/menor a </mayor o igual >= /menor o igual a <=/ -= quitarle 
#      if num>numran:
#           print("el numero a adivinar es menor")
#      else:
#         print("el numero a adivinar es mayor")

# print("adivinaste el numero")

#_________________________________________________________________
#adivina el numero entre el 1 y 50 y ponere cantidad de intentos

# import random                              

# numran=random.randint(1,50)
# print("adivine el numero entre 1 y 50")          #ARREFLAR!!
# num=int(input())
# while numran!=num: #!= distinto de/  igual a ==/ mayor a >/menor a </mayor o igual >= /menor o igual a <=/ -= quitarle 
#      intentos -=1
#      if intentos==0:
#           break
#     if  num>numran
#           print("el numero a adivinar es menor")
#      else:
#         print("el numero a adivinar es mayor")
#         print(f"")
#   if intentos==0 

#  else:
#       print("adivinaste el numero")


#____________________________________________________________________
#designar 2 peleadores solicitando sus nombres
# caada eleador tiene 50 hp,debe mostrar la barra de energia ,las peleas son por turnos
# cad turno el peleador ataca 3 y 15
# existe posibilidad de ataque critico del 20% sera ataque doble
# gana el que le quita todo el hp al rival


# print("ingrese lso nombres de los peleadores")
# p1=input("peleador 1")
# p2= input ("peleador 2")
# hp1= 50
# hp2 = 50
# turno=random.randint (1,2)

# while hp1>0 and hp2>0:

#     if turno % 2==0:
#         print("turno de " , p1)
#         ataq=random.randint(3,15)
#         critical=random.randint(1,5)
#         if critical==3:
#             ataq*2
#             print("ATAQYE CRITICO")
#         hp2-= ataq
#         timee.sleep(1)
#         print(f"vida de{p2}")
#         print("/"*hp2)

# else: 
#         print("turno de " , p2)
#         ataq=random.randint(3,15)
#         critical=random.randint(1,5)
#         if critical==3:
#             ataq*2
#             print("ataque critico")
#         hp2-= ataq
#         time.sleep(1)
#         print(f"vida de{p1}")
#         print("/"*hp1)
#         turno+=1

#         if hp1>hp2:
#              print(f"ha ganado el {p1}")

#         else: 
#              print(f"ha ganado el {p2}")

#________________________________________________________
# Crear un cajero automatico :
# tener en cuenta cajas de billetes de 5000,10000 y 20000
# cada caja tiene 30 billetes,verificar si el monto solicitado esta disponible en el cajero
# Verificar si el monto solicitado es posible por el multiplo de los billetes disponibles
# al termianr cada transaccion,debe mostrar saldo disponible
# debe haber 3 usuarios cada uno con su saldo correspondiente,usar clave secreta para iniciar y segun la clave
# asociar el saldo disponible 


#_________________________________________________________

# color=input("ingrese un color")
# if color.lower()!="negro":
#     print("el color no es el requerido")
# else:
#     print("este es el color requerido")

#_________________________________________________________ practica con while.if

# intentos=3
# while intentos>0:   #<=3 menor o igual a 3
#     intentos-=1
#     color=input("ingrese un color")
#     if color.lower()!="negro":
#          print("el color no es el requerido")
#     else:
#          print("este es el color requerido")
#          break

#__________________________________________________________
#La Florida 20%,/La Pintana 30%,/Puente Alto 25%,/San Joaquin 15%/ pregunta al usuario de que comuna es
# Grupo familiar: 1=>2%,2 a 4=>3%,5 o mas=>4% cuantos son en el grupo familiar
# calcular el arancel actual, es de 200.000 por semestre, y con la informacion dada calcular el descuento
# ej:
# ingrese su comuna: La Pintana
#Ingrese su grupo familiar (numero entero)
# el total del descuento es: 23%
# el total a pagar es 

# descuento=0
# arancel=200000
# print('''
#     1.- la florida 
#     2.- la pintana
#     3.- San juaquin
#     4.-Puente alto 

#     ''')
# comuna=int(input("ingrese su comuna"))

# if comuna==1:
#     descuento=20
# elif comuna==2:
#     descuento=30

# elif comuna==3:
#      descuento=25

# elif comuna==4:
#     descuento=15

# else:
#     print("respuesta invalida")

# grupof=int(input)

#_________________________________________________________________________________
#clasificar segun categoria y precio
#cat 1 +200,cat 2+400,cat 3 +600
#Precios:1000 y menos,3%,entre 1001 y 5000;5%,5001 y mas 6%
# Poner listado de 3 productos por categoria,las cat son 1.2 y 3
#agregar los impuestos al precio,segun la cat y luego aplicar descuento al total de la boleta segun el monto

# ej:
# producto1,cat 2.1500+400
# producto 2 cat 1, 8000+200
# el total es 10100*-6%
# el total a pagar es :9494

# total=0
# print('''
#     Selecione una categoria
#       1.- Zpatillas
#       2.- Poleras
#       3.- Pelotas
#       ''')
# cat=int(input())

# if cat==1:
#     print('''
#         1.- Zapatilla runing 2000
#         2.- Zapatilla Futbolito 1500
#         3.- Zapatilla Padel 20      
#           ''')
#     op=int(input())
#     if op==1:
#         total+=2000+200
#     elif op==2:
#         total+=1500+200
#     elif op==3:
#         total+=20+200
#     else:
#         print("Opcion invalida")
# elif cat==2:
#     print('''
#         1.- Polera Runing 3000
#         2.- Camiseta Futbolito 1500
#         3.- Polera Padel 60      
#           ''')
#     op=int(input())
#     if op==1:
#         total+=3000+400
#     elif op==2:
#         total+=1500+400
#     elif op==3:
#         total+=60+400
#     else:
#         print("Opcion invalida")
# elif cat==3:
#     print('''
#         1.- Pelota Voley 1000
#         2.- Pelota Futbolito 2500
#         3.- Pelota Rugby 3500     
#           ''')
#     op=int(input())
#     if op==1:
#         total+=1000+600
#     elif op==2:
#         total+=2500+600
#     elif op==3:
#         total+=3500+600
#     else:
#         print("Opcion invalida")
# else:
#     print("Opcion invalida")

# if total<=1000:
#     total= total*0.97
# elif total<=1001 and total>=5000:
#     total= total*0.95
# elif total>=5001:
#     total= total*0.94

# print(" EL total es ", total)
 #_________________________________________________________________________
#calcular el puntaje de credito
# Se debe calcular que tanto credito tiene una persona 
# en cierta entidad financiera ,debera considerar cantidad de ingresos,nivel educacional y nacionalidad
# cantidad de ingresos 
# 500.000 a 1.000.000: 300.000
# 1.000.000 a 1.500.000: 650.000
# 1.500.001 o mas: 1.000.000
# Nivel educacional :Basico:x1 ,medio x1.3,superior:x1.5
# Nacionalidad : Chilena:+300.000, extranjero:+0

# credito = 0
# print("ingrese su  rango de ingresos")
# print('''cantidad de ingresos
#       1- 500.000 a 1.000.000
#       2.-1.000.000 a 1.500.000
#       3.- 1.500.001 o mas 

#       ''')

# op_ingresos= int(input())

# if op_ingresos==1:
#     credito+= 300000
# elif op_ingresos==2:
#     credito+= 650000
# elif op_ingresos==3:
#     credito+= 1000000
# else:
#     print("ingrese una opcion")


# print('''Nivel educacional
#       1.- Basico
#       2.- Medio
#       3.- Superior

#       ''')
# print("ingrese su  nivel educativo")
# op_educ=int(input())

# if op_educ==1:
#     credito*=1
# elif op_educ==2:
#     credito*=1.3
# elif op_educ==3:
#     credito*=1.5
# else:
#     print("escoja una opcion correcta")

# print("ingrese cual es su nacionalidad")
# print('''
#     1.-Chilena
#     2.- Extranjero
#     3.- Otro
      
#       ''')

# op_nacio=int(input())
# if op_nacio == 1 :
#     credito+= 300000
# elif op_nacio==2:
#     credito+= 0

# print("su puntaje de credito final es", credito)




# pedir dia y mes de nacimiento y mostrar el signo zodiacal


#Pida al usuario 2 digitos verificando que el segundo sea mayor
#genere un numero aleatorio entre esos digitos
# e imprima la cantidad de veces el simbolo (vuadrado) (alt+220)
# import random
# print("ingresa  2digitos")
# n1=int(input("numero 1: "))
# n2=int(input("numero 2 :"))

# while n1>n2:
#     print("El numero 2 no puede ser menor que el numero1")
#     n1=int(input("numero 2:"))

# num=random.randint(n1,n2) hacer lo mismo con for!

#Crear un programa que pida la cantidad de ramos y luego
# pida el promedio por cada materia 
# basados en su promedio final,aplicar puntaje de beneficios
# 4.5 y 5: 300, 5.1 y 6.0:500,6.1 y 7.0:800
# agregar puntaje segun carrera
# Tecnico: +60, ingenieria: +40, diplomado: +20

# mat=int(input("Ingrese la cant de materias: "))
# suma=0
# for i in range(mat):
#    notaramo=float(input(f"Ingrese la nota del ramo{i+1}: "))
#    suma+=notaramo
# prom=suma/mat
# print("Su nota final es ", round(prom,1))
# if prom>=4.5 and prom<=5.0:
#    puntaje=300
#    print( f"Su puntaje de beneficios es de {puntaje}")
# elif prom>=5.2 and prom<=6.0:
#     puntaje=500
#     print( f"Su puntaje de beneficios es de {puntaje}")
# elif prom>=6.1 and prom<=7.0:
#     puntaje=800
#     print( f"Su puntaje de beneficios es de {puntaje}")
# else:
#    print(" Es tan porro que no tiene beneficios")

# car=int(input('''
#             Ingrese su tipo de grado
#               1.- Tecnico
#               2.- Ingenieria
#               3.- Diplomado
#               '''))
# if car==1:
#    puntaje+=60
# elif car==2:
#    puntaje+=40
# elif car==3:
#    puntaje+=20
# else:
#    print("no es nuemro valido")

# print( " El puntaje de beneficios es ", puntaje)