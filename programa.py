
n1= int(input())
n2= int(input())
n= 2
t = True
a= []
while t:    
    if n1!=1 or n2!=1:
        f=True
        while f:
            #primeiro faz a fatoração dos numeros pelos primos a armazena eles em a
             if (n1%n)!=0 and (n2%n)==0:
                 n2=n2/n
                 a.append(n)
             elif (n1%n)==0 and (n2%n)==0:
                 n1= n1/n
                 n2= n2/n
                 a.append(n)
             elif (n1%n)==0 and (n2%n)!=0:
                 n1=n1/n
                 a.append(n)
             else:
                 f=False
                 y=True
                
    else:
        # o loop itera ate os valores de n1 e n2 serem 1 ou seja ate a fatoração terminar
        t=False
        y=False
    count=2
    #aqui calcula o proximo primo
    n=n+1
    while y:
        if (n % count) == 0:
            if n == count:
                y=False
            else:
                #alem de verificar o numero seguinte reseta o count para testar os valores a partir do 2 de novo
                n=n+1
                count=2
        else:
            count=count+1
        
p=1
c=0
#multiplica os valores em a para calcular o mmc
while c<len(a):
    p=p*a[c]
    c=c+1
print(a)
print(p)
        
        
