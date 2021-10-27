pedido=int(input("Digite 1 para cachorro quente \n 2 para bauru simples \n 3para bauru com ovo \n 4 para hambúguer \n 5 para cheeseburguer \n para 6 refrigerante"))
x=0
cachorro=0
bauru_s=0
bauru_com_ovo=0
ham=0
chees=0
refri=0
while x>1000:
    if pedido ==1:
        cachorro = int(input("Digite quantos você deseja"))
    elif pedido==2:
        bauru_s = int(input("Digite quantos você deseja"))
    elif pedido ==3:
        bauru_com_ovo = int(input("Digite quantos você deseja"))
    elif pedido ==4:
        ham = int(input("Digite quantos você deseja"))
    elif pedido ==5:
        chees = int(input("Digite quantos você deseja"))
    elif pedido ==6:
        refri = int(input("Digite quantos você deseja"))
    else:
        print("A conta ficou em:", (cachorro*1.20)+(bauru_s*1.30)+(bauru_com_ovo*1.50)+(ham*1.20)+(chees*1.30)+(refri*1.00))
