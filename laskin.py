luku1 = int(input("Anna luku:"))
luku2 = int(input("Anna toinen luku:"))

print("""(1) +
(2) -
(3) *
(4) /
(5)Vaihda luvut
(6)Lopeta""")


while True:
	valinta = int(input("Tee valinta (1-4):"))
	if valinta == 1:
		tulos = luku1 + luku2
		print("Tulos on:",tulos)
	elif valinta == 2:
		tulos = luku1 - luku2
		print("Tulos on:",tulos)
	elif valinta == 3:
		tulos = luku1 * luku2
		print("Tulos on:",tulos)
	elif valinta == 4:
		tulos = luku1 / luku2
		print("Tulos on:",tulos)
	elif valinta == 5:
		luku1 = int(input("Anna uusi ensimmäinen luku:"))
		luku2 = int(input("Anna uusi toinen luku:"))	
	elif valinta == 6:
		break
	else:
		print("Valintaa ei tunnistettu.")