from curses import def_prog_mode
#Programa hecho en clase (el 07/09/22)
import random
class Arreglo:
    a=[]

def __int__(self):
    print(self.a)
def llamarArre(self,i):
    if(i==5):
        return
    self.a.append(random.randint(1,100))#append es para llenar arreglo
    self.llenarArre(i+1)

def despArre(self):
    print(self.a)
def despRevArre(self):
    print(self.a[::-1])

def sumaArre(self,i):
    if(i==5):
     return 0
    return self.a[i]+self.sumaArre(i+1)

def promeArre(self,i):
    return self.a[i]+self.sumaArre(i)/5

def totalElementosArre(self):
    return len(self.a)
def sumaParesArre(self,i):
    if(i==5):
     return 0
    suma=0
    if(i%2==0):
       suma=suma+i      
    return suma+sumaParesArre(i+1)
def sumaImparesArre(self,i):
    if(i==5):
     return 0
    suma1=0
    if(i%2!=0):
        suma1=suma1+i
    return suma1+sumaImparesArre(i+1)

#from Arreglo import Arreglo
class MainArre:
    arre=Arreglo()

    def __init__(self):
        self.menu()
    def pedirOpcion(self):
        bien=False
        op=0
        while not bien:
            try:
                op=int(input("Teclea opcion: "))
                bien =True
            except ValueError:
               print("Error,introduce un entero: ")
        return op
    def menu(self):
        salir=False
        op=0
        
        while(not salir):
            print("1.-Generar un arreglo: ")
            print("2.-Desplegar arreglo: ")
            print("3.-Desplegar el arreglo al reves: ")
            print("4.-Sumar el arreglo: ")
            print("5.-Promedio del arreglo: ")
            print("6.-Mostrar total de elementos del arreglo: ")
            print("7.-Sumar numeros pares del arreglo: ")
            print("8.-Sumar numeros impares del arreglo: ")

            op=self.pedirOpcion()
            
            