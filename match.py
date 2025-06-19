# # uso y explicacion de match
# import random

# def suma():
#     n1=int(input("Ingrese un numero"))
#     n2=int(input("Ingrese otro numero"))
#     print("El resultado de la suma es", n1+n2)
# def resta():
#     n1=int(input("Ingrese un numero"))
#     n2=int(input("Ingrese otro numero"))
#     print("El resultado de la resta es", n1-n2)
# def multi():
#     n1=int(input("Ingrese un numero"))
#     n2=int(input("Ingrese otro numero"))
#     print("El resultado de la suma es", n1*n2)
# def division():
#     n1=int(input("Ingrese un numero"))
#     n2=int(input("Ingrese otro numero"))
#     print("El resultado de la division es", n1/n2)


# def calcu():
#     while True:
#         op=int(input('''Ingrese una peracion
#                     1.-Suma
#                     2.-Resta
#                     3.-Mutltiplicacion
#                     4.-Division
#                     5.-Salir
#                     '''))
#         match op:
#             case 1:
#                 print("Suma")
#                 suma()
#             case 2:
#                 print("Resta")
#                 resta()
#             case 3:
#                 print("Mutltiplicacion")
#                 multi()
#             case 4:
#                 print("Division")
#                 division()
#             case 5:
#                 print("Saliendo...")
#                 break
#             case _:
#                 print("Opcion INVALIDA")

# # calcu()

# def azarN():
#     num=random.randint(1,10)
#     return num

# def arancel():
#     arancel=200000
#     descuento=0
#     print('''
#         1.- La Florida 20%
#         2.- La Pintana 30%
#         3.- Puente Alto 25%
#         4.- San Joaquin 15%
#         ''')
#     comuna=int(input("Seleccione una comuna: "))

#     if comuna==1:
#         descuento=20
#     elif comuna==2:
#         descuento=30
#     elif comuna==3:
#         descuento=25
#     elif comuna==4:
#         descuento=15
#     else:
#         print("Seleccion incorrecta")

#     grupo=int(input("Ingrese su grupo familiar( numero entero usted incluido ) :"))

#     if grupo==1:
#         descuento+=2
#     elif grupo<=4 and grupo>=2:
#         descuento+=3
#     elif grupo>=5:
#         descuento+=4
#     else:
#         print("Seleccion incorrecta")

#     print("El descuento total es ", descuento)
#     desc=arancel*descuento/100
#     total=arancel-desc
#     print("El total a pagar es $",total)

# arancel()



#///////////////////////////////////////////////

# # '''
# # Crear un menu de carrito con las siguientes opciones
# # 1.-Ingresar nombre del usuario
# # Sera mostrado en la boleta, con un saludo
# # 2.- Comprar, poner productos para poder comprar
# # con su precio correspondiente ej: producto $1000
# # 3.- Sacar boleta, calcular el precio neto
# # y el precio mas IVA. Mostrar totales
# # bonus, mostrar cant de articulos que lleva
# # 4.- Salir 
# # Consideraciones:
# # Por lo menos 3 productos
# # No hay limite de compra
# # Se puede salir en cualquier momento
# # Los montos de los productos son fijos
# # '''



# uso y explicacion de match
# import random

# def suma():
#     n1=int(input("Ingrese un numero: "))
#     n2=int(input("Ingrese otro numero: "))
#     print("EL resultado de la suma es", n1+n2)
# def resta():
#     n1=int(input("Ingrese un numero: "))
#     n2=int(input("Ingrese otro numero: "))
#     print("EL resultado de la resta es", n1-n2)
# def multi():
#     n1=int(input("Ingrese un numero: "))
#     n2=int(input("Ingrese otro numero: "))
#     print("EL resultado de la multiplicacion es", n1*n2)
# def division(): 
#     try:
#         n1=int(input("Ingrese un numero: "))
#         n2=int(input("Ingrese otro numero: "))
#         print("EL resultado de la resdivisionta es", n1/n2)
#     except ZeroDivisionError as nombre_de_excepcion:
#         # Código para manejar la excepción
#         print(f"Se produjo una excepción: {nombre_de_excepcion}")


# def calcu():

#     while True:
#             try:
#                 print('''
#                     1.- Suma
#                     2.- Resta
#                     3.- Multiplicacion
#                     4.- Division
#                     5.-Salir
#                     ''')
#                 op=int(input("Seleccione un a opcion"))

