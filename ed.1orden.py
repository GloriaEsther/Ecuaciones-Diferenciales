import os
from sys import setswitchinterval
print ("Autor: Gloria Esther Mtz Mtz")
print ("Clasificador de Ecuaciones Diferenciales (1er Orden y 2do Orden)")


#def pedirNumEnte():
    #correcto= False
    #num=0
    #while(not correcto):
        #try:
           # num=int(input("Introuduce un numero correcto: "))
           # correcto=True
       # except ValueError:
            #print("Error, introduce un numero entero")

  #  return num

salir=False
opcion= 0

while not salir:
    menu="""
    [1] Mi ecuación tiene una derivada
    [2] Mi ecuacion tiene dos derivadas
    [3] Salir
    """

    print (menu)
    print("Elige una opcion")
    opcion= input ("Ingrese la opcion que eligio: ")
    
    if opcion=='1':
       print("¿Cual es el grado de su ecuacion(el mayor exponente de la mayor derivada)?")
       potencia=int(input("Ingrese el valor: "))
       print(f"La ecuacion diferencial es de tipo ORDINARIA")
       print(f"La ecuacion es de Orden 1")
       print(f"La ecuacion tiene un Grado de {potencia}")


       #opcion= pedirNumEnte()

    elif opcion == '2':
        print("¿Cual es el grado de su ecuacion(el mayor exponente de la mayor derivada)?")
        potencia=int(input("Ingrese el valor: "))
        print("La ecuacion es de tipo PARCIAL")
        print("La ecuación es de Orden 2")
        print(f"La ecuacion es de Grado {potencia}")
        
        #opcion= pedirNumEnte()
    elif opcion == '3':
        salir = 'True'
    else:
        print("Ingrese un numero entre 1 y 3")
print ("Fin")

        


    
    
    
