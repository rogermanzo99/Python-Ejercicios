#-*- encoding: utf-8 -*-

from Tkinter import *

def Sumar():
	resultado.set("La suma es = " +str(float(vartxt1.get())+float(vartxt2.get())))
def Restar():
	resultado.set("La resta es = " +str(float(vartxt1.get())-float(vartxt2.get())))
def Multiplicar():
	resultado.set("La multiplicacion es = " +str(float(vartxt1.get())*float(vartxt2.get())))
def Dividir():
	resultado.set("La división es = " +str(float(vartxt2.get())/float(vartxt1.get())))
def limpiar():
	resultado.set("")
	vartxt1.set("")
	vartxt2.set("")

ventana = Frame(height=250, width=250)
ventana.pack(padx=5,pady=5)

vartxt1= StringVar()
txt1 = Entry(ventana, textvariable=vartxt1).place(x=0,y=0)

vartxt2= StringVar()
txt2 = Entry(ventana, textvariable=vartxt2).place(x=123,y=0)

resultado= StringVar()
txt3 = Entry(ventana, textvariable=resultado,width=100).place(x=0,y=140)



bsu = Button(ventana,command=Sumar, text="Sumar",padx=40,pady=5, background="#58FA82").place(x=0,y=25)
bre = Button(ventana,command=Restar, text="Restar",padx=40,pady=5, background="#58FA82").place(x=130,y=25)
bmu = Button(ventana,command=Multiplicar, text="Multiplicar",padx=30,pady=5, background="#58FA82").place(x=0,y=65)
bdi = Button(ventana,command=Dividir, text="Dividir",padx=40,pady=5, background="#58FA82").place(x=130,y=65)
blim = Button(ventana,command=limpiar, text="limpiar",padx=110,pady=5,background="#F4FA58").place(x=0,y=100)

ventana.mainloop()