#                 match op:
#                     case 1:
#                         print("Suma")
#                         suma()
#                     case 2:
#                         print("Resta")
#                         resta()
#                     case 3:
#                         print("Multiplicacion")
#                         multi()
#                     case 4:
#                         print("Division")
#                         division()
#                     case 5:
#                         print("Saliendo")
#                         break
#                     case _:
#                         print("Opcion no valida")
#             except ValueError as errorr:
#                 print("Debe ingreser un numero entero")
#                 print(f"Error: {errorr}")

# calcu()5


## nuevo menu recursivo
# debe tener 3 programas creados enteriormente
# Los programas deben estar en una funcion
# el menu debe llamar a estos programas 
# y ejecutarlos de manera correcta
# debe tener la opcion de salir 
# y la opcion por defecto



def clave_inf():
    #Clave con intentos infinitos
    clave=3344
    password=int(input("Ingrese su pass :"))
    while clave!=password:
        print ("ERORR, clave invalida")
        password=int(input("Ingrese su pass :"))

    print("Bienvenido al sistema")

def azar():
    
    numeroAadivinar=random.randint(1,50)

    num=int(input("Adivine el número"))

    while num!=numeroAadivinar:
        print(numeroAadivinar)
        if num>numeroAadivinar:
            print("El numero a adivinar es menor")
        else:
            print("El numero a adivinar es mayor")
        num=int(input("Adivine el número"))
    print("Le achuntaste!") 

def ruleta():
    # # Ruleta rusa

    barril=random.randint(1,6)
    rul=int(input("Dispare : "))

    while rul!=barril:
        rul=int(input("Dispare"))
    print("BANG!!!")
    

def menu_nuevo():
    while True:
        op=int(input('''
                Seleccione una opcion
                1.-Clave con intentos infinitos
                2.- NUmero al azar
                3.-Ruleta Rusa
                4.-Salir
                '''))   
        match op:
            case 1:
                clave_inf()
            case 2:
                azar()
            case 3:
                ruleta()
            case 4:
                break
            case _:
                print("Opcion no valida")

# '''
# Crear un menu de carrito con las siguientes opciones
# 1.-Ingresar nombre del usuario
# Sera mostrado en la boleta, con un saludo
# 2.- Comprar, poner productos para poder comprar
# con su precio correspondiente
# 3.- Sacar boleta, calcular el precio neto
# y el precio mas IVA. Mostrar totales
# bonus contar la cantidad de articulos
# 4.- Salir 
# Consideraciones:
# Por lo menos 3 productos disponibles
# No hay limite de compra
# Se puede salir en cualquier momento
# Los montos de los productos son fijos
# Mostrar tb el total de articulos.
# '''






# ## nuevo menu recursivo
# # debe tener 3 programas creados enteriormente
# # Los programas deben estar en una funcion
# # el menu debe llamar a estos programas 
# # y ejecutarlos de manera correcta
# # debe tener la opcion de salir 
# # y la opcion por defecto



# def clave_inf():
#     #Clave con intentos infinitos
#     clave=3344
#     password=int(input("Ingrese su pass :"))
#     while clave!=password:
#         print ("ERORR, clave invalida")
#         password=int(input("Ingrese su pass :"))

#     print("Bienvenido al sistema")

# def azar():
    
#     numeroAadivinar=random.randint(1,50)

#     num=int(input("Adivine el número"))

#     while num!=numeroAadivinar:
#         print(numeroAadivinar)
#         if num>numeroAadivinar:
#             print("El numero a adivinar es menor")
#         else:
#             print("El numero a adivinar es mayor")
#         num=int(input("Adivine el número"))
#     print("Le achuntaste!") 

# def ruleta():
#     # # Ruleta rusa

#     barril=random.randint(1,6)
#     rul=int(input("Dispare : "))

#     while rul!=barril:
#         rul=int(input("Dispare"))
#     print("BANG!!!")
    

# def menu_nuevo():
#     while True:
#         op=int(input('''
#                 Seleccione una opcion
#                 1.-Clave con intentos infinitos
#                 2.- NUmero al azar
#                 3.-Ruleta Rusa
#                 4.-Salir
#                 '''))   
#         match op:
#             case 1:
#                 clave_inf()
#             case 2:
#                 azar()
#             case 3:
#                 ruleta()
#             case 4:
#                 break
#             case _:
#                 print("Opcion no valida")







