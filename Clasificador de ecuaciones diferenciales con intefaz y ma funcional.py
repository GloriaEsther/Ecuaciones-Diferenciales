import tkinter
from sympy import*
print("Clasificador de Ecuaciones Diferenciales (1er Orden y 2do Orden)")
################################################################################################

ventana = tkinter.Tk()
ventana.geometry("600x400")
# FUNCIONES

def imprimirTodo():
    orden = int(agregar_orden.get())
    grado = int(agregar_potencia.get())
    variableMas= bool(agregar1_variable.get())
    print("******************************************************************")
    if orden > 1:
        print("Tu ecuacion es de Orden Superior y de: " + str(orden))
    else:
        print("Tu ecuacion es de primer Orden ")
    if variableMas == True:
        print("Tu ecuacion es Parcial")
    else:
        print("Tu ecuacion es Ordinaria")
    if grado > 1:
        print('El grado de tu ecuacion es de : ' + str (grado))
    print("*******************************************************************")
##############################################################################################
x=symbols('x')
y=Function('y')

ED = Eq(diff(y(x))-5*y(x), x/3)
dsolve(ED, y(x))
ED2 = Eq(diff(y(x))-5*y(x), 8)
CI = {y(0): 10}
dsolve(ED2, y(x), ics=CI)

#ETIQUETAS
etiqueta = tkinter.Label(ventana, text="Clasificador de Ecuaciones Diferenciales", font=("arial", 18),bg="#3F33FF",
                         width=2, height=2)
etiqueta.pack(fill = tkinter.X)
#Colores
#Verde Oscuro 3f5b0b
#Verde Claro 6d8517
#Amarillo Marron d1b834
#Amarillo Claro f2d16c
#Amarillo Huevo fcea8c

#####################################################################################################################


#CAJAS DE TEXTO
########################    Funcion   #############################
agregar_funcion = tkinter.Entry(ventana, text="Agrega el exponente que desee usar", bg="#3F33FF",
                                width="20", font=("helvetica 15"))
agregar_funcion.place(x=14, y=80)#y=80
#######################     Parrafos_Funcion   ######################################
agregar_funcion1 = tkinter.Label(ventana, text="Agrega tu funcion! deseada", bg="#3F33FF",
                                 width="30", font=("helvetica 15"))
agregar_funcion1.place(x=255, y=80)#78
########################    Variable simbolica    #############################
agregar_variable= tkinter.Entry(ventana, text="Agregar Orden correspondiente ", bg="#3F33FF",
                                width="20", font=("helvetica 15"))
agregar_variable.place(x=14, y=130)
#######################     Parrafos_VariableSimbolica   ######################################
agregar_funcion1 = tkinter.Label(ventana, text="Agrega tu variable! correspondiente", bg="#3F33FF",
                                 width="30", font=("helvetica 15"))
agregar_funcion1.place(x=255, y=130)
########################    Orden     ###############################
agregar_orden = tkinter.Entry(ventana, text="Agregar variable simbolica correspondiente", bg="#3F33FF",
                              width="20", font=("helvetica 15"))
agregar_orden.place(x=14, y=180)
#######################     Parrafos Orden   ######################################
agregar_funcion1 = tkinter.Label(ventana, text="¿De que orden deseas tus derivadas?", bg="#3F33FF",
                                 width="30", font=("helvetica 15"))
agregar_funcion1.place(x=255, y=180)
###########################     Potencia   ############################
agregar_potencia = tkinter.Entry(ventana, text="Elevar la funcion",bg="#3F33FF",
                                 width="20", font=("helvetica 15"))
agregar_potencia.place(x=14, y=230)
#######################     Parrafos_Potencia   ######################################
agregar_funcion1 = tkinter.Label(ventana, text="Agrega la Potencia necesaria", bg="#3F33FF",
                                 width="30", font=("helvetica 15"))
agregar_funcion1.place(x=255, y=230)
########################    Variable simbolica    #############################
agregar1_variable= tkinter.Entry(ventana, text="Ingrese el orden", bg="#3F33FF",
                                 width="20", font="helvetica 15")
agregar1_variable.place(x=14, y=280)
#######################     Parrafos de Variable Simbolica   ######################################
agregar_funcion1 = tkinter.Label(ventana, text="Agrega tu segunda variable", bg="#3F33FF",
                                 width="30", font="helvetica 15")
agregar_funcion1.place(x=255, y=280)

###########################################################################################################

# BOTONES
#    Obtener Clasificacion      #
obtener_Clasificacion = tkinter.Button(ventana, text="Obtener Clasificacion", command=imprimirTodo)
obtener_Clasificacion.place(x=450, y=350)
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

ventana.mainloop()
