print ("Algoritmo de calculo passagem") 
x=0
while (x<1):
    tipo=int(input("\n 1-Bilhete Unitario;\n 2-Bilhete Duplo; \n 3-Bilhete 10 viagens; \n Escolha o tipo de passagem: "))
    quant=float(input("\n Digite a quantidade de passagens desejadas: "))
    valor=float(input("Digite o valor que sera dado para pagamento: "))
    if tipo == 1:
        print ("O valor total é: ", quant*4, "\n o troco será de: ", (quant*4)-valor)
    elif tipo == 2:
        print ("O valor total é: ", quant*7, "\n o troco será de: ", (quant*7)-valor)
    elif tipo == 3:
        print ("O valor total é: ", quant*30, "\n o troco será de: ", (quant*30)-valor)
        
    
        