#//////////////////////////////////////////////////////777777777


# # # ejemplo de funcion con return
# # # retorna un numero entero.

# # def suma_ret():
# #     n1=int(input("Ingrese un numero: "))
# #     n2=int(input("Ingrese otro numero: "))
# #     return n1+n2

# # nume=suma_ret()

# # for i in range(nume):
# #     print ("hola")


# ##### Promedios por cantidad de alumnos#####
# # Pedir cantidad de alumnos 
# # pedir notas por cada alumno
# # premediar a cada alumno 
# # y mostrar si aprueba o reprueba
# # Bonus, mostrar promedio de todos los alumnos
# # ingresados

# '''Ingrese cant de alumnos: 5
# Ingrese cantidad de notas del alumno 1 :3 
# Ingrese la nota 1 del alumno 1
# Ingrese la nota 2 del alumno 1
# Ingrese la nota 3 del alumno 1
# El promedio del alumno 1 es : 5.6
# El alumno 1 Aprobó
# Ingrese la nota 1 del alumno 2
# ...
# ...
# ...
# El promedio general del curso es: 
# '''

#///////////////////////////////////////////////////////////////////// ejercicio de la prueba
# entradas para un cine por medio de un menú de opciones.
# El programa debe tener un saldo inicial de entradas disponibles (por ejemplo, 50 entradas).
# Luego debe mostrar un menú de opciones que permita al usuario:
# ***** Cine Estrella *****
# Bienvenido al sistema de venta de entradas del Cine Estrella
# 1. Ver cuántas entradas quedan.
# 2. Comprar una cantidad de entradas.
# 3. Salir del sistema.
# Si el usuario desea comprar entradas, se debe validar que haya suficiente cantidad disponible.
# En caso de que no haya suficientes, debe informarse al usuario.
# El programa debe repetirse hasta que el usuario elija la opción de salir



# Sinicial= 60
# while True:
#         try: 
#           op =int(input('''Bienvenido al sistema de venta de entradas del "Cine Estrella(1-3)
#              1.- Ver entradas disponibles
#              2.-        Comprar entradas.
#              3.-        Salir del sistema.
#                      '''))
#           match op:
#                 case 1: 
#                     while True:
#                         op=int(input('''seleccione una opcion 
#                                 1.- hay 60  entradas disponibles
#                                 2.- volver al menu principal...   
#                                             '''))
#                         match op:
                                    
#                             case 1:
#                                 print("has seleccionado ver la cantidad de entradas", Sinicial)
#                     #                     
#                             case 2:
#                                 print("volviendo al menu principal")
#                                 break #salir del menu secundario
#                             case _:
#                                 print("opcion invalida")
                        
#                 case 2:
                      
#                     print("has seleccionado comprar ")
#                     cant=int(input("cuantas entradas desea comprar?"))
#                     if cant <= Sinicial and cant>0:#??
#                       Sinicial-= cant
#                       print("has comprado con exito quedan  esta cantidad de entradas disponibles", Sinicial)
#                     else:
#                       print(" no hay suficientes entradas")
#                 case 3:
#                     print("Salir del sistema")
#                     break
#                 case _:
#                     print("opcion invalida")
    
#         except Exception:
#           print(" ingrese solo numeros enteros")

##################################### ejercicio de la prueba 
#EJERCICIO 1
 # Construya un programa en Python que permita registrar empleados de una empresa y verificar si cada uno tiene más de 10 años de antigüedad.
 # Primero se debe ingresar la cantidad de empleados a registrar. Este número debe ser entero.
 # Luego, para cada empleado, se debe pedir su nombre y los años de antigüedad.
 # El programa debe indicar si el empleado tiene "Más de 10 años de antigüedad" o "10 o menos años de antigüedad".
 # Al finalizar, se debe mostrar cuántos empleados tienen más de 10 años de antigüedad y cuántos no
# 

antiminima=10
mas10=0
menos10=0

while True:
    try:
        cant=int(input("ingrese la cantidad  de empleados"))
    except Exception:
        print("solo numeros")

    for i in range 
