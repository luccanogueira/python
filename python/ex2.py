print ("Termos da sequência Fibonacci!")
x=1
n1=1
n2=0
n3=0
a=0
while (x<=30):
    a+=1
    print("A sequencia é", a,":", n3)
    n3= n1 + n2
    n1 = n2
    n2 = n3
    x+=1

