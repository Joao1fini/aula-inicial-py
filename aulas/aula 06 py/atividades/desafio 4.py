# DESAFIO 04

# Refaça o DESAFIO 09, mostrando a tabuada de um número
# que o usuário escolher, só que agora utilizando um laço for.

n1=int(input("digite um numero: "))
op=input("escolha a operação:" )
op=op.upper()
if op=="+" or op=="MAIS":
    for num in range(1,11):
        cont=n1+num
        print(f"o resultado de {n1}+{num}={cont}")
elif op=="-" or op=="MENOS":
    for num in range(1,11):
        cont=n1-num
        print(f"o resultado de {n1}-{num}={cont}")
elif op=="*" or op=="VEZES" or op=="X":
    for num in range(1,11):
        cont=n1*num
        print(f"o resultado de {n1}X{num}={cont}")
elif op=="/" or op=="DIVIDIR" or op=="DIVISAO":
    n1=float
    for num in range(1,11):
        cont=n1/num
        print(f"o resultado de {n1}/{num}={cont}")