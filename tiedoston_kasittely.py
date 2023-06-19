#read every line in file merkkijono.txt and check line with .isalnum()
tiedosto = open("merkkijonoja.txt","r")
for rivi in tiedosto:
    if rivi.isalnum():
        print(rivi)
    else:
        print(rivi.strip())