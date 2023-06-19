import math

def lue_luku():
    while True:
        luku = input("Anna luku: ")
        try:
            luku = int(luku)
            return luku
        except ValueError:
            print("Virheellinen syöte!")

def laske_tulos(valinta, luku1, luku2):
    if valinta == 1:
        return luku1 + luku2
    elif valinta == 2:
        return luku1 - luku2
    elif valinta == 3:
        return luku1 * luku2
    elif valinta == 4:
        return luku1 / luku2
    elif valinta == 5:
        return math.sin(luku1 / luku2)
    elif valinta == 6:
        return math.cos(luku1 / luku2)
    else:
        return None

def main():
    luku1 = lue_luku()
    luku2 = lue_luku()
    valitut_luvut = [luku1, luku2]

    while True:
        print("(1) +\n(2) -\n(3) *\n(4) /\n(5)sin(luku1/luku2)\n(6)cos(luku1/luku2)\n(7)Vaihda luvut\n(8)Lopeta")
        print("Valitut luvut:", luku1, luku2)
        valinta = input("Tee valinta (1-8): ")

        try:
            valinta = int(valinta)
            if valinta == 7:
                luku1 = lue_luku()
                luku2 = lue_luku()
                valitut_luvut = [luku1, luku2]
            elif valinta == 8:
                print("Lopetetaan.")
                break
            else:
                tulos = laske_tulos(valinta, luku1, luku2)
                if tulos is not None:
                    print("Tulos on:", tulos)
                else:
                    print("Virheellinen valinta!")
        except ValueError:
            print("Virheellinen valinta!")

if __name__ == "__main__":
    main()
