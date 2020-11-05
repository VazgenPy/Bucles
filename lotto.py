import random
while True:
	a = random.sample(range(1,49), 6)
	print(a)
	b = str(input("Lo quieres? (si o no) \n"))
	if b == "Si" or b == "si":
		print("Has elegido el numero" , a)
		break
	elif b == "No" or b == "no":
		continue
	else:
		print("Muy mal no puedes poner eso")
		print("Te quedas con este numero por listo" , a)
		break