print ("Algoritmo de categoria de idade")
x=0
while (x < 1):
    idade= int(input("Digite a idade do nadador:"))
    if idade>=5 and idade<=7:
        print("Esse nadador pertence a categoria Infantiu A")
    elif idade>=8 and idade<=10:
        print("Esse nadador pertence a categoria Infantiu B")
    elif idade>=11 and idade<=13:
        print("Esse nadador pertence a categoria Juvenil A")
    elif idade>=14 and idade<=17:
        print("Esse nadador pertence a categoria Juvenil B")
    else:
        print("Esse nadador pertence a categoria Adultos")
