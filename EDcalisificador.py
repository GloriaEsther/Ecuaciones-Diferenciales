import os
from sys import setswitchinterval
print ("Gloria Esther Mtz Mtz")
print ("Clasificador de Ecuaciones Diferenciales (1er Orden y 2do Orden)")

salir=False
opcion= 0

while not salir:
    menu="""
    1.- Mi ecuación tiene una derivada
    2.- Mi ecuacion tiene dos derivadas
    3.- Salir
    """

    print (menu)
    print("Elige una de las siguientes opciones:")
    opcion= input ("Ingrese la opcion que eligio: ")
    
    if opcion=='1':
       print("¿Cual es el grado de su ecuacion(el mayor exponente de la mayor derivada)?")
       potencia=int(input("Ingrese el valor: "))
       print(f"La ecuacion diferencial es de tipo ORDINARIA")
       print(f"La ecuacion es de Orden 1")
       print(f"La ecuacion tiene un Grado de ",potencia)


    elif opcion == '2':
        print("¿Cual es el grado de su ecuacion(el mayor exponente de la mayor derivada)?")
        potencia=int(input("Ingrese el valor: "))
        print("La ecuacion es de tipo PARCIAL")
        print("La ecuación es de Orden 2")
        print(f"La ecuacion es de Grado ",potencia)
        
        #opcion= pedirNumEnte()
    elif opcion == '3':
        salir = 'True'
    else:
        print("Porfavor vuelva a ingresar la opcion")
print ("Fin")

        


    
    
    
