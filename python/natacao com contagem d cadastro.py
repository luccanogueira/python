
print ("Algoritmo de categoria de idade")
x=0
q=0
y=0
w=0
z=0
a=0
while (x < 1000):
    n=int(input("Digite 1 para cadrastrar nova nadador: "))
    if n == 1:
        idade= int(input("Digite a idade do nadador:"))
        if idade>=5 and idade<=7:
            print("Esse nadador pertence a categoria Infantiu A")
            q+=1
        elif idade>=8 and idade<=10:
            print("Esse nadador pertence a categoria Infantiu B")
            y+=1
        elif idade>=11 and idade<=13:
            print("Esse nadador pertence a categoria Juvenil A")
            w+=1
        elif idade>=14 and idade<=17:
            print("Esse nadador pertence a categoria Juvenil B")
            z+=1
        else:
            print("Esse nadador pertence a categoria Adultos")
            a+=1
    else:
        print ("Foram cadrastrados", q, "na categoria Infantiu A", "\n Foram cadrastrados", y,"na categoria Infantiu B",
               "\n Foram cadrastrados", w, "na categoria Juvenil A","\n Foram cadrastrados", z, "na categoria Juvenil B",
               "\n Foram cadrastrados", a, "na categoria Adultos")
