def tulostaja(sana):
	print(sana)

def main():
	sana= str(input("Anna syöte (Lopeta lopettaa):"))
	while sana != "Lopeta":
		
		if len(sana) > 5:
			tulostaja(sana)
		else:
			tulostaja("Oletustulostus")
		sana= input("Anna syöte (Lopeta lopettaa):")
		
		
	

if __name__ == "__main__":
    main()
