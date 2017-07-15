#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk

raiz = Tk()

raiz.geometry('600x300') #Anchura y altura

#Asignar un color de fondo
raiz.configure(bg = 'gray')

#Asignar un titulo a la ventana
raiz.title('Calculadora')

#Definir un boton inferior 'salir' para terminar el programa
ttk.Button(raiz, text='Salir', command=quit).pack(side=BOTTOM)

#Esta linea ejecuta el programa esperando que se interactue en el
raiz.mainloop()