print ("Contagem de pessoas em cada nível de escolaridade")
e1=0
e2=0
e3=0
e4=0
e5=0
pessoa=0
i_seg=0
m_pos=0
f_pos=0
x=0
while x<=1000:
    idade=0
    s=0
    escola=int(input("\n 0- Analfabeto \n 1- Primário \n 2-Segundario \n 3- Superio \n 4- Pós-graduação \n 5- Para ver o resultado\n Digite:"))
    if escola==0:
        s=int(input("\n Digite 1 para masculino e 2 para feminino"))
        idade=int(input("\n Digite sua idade:"))
        e1=e1+1
        pessoa=pessoa+1
        x=x+1
        print("\n Pessoa registrada")
    elif escola==1:
        s=int(input("\n Digite 1 para masculino e 2 para feminino"))
        idade=int(input("\n Digite sua idade:"))
        e2=e2+1
        pessoa=pessoa+1
        x=x+1
        print("\n Pessoa registrada")
    elif escola==2:
        s=int(input("\n Digite 1 para masculino e 2 para feminino"))
        idade=int(input("\n Digite sua idade:"))
        if idade<=50:
            e3=e3+1
            pessoa=pessoa+1
            x=x+1
            print("\n Pessoa registrada")
        else:
            e3=e3+1
            i_seg=i_seg+1
            pessoa=pessoa+1
            x=x+1
            print("\n Pessoa registrada")
    elif escola==3:
        s=int(input("\n Digite 1 para masculino e 2 para feminino"))
        idade=int(input("\n Digite sua idade:"))
        e4=e4+1
        pessoa=pessoa+1
        x=x+1
        print("\n Pessoa registrada")
    elif escola==4:
        s=int(input("\n Digite 1 para masculino e 2 para feminino"))
        idade=int(input("\n Digite sua idade:"))
        if s==1:
            e5=e5+1
            m_pos=m_pos+1
            pessoa=pessoa+1
            x=x+1
            print("\n Pessoa registrada")
        else:
            e5=e5+1
            f_pos=f_pos+1
            pessoa=pessoa+1
            x=x+1
            print("\n Pessoa registrada")
    else:
        print(" Foram registradas um total de", pessoa, "pessoas \n Onde", e1, "são analfabetas \n", e2,
              "Tem apenas o primário \n", e3, "Tem apenas o secundário, desses", i_seg, "são pessoas com 50 anos ou mais \n",  e4,
              "Tem o superior \n", e5, "Tem pós graduação onde", m_pos, "são homens e", f_pos, "são mulheres")
