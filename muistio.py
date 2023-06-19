import os
import datetime

def tarkista_muistio(tiedoston_nimi):
    """
    Check if the specified file exists. If it does not exist, create the file. 
    :param tiedoston_nimi: the name of the file to be checked or created
    :return: None
    """
    if not os.path.exists(tiedoston_nimi):
        print("Oletusmuistioa ei löydy, luodaan tiedosto.")
        try:
            with open(tiedoston_nimi, "w") as tiedosto:
                pass
        except IOError:
            print("Tiedoston luominen epäonnistui.")

def vaihda_muistio():
    """
    Prompts user for a file name, checks if the file exists and creates it if it doesn't.
    
    :return: The name of the created file.
    """
    tiedoston_nimi = input("Anna tiedoston nimi: ")
    if not os.path.exists(tiedoston_nimi):
        print("Tiedostoa ei löydy, luodaan tiedosto.")
        try:
            with open(tiedoston_nimi, "w") as tiedosto:
                pass
        except IOError:
            print("Tiedoston luominen epäonnistui.")
    return tiedoston_nimi

def lue_muistiota(tiedoston_nimi):
    """
    Reads the contents of a file and prints out each line. 

    :param tiedoston_nimi: A string representing the name of the file to read.
    :type tiedoston_nimi: str
    :return: None
    """
    try:
        with open(tiedoston_nimi, "r") as tiedosto:
            merkinnat = tiedosto.readlines()
            for merkinta in merkinnat:
                print(merkinta.strip())
    except IOError:
        print("Tiedoston lukeminen epäonnistui.")

def lisaa_merkinta(tiedoston_nimi):
    """
    Adds a new entry to a given file with the current timestamp and a user inputted message.

    :param tiedoston_nimi: A string representing the name of the file to add the entry to.
    :type tiedoston_nimi: str
    :return: None
    :rtype: None
    """
    merkinta = input("Kirjoita uusi merkintä: ")
    aika = datetime.now().strftime("%H:%M:%S %d/%m/%y")
    try:
        with open(tiedoston_nimi, "a") as tiedosto:
            tiedosto.write(f"{merkinta}:::{aika}\n")
    except IOError:
        print("Merkinnän lisääminen epäonnistui.")

def tyhjenna_muistio(tiedoston_nimi):
    """
    Empties the contents of a file with the given filename.

    :param tiedoston_nimi: The name of the file to be emptied.
    :type tiedoston_nimi: str
    """
    try:
        with open(tiedoston_nimi, "w") as tiedosto:
            print("Muistio tyhjennetty.")
    except IOError:
        print("Muistion tyhjentäminen epäonnistui.")

def main():
    """
    Runs the main program loop for a simple text editor. 
    
    Args:
        None
    
    Returns:
        None
    """
    tiedoston_nimi = "muistio.txt"
    tarkista_muistio(tiedoston_nimi)
    print("Käytetään muistiota:", tiedoston_nimi)

    while True:
        print("(1) Lue muistikirjaa")
        print("(2) Lisää merkintä")
        print("(3) Tyhjennä muistikirja")
        print("(4) Vaihda muistiota")
        print("(5) Lopeta")

        valinta = input("Mitä haluat tehdä?: ")

        if valinta == "1":
            lue_muistiota(tiedoston_nimi)
        elif valinta == "2":
            lisaa_merkinta(tiedoston_nimi)
            print("Käytetään muistiota:", tiedoston_nimi)
        elif valinta == "3":
            tyhjenna_muistio(tiedoston_nimi)
        elif valinta == "4":
            tiedoston_nimi = vaihda_muistio()
            print("Käytetään muistiota:", tiedoston_nimi)
        elif valinta == "5":
            print("Lopetetaan.")
            break
        else:
            print("Virheellinen valinta!")

if __name__ == "__main__":
    main()
