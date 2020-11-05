import random
a = random.randint(0,9)
while True:	
	b = int(input("Que numero es: "))
	if b == a:
		print("Bien")	
		break
	elif b != a:
		print("Mal")