#write a bubblesort function that takes a list of numbers and returns a sorted list in python
def bubblesort(list):    
    for i in range(len(list)-1):
        for j in range(len(list)-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

#simple calculator that asks user for two numbers and asks if the want to multiply or divide
def calculator():
    
    input1 = int(input("Anna ensimmäinen luku:"))
    input2 = int(input("Anna toinen luku:"))
    while True:
        valinta = int(input("Tee valinta (1-2):"))
        if valinta == 1:
            tulos = input1 + input2
            print("Tulos on:",tulos)
        elif valinta == 2:
            tulos = input1 - input2
            print("Tulos on:",tulos)
        elif valinta == 3:
            tulos = input1 * input2
            print("Tulos on:",tulos)
        elif valinta == 4:
            tulos = input1 / input2
            print("Tulos on:",tulos)
        elif valinta == 5:
        else:
            print("Valintaa ei tunnistettu.")


#write a function thet will add together the rounds of loops like 0+1+2+3+4+5 based on the user input
plus = int(input("Kuinka monta kierrosta?:"))
tulos = 0
for kierros in range(1,plus+1):
    tulos = tulos+kierros

print("Kertymäksi saatiin:",tulos)
