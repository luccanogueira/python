print ("Algoritmo de calculo de salário") 
x=0
while (x<1):
    cargo=int(input("\n 1-Gerente;\n 2-Engenheiro; \n 3-Tecnico; \n 4-Estagiario; \n 5-Outros; \n Digite o cargo do funcionario: "))
    salario=float(input("\n Digite o atual salário do funcionario: "))
    if cargo == 1:
        print ("\n O salário atual é: ", salario ,
               "\n O novo salário será: ",  salario*1.10)
    elif cargo == 2:
        print ("\n O salário atual é: ", salario ,
               "\n O novo salário será: ", salario*1.15)
    elif cargo == 3:
        print ("\n O salário atual é: ", salario ,
               "\n O novo salário será: ", salario*1.20)
    elif cargo == 4:
        print ("O salário atual é: ", salario ,
               "\n O novo salário será: ", salario*1.25)
    else:
        print ("\n O salário atual é: ", salario ,
               "\n O novo salário será: ", salario*1.40)
    
        
