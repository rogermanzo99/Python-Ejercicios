#!/usr/bin/env python
# -*- coding: utf-8 -*-
while True:
	print("Presione '1' para realizar una suma")
	print("Presione '2' para realizar una resta")
	print("Presione '3' para realizar una multiplicacion")
	print("Presione '4' para realizar una division")
	print("Presione '5' para salir de la calculadora ")

	user = input("")
	user = int(user)

	if user == 1:
		print ("Ingrese el primer digito: \n")
		a = input("")
		print ("Ingrese el segundo digito: \n")
		b = input("")
		operacion = float(a + b)
		resultado = (operacion)
		print ("El resultado de la suma es %s" %(resultado))

	elif user == 2:
		print("Ingrese el primer digito:")
		a = input("")
		print("Ingrese el segundo digito:")
		b = input("")
		operacion = float(a - b)
		resultado = (operacion)
		print ("El resultado de la resta es %s" %(resultado))

	elif user == 3:
		print("Ingrese el primer digito:")
		a = input("")
		print("Ingrese el segundo digito:")
		b = input("")
		operacion = float(a * b)
		resultado = (operacion)
		print ("El resultado de la multiplicación es %s" %(resultado))

	elif user == 4:
		print("Ingrese el primer digito:")
		a = input("")
		print("Ingrese el segundo digito:")
		b = input("")
		operacion = float(b / a)
		resultado = (operacion)
		print ("El resultado de la división es %s" %(resultado))

	elif user == 5:
		print("Gracias por usar nuestra calculadora")
		break