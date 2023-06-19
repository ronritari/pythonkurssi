def pituusmitta(sana):
	if len(sana)>0:
		print("Antamasi syöte oli",len(sana),"merkkiä pitkä")
	else:
		print("Et antanut syötettä")

def main():
	sana= str(input("Anna syöte (Lopeta lopettaa):"))
	while sana != "Lopeta":
		tulostaja(sana)
		sana= input("Anna syöte (Lopeta lopettaa):")
		
		
	

if __name__ == "__main__":
    main()
