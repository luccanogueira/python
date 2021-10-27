x = 0
while (x < 1):
    venda = ""
    m = int(input("Digite quantas maçãs seram vendidas:"))
    if m >= 1 and m < 11:
        venda = (m)
    elif m >= 11 and m < 21:
        venda = (m * 0.90)
    else:
        venda = (m * 0.80)
    print ("O valor da venda é:",venda)
    n = input ("Novo cliente?!")
    if n == "sim":
        x = 0
    else:
        x = 2
        break
        
    
