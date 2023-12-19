def leitura():
    return (int(input("Digite um número ")))

def leitura(str):
    return (int(input(str)))

def media (a, b):
    return (a+b)/2

def calculamedia():
    v1=leitura()
    v2=leitura()
    m=media(v1,v2)
    return m

def negativos():
    qtdnegativos=0
    for i in range(5):    
        n=leitura("Qual o valor?")
        if n < 0:
            qtdnegativos+=1
    return qtdnegativos

#print(negativos())

def mediavalorespositivos():
    m=0
    s=0
    qtd=0
    v=leitura()
    while v >= 0:
        s+=v
        qtd+=1
        v=leitura()
    if qtd > 0:
        m=s/qtd
    return m    

def candidatos():
    v1=0; v2=0; v3=0; v4=0; v5=0; v6=0
    voto=leitura("Qual o seu voto?") 
    while voto > 0:
        if voto == 1:
            v1+=1
        elif voto == 2:
            v2+=1
        elif voto == 3:
            v3+=1
        elif voto == 4:
            v4+=1
        elif voto == 5:
            v5+=1
        elif voto == 6:
            v6+=1
        voto=leitura("Qual o seu voto?") 
    soma=v1+v2+v3+v4+v5+v6
    print("Candidato 1 = ", v1, " equivale a ", v1/soma*100)
    print("Candidato 2 = ", v2, " equivale a ", v2/soma*100)
    print("Candidato 3 = ", v3, " equivale a ", v3/soma*100)
    print("Candidato 4 = ", v4, " equivale a ", v4/soma*100)
    print("Candidato 5 = ", v5, " equivale a ", v5/soma*100)
    print("Candidato 6 = ", v6, " equivale a ", v6/soma*100)

candidatos()    

def retornos():
    return 1, 2, 3, 4

x= retornos()

#print(x)
#for i in x:
#    print (i)
 
#print(mediavalorespositivos())       
        

#print("Foram digitados ", negativos(), " números negativos")
#print ("A media é ", calculamedia())




def imc(peso, altura):
    return (peso/(altura*altura))

def ponderada(n1, n2, n3, p1, p2, p3):
    return (n1*p1+n2*p2+n3*p3)/(p1+p2+p3)

#print(media(10,15))
#print (imc(79,1.64))
#print(ponderada(6,7.9,9.5,2,3,4))


def calculamedia(n):
    soma = 0
    for i in range (n):
        v = leitura()
        soma+=v
    return soma

#print(calculamedia(3))

        
