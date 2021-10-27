print ("Algoritimos em laços de repetição")
w=0
while (w<1):
    escolha = int(input("\n 1- 10 nº e leia o maior; \n 2- Caixa mercado \n 3- Salario Funcionario \n Digite a função desejada:"))
    if escolha == 1:
        x=1
        soma=0
        maior =0
        while (x<=10):
            i=int(input ('\n Digite um numero: '))
            soma += i
            if i>maior:
                maior=i
            x += 1
        print (" O maior numero é:",maior,"\n A soma dos valores é: ", soma, "\n A média dos númeors é: ", soma/10)

        
    elif escolha == 2:
        soma = 0
        cond = 1
        while (cond == 1):
            y = int(input("\n Digite 1 para registar produto, se não precione qualquer tecla: "))
            if y == 1:
                preco = int(input("\n Digite o valor do protudo: "))
                quant = int(input(" Digite a quantidade de protudos: "))
                soma += preco*quant
            else:
                print ("O valor da compra é: ", soma)
    elif escolha == 3:
        cond = 1
        while (cond==1):
            f=1
            while f<=15:
                salario=float(input("\n Digite o salario por hora do funcionario: "))
                hora=float(input("\n Digite as horas trabalhadas pelo funcionario no mês: "))
                print ("O salário do funcionario é: ", salario*hora)
            f+=1
   
        

