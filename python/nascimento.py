dia = int(input("Digite o dia em que você nasceu:"))
mes = int(input("Agora digite o mes em que você nasceu:"))
ano = int(input("Agora digite o ano em que você nasceu:"))
condicao  = ""
if dia < 30:
    condicao = "Essa data não existe."
    print (condicao)
elif mes < 12:
    print (condicao)
elif ano < 2019 and ano > 1915:
    print (condicao)
else:
    print ("Você nasceu em", dia, "/", mes, "/", ano, "e seu aniversario será", dia, "/", mes, "/2019")

    

