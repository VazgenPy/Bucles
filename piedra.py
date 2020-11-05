import random
v = 0
d = 0
c = str(input("Dime tu nombre: "))
l = "u" , "Piedra" , "Papel" , "Tijeras"
while True:
	print("""
	1)Piedra
	2)Papel
	3)Tijeras
      	""")
	a = int(input("Que quieres: "))
	b = random.randint(1,3)
	if a == 1 and b == 1:
		print("Has elegido: " , l[a])
		print("La maquina ha elegido: " , l[b])
		print("Has empatado")
	elif a == 1 and b == 2:
		print("Has elegido: " , l[a])
		print("La maquina ha elegido: " , l[b])
		print("Has perdido")
		d = d+1 
	elif a == 1 and b == 3:
		print("Has elegido: " , l[a])
		print("La maquina ha elegido: " , l[b])
		print("Has ganado")
		v = v+1
	elif a == 2 and b == 1:
		print("Has elegido: " , l[a])
		print("La maquina ha elegido: " , l[b])
		print("Has ganado")
		v = v+1
	elif a == 2 and b == 2:
		print("Has elegido: " , l[a])
		print("La maquina ha elegido: " , l[b])
		print("Has empatado")
	elif a == 2 and b == 3:
		print("Has elegido: " , l[a])
		print("La maquina ha elegido: " , l[b])
		print("Has perdido")
		d = d+1
	elif a == 3 and b == 1:
		print("Has elegido: " , l[a])
		print("La maquina ha elegido: " , l[b])
		print("Has perdido")
		d = d+1
	elif a == 3 and b == 2:
		print("Has elegido: " , l[a])
		print("La maquina ha elegido: " , l[b])
		print("Has ganado")
		v = v+1
	elif a == 3 and b == 3:
		print("Has elegido: " , l[a])
		print("La maquina ha elegido: " , l[b])
		print("Has empatado")
	if v == 2 or d == 2:
		print("--------------------------------------------")
		print("\033[;32m"+ c , "Has ganado", v)
		print("\033[;31m"+ c , "Has perdido", d)	
		break	