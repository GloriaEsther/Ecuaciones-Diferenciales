import tkinter
print ("Clasificador de Ecuaciones Diferenciales (1er Orden y 2do Orden)")
ventana = tkinter.Tk()
ventana.geometry("600x750")
#FUNCIONES
#######################################AYUDA###################################
def imprimirTodo():
    orden = int(agregar_orden.get())
    grado = int(agregar_potencia.get())
    variableMas= bool(agregar1_variable.get())
    print ("******************************************************************")
    if orden > 1:
        print ("Tu ecuacion es de Orden Superior y de: " + str(orden))
    else:
        print("Tu ecuacion es de primer Orden ")
    if variableMas == True:
        print ("Tu ecuacion es Parcial")
    else:
        print ("Tu ecuacion es Ordinaria")
    if grado > 1:
        print ('El grado de tu ecuacion es de : ' + str (grado))
    print ("*******************************************************************")

#ETIQUETAS
etiqueta = tkinter.Label(ventana, text="Clasificador de Ecuaciones Diferenciales", font=("helvetica", 20),bg="#6d8517"
                        ,width=6,height=2)
etiqueta.pack(fill = tkinter.X)
#Colores
#verde oscuro 3f5b0b
#Verde claro 6d8517
#Amarillo Marron d1b834
#Amarillo Claro f2d16c
#Amarillo Huevo fcea8c


#CAJAS DE TEXTO
########################    Funcion   #############################
agregar_funcion = tkinter.Entry(ventana,text="Agrega el exponente que desee usar",bg="#fcea8c",
                        width="20",font=("helvetica 15"))
agregar_funcion.place(x=14, y=80)
#######################     Parrafos_Funcion   ######################################
agregar_funcion1 = tkinter.Label(ventana,text="Agrega tu funcion! deseada",bg="#fcea8c",
                        width="30",font=("helvetica 15"))
agregar_funcion1.place(x=255, y=78)
########################    Variable simbolica    #############################
agregar_variable= tkinter.Entry(ventana,text="Agregar Orden correspondiente ",bg="#fcea8c",
                        width="20",font=("helvetica 15"))
agregar_variable.place(x=14, y=130)
#######################     Parrafos_VariableSimbolica   ######################################
agregar_funcion1 = tkinter.Label(ventana,text="Agrega tu variable! correspondiente",bg="#fcea8c",
                        width="30",font=("helvetica 15"))
agregar_funcion1.place(x=255, y=130)
########################    Orden     ###############################
agregar_orden = tkinter.Entry(ventana,text="Agregar variable simbolica correspondiente",bg="#fcea8c",
                        width="20",font=("helvetica 15"))
agregar_orden.place(x=14, y=180)
#######################     Parrafos Orden   ######################################
agregar_funcion1 = tkinter.Label(ventana,text="¿De que orden deseas tus derivadas?",bg="#fcea8c",
                        width="30",font=("helvetica 15"))
agregar_funcion1.place(x=255, y=180)
###########################     Potencia   ############################
agregar_potencia = tkinter.Entry(ventana,text="Elevar la funcion",bg="#fcea8c",
                        width="20",font=("helvetica 15"))
agregar_potencia.place(x=14, y=230)
#######################     Parrafos_Potencia   ######################################
agregar_funcion1 = tkinter.Label(ventana,text="Agrega la Potencia necesaria",bg="#fcea8c",
                        width="30",font=("helvetica 15"))
agregar_funcion1.place(x=255, y=230)
########################    Variable simbolica    #############################
agregar1_variable= tkinter.Entry(ventana,text="Ingrese el orden",bg="#fcea8c",
                        width="20",font=("helvetica 15"))
agregar1_variable.place(x=14, y=280)
#######################     Parrafos de Variable Simbolica   ######################################
agregar_funcion1 = tkinter.Label(ventana,text="Agrega tu segunda variable",bg="#fcea8c",
                        width="30",font=("helvetica 15"))
agregar_funcion1.place(x=255, y=280)



#BOTONES
###########################     Obtener Clasificacion       ##################################
obtener_Clasificacion = tkinter.Button(ventana,text="Obtener Clasificacion",command=imprimirTodo)
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
