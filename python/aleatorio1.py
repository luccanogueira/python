def mostrar_na_tela(salario, percentual, valor_do_aumento, salario_novo):
    print('O salário antes do reajuste era: %.2f.' % (salario))
    print('O percentual de aumento foi de: %d%%.' % (percentual))
    print('O valor do aumento foi de: %d.' % (valor_do_aumento))
    print('O novo salrio ficou em: %.2f.' % (salario_novo))
    

salario = float(input('Digite o salário: '))

if salario <= 280.00:
    calcula(salario, 20)
    
elif salario > 280.00 and salario <= 700.00:
    calcula(salario, 15)

elif salario > 700.00 and salario <= 1500.00:
    calcula(salario, 10)

else:
    calcula(salario, 5)
