# DESAFIO 04

# Faça um programa que leia três números e mostre qual é o
# maior e qual é o menor.

n1=int(input("digite um numero: "))
n2=int(input("digite um segundo numero: "))
n3=int(input("digite um terceiro numero: "))

if n1==n2 and n1==n3:
    print("todos sao iguais")
else:
    if n1<n2 and n1<n3:
        print(f"{n1} é o menor")
    elif n2<n1 and n2<n3:
        print(f"{n2} é o menor")
    else:
        print(f"{n3} é o menor")           
    if n1>n2 and n1>n3:
        print(f"{n1} é o maior numero")
    elif n2>n1 and n1>n3:
        print(f"{n2} é o maior numero")
    elif n3>n1 and n2:
        print(f"{n3} é o maior numero")