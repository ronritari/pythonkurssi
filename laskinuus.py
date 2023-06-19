import math

luku1 = 0
luku2 = 0

while True:
    print("(1) +")
    print("(2) -")
    print("(3) *")
    print("(4) /")
    print("(5) sin(luku1/luku2)")
    print("(6) cos(luku1/luku2)")
    print("(7) Vaihda luvut")
    print("(8) Lopeta")
    print("Valitut luvut:", luku1, luku2)
    valinta = input("Tee valinta (1-8): ")

    if valinta == "1":
        tulos = luku1 + luku2
        print("Tulos on:", tulos)
    elif valinta == "2":
        tulos = luku1 - luku2
        print("Tulos on:", tulos)
    elif valinta == "3":
        tulos = luku1 * luku2
        print("Tulos on:", tulos)
    elif valinta == "4":
        tulos = luku1 / luku2
        print("Tulos on:", tulos)
    elif valinta == "5":
        tulos = math.sin(luku1 / luku2)
        print("Tulos on:", tulos)
    elif valinta == "6":
        tulos = math.cos(luku1 / luku2)
        print("Tulos on:", tulos)
    elif valinta == "7":
        luku1 = float(input("Anna ensimmäinen luku: "))
        luku2 = float(input("Anna toinen luku: "))
    elif valinta == "8":
        break
    else:
        print("Tuntematon valinta.")
