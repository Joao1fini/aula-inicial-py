soma=0
n1=0
while n1<999:
        n1=int(input("digite um numero: "))
        if n1>=999:
            break
        else:
            soma+=n1
print(f"a soma de tudo que voce digitou deu {soma}")