import random
import time
l = "2" , "3" , "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"
while True:
	b = random.randint(0, 12)
	a = random.randint(0, 12) 
	print(l[a])
	time.sleep(1)
	print(l[b])
	time.sleep(1)
	if a < b:
		print("Mal")
	elif a > b:
		print("Bien")
		break