print("Algoritmo para conversão de moeda")
x = 0
while (x < 1):
    moeda=float(input("Digite qual a sua moeda (1-Real;2-Dólar;3-Euro):"))
    conv=float(input("Digite a moeda para conversão (1-Real;2-Dólar;3-Euro):"))
    valor=float(input("Digite o valor a ser convertido:"))
    if moeda==1 and conv==2:
        print("O valor da conversão é ", valor/3.85)
    elif moeda==1 and cov==3:
        print("O valor da conversão é", valor/4.34)
    elif moeda==2 and conv==1:
        print("O valor da conversão é ",valor*3.85)
    elif moeda==2 and conv==3:
        print("O valor da conversão é  ",valor*0.89)
    elif moeda==3 and conv==2:
        print("O valor da conversão é  ", valor*1.13)
    elif moeda==3 and conv==1:
        print("O valor da conversão é ",valor*4.34)
    else:
        print ("Digitação incorreta")
    

    
