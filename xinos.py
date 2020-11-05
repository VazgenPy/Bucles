import random
v = 0
d = 0
p = int(input("Cuantas partidas quieres: "))
while True:
	xa = int(input("Cuantos xinos escoges de (0 a 3): "))
	xm = int(random.randint(0,3))
	xr = int(input("Cuantos xinos crees que hay en total: "))
	if xr == xm + xa:
		print("La maquina tenia: " , xm , "xinos")
		print("-------------------------------------------")
		print("Has ganado") 
		print("-------------------------------------------")
		v = v+1
	elif xr != xm + xa:
		print("La maquina tenia: " , xm , "xinos")
		print("-------------------------------------------")
		print("Has perdido")
		print("-------------------------------------------")
		d = d+1
	if v + d == p:
		print("\033[;32m" , "Has ganado " , v)
		print("\033[;31m" , "Has perdido " , d)
		break