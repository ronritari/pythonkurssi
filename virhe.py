	luku = input("Anna luku: ")

  #koitetaan muuttaa syöte lukuarvoksi
 	try:
     	luku = int(luku)
     	print("Syöte oli kelvollinen.")

  #Jos tapahtuu mikä tahansa virhe,
  #Ajetaan except-osio
 	except:
     	print("Virheellinen syöte!.")