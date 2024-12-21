from cProfile import label
from errno import ETIME
import tkinter
from tkinter import font
from sympy import*
init_printing()

print ("Soluciones de Ecuaciones Diferenciales")
ventana = tkinter.Tk()
ventana.geometry("600x400")
##################################################################
def resultado():
    coeficiente=int(agregar_coeficiente.get())
    exponente=int(agregar_exponente.get())
    a=0
    b=0
    expo=0
    Expo=0
    if(coeficiente==1):
        a=int(input("Ingresa el coeficiente:"))
    if(coeficiente==2):
        a=int(input("Ingresa el primer coeficiente: "))
        b=int(input("Ingresa el segundo coeficiente: "))
    if(exponente==1):
        expo=int(input("Ingresa el primer exponente: "))
    if(exponente==2):
        expo=int(input("Ingresa el primer exponente: "))
        Expo=int(input("Ingresa el segundo exponente: "))

    #EDO
    x=symbols("X")
    y=Function("y")
    y(x).diff()
    diffeq=Eq(y(x).diff()+a*x**expo*y(x),b*x**Expo)
    #pprint(diffeq=Eq(y(x).diff()+a*x**expo*y(x),b*x**Expo),use_unicode=True)
    dsolve(diffeq,y(x))#Resuelve la ecuacion diferencial
    #Muestra el resultado
    pprint(dsolve(diffeq,y(x)),use_unicode=True)

###################################################################
#Etiquetas
etiqueta = tkinter.Label(ventana, text="Solucion de Ecuaciones Diferenciales", font=("arial", 18),bg="#3f5b0b"
                        ,width=2,height=2)
etiqueta.pack(fill = tkinter.X)

#Cajas de texto
#######################     Parrafos_Funcion   ######################################
#agregar_funcion1 = tkinter.Label(ventana,text="Agrega tu funcion! deseada",bg="#3F33FF",
#                        width="30",font=("helvetica 15"))
#agregar_funcion1.place(x=255, y=80)
########################  Variable independiente(simbolica)  #############################
agregar_funcion = tkinter.Entry(ventana,text="Agregue la variable deseada ",bg="#3F33FF",
                        width="20",font=("helvetica 15"))
agregar_funcion.place(x=14, y=80)
agregar_funcion1= tkinter.Label(ventana,text="Cual es tu variable independiente?",bg="#3F33FF",
                        width="30",font=("arial 16"))
agregar_funcion1.place(x=255, y=80)#x=255 y=80

#######################  Funcion ######################################
agregar_funcion= tkinter.Entry(ventana,text="Agregue funcion ",bg="#3F33FF",
                        width="20",font=("helvetica 15"))
agregar_funcion.place(x=14, y=80)
agregar_funcion1 = tkinter.Label(ventana,text="Elige tu funcion: ",bg="#3F33FF",
                        width="30",font=("arial 16"))
agregar_funcion1.place(x=255, y=130)#x=255,y=130

########################  Coeficientes   #############################
agregar_coeficiente= tkinter.Entry(ventana,text="Ingrese el coeficiente",bg="#3F33FF",
                        width="20",font=("helvetica 15"))
agregar_coeficiente.place(x=14, y=180)
agregar_funcion1= tkinter.Label(ventana,text="Cuantos coeficientes tiene?",bg="#3F33FF",
                        width="30",font=("arial 16"))
agregar_funcion1.place(x=255, y=180)

####################### Exponentes ######################################
agregar_exponente= tkinter.Entry(ventana,text="Ingrese el exponente",bg="#3F33FF",
                        width="20",font=("helvetica 15"))
agregar_exponente.place(x=14, y=230)
agregar_funcion1= tkinter.Label(ventana,text="Cuantos exponentes tiene? ",bg="#3F33FF",
                        width="30",font=("arial 16"))
agregar_funcion1.place(x=255, y=230)
#BOTONES
###########################     Obtener Solucion   ##################################
obtener_Solucion = tkinter.Button(ventana,text="Obtener Solucion",command=resultado)
obtener_Solucion.place(x=255, y=280)

"""###########################     Funcion       ##################################
boton_Exponente = tkinter.Button(ventana,text="Agregar Funcion",command=imprimirTodo)
boton_Exponente.place(x=330, y=80)
###########################     Variable Simbolica      ##################################
boton_Agregar_Otra = tkinter.Button(ventana,text="Agregar variable simbolica",command=imprimirTodo)
boton_Agregar_Otra.place(x=330, y=130)
###########################     Orden      ##################################
boton_Funcion = tkinter.Button(ventana,text="Agregar orden a la derivada",command=imprimirTodo)
boton_Funcion.place(x=330, y=180)
###########################     Exponente     ##################################
boton_Elevar_Funcion = tkinter.Button(ventana,text="Agregar exponente ",command=imprimirTodo)
boton_Elevar_Funcion.place(x=330, y=230)
###########################     Variable Simbolica++      ##################################
boton1_Agregar_Otra = tkinter.Button(ventana,text="Agregar otra variable simbolica",command=imprimirTodo)
boton1_Agregar_Otra.place(x=330, y=280)"""


ventana.mainloop()#para mostrarlo