#-*- encoding: utf-8 -*-
while True:
	print("Escribe '1' si deseas convertir de Bolivares a Dolares")
	print("Escribe '2' si deseas convertir de Dolares a Bolivares")
	print("Escribe '3' si deseas salir del programa")
	user = input("")
	if user == "1":
		print ("Introduzca los bolivares: ")
		bsf= input("")
		bsf= int(bsf)
		print("Introduzca cuanto equivale un bolivar en dolares: ")
		#print("Introduzca actualmente, \n¿cuanto equivale 1Bsf en dolares?")
		usd= input("")
		usd= int(usd)
		r = float(bsf/usd)
		print(r)
	elif user == "2":
		print("Introduzca los dolares: ")
		usd= input("")
		usd= int(usd)
		print("Introduzca cuanto equivale un dolar en bolivares: ")
		bsf= input("")
		bsf= int(bsf)
		r= float(usd*bsf)
		print(r)
	elif user == "3":
		break