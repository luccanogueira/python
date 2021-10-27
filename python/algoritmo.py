print ("Junção de Algoritmos")
x=0
while (x<1):
    escolha=int(input(" \n 1-Tipo de triangulo; \n 2-Lucro de venda; \n 3-Bilheteria trem; \n 4-Aumento de salário; \n 5-Calculadora Simples; \n Digite o código do programa que quer executar:"))
    if escolha==1:
        lad1=int(input("\n Digite o valor do primeiro lado do triangulo: "))
        lad2=int(input(" Digite o valor do segundo lado do triangulo: "))
        lad3=int(input(" Digite o valor do terceiro lado do triangulo: "))
        if lad1==lad2 and lad1==lad3:
            print ("\n O triangulo é equilatero!")
        elif (lad1==lad2 and lad1!=lad3) or (lad2==lad3 and lad2!=lad1):
            print ("\n O triangiulo é isósceles!")
        else:
            print ("\n O triangulo é escaleno!")
            
    elif escolha==2:
        valor=float(input("\n Digite o valor do produto comprado: "))
        if valor<20:
            print ("\n O produto deve ser revendido por:", valor*1.45)
        elif valor>20 and valor<=50:
            print (" O produto deve ser revendo por:", valor*1.30)
        else:
            print (" O produto deve ser revendo por:", valor*1.20)
            
    elif escolha==3:
        passagem=int(input(" \n 1-unitario \n 2-duplo \n 3-Até 10 viagens \n Escolha o tipo do bilete:"))
        quant=int(input("\n Digite quantas passagens deseja:"))
        valor=float(input(" Digite o valor que sera dado como pagamento:"))
        if passagem==1:
            print ("\n O valor total do bilhete unitario ficou: ", quant*4, "\n O troco será de:", valor-(quant*4))
        elif passagem==2:
            print (" O valor total do bilhete duplo ficou: ", quant*7, "\n O troco será de:", valor-(quant*7))
        elif passagem==3:
            print (" O valor total do bilhete de 10 viagens ficou: ", quant*30, "\n O troco será de:", valor-(quant*30))
        else:
            print (" Código não encontrado!")
            
    elif escolha==4:
        cargo=int(input(" \n 1-Gerente \n 2-Engenheiro \n 3-Técnico \n 4-Estagiario \n 5-Outros \n Digite o código do cargo do funcionario:"))
        salario=float(input("\n Digite o salario atual do funcionario: "))
        if cargo == 1:
            print("\n O salario atual é: ", salario, "O novo salario é: ", salario*1.10)
        elif cargo == 2:
            print(" O salario atual é: ", salario, "O novo salario é: ", salario*1.15)
        elif cargo == 3:
            print(" O salario atual é: ", salario, "O novo salario é: ", salario*1.20)
        elif cargo == 4:
            print(" O salario atual é: ", salario, "O novo salario é: ", salario*1.25)
        else:
            print (" Código não encontrado!")

    elif escolha==5:
        operacao=int(input("\n 1-Soma; \n 2-Subitração; \n 3-Multiplicação; \n 4-Divisão;"))
        n1=float(input("\n Digite o primeiro valor: "))
        n2=float(input(" Digite o segundo valor: "))
        if operacao == 1:
            print("O resultado do calculo é: ", round(n1+n2, 2))
        elif operacao == 2:
            print("O resultado do calculo é: ", round(n1-n2, 2))
        elif operacao == 3:
            print("O resultado do calculo é: ", round(n1*n2, 2))
        elif operacao == 4:
            print("O resultado do calculo é: ", round(n1/n2, 2))
        else:
            print("Código não encontrado")
        
    else:
        print ("\n Código não encontrado, digite novamente:")
        
        
    
    
