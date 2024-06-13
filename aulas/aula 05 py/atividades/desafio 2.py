# DESAFIO 02

# Escreva um programa que leia dois números inteiros e
# compare- os, mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

n1=int(input("digite um numero: "))
n2=int(input("digite mais um numero: "))
if n1==n2:
    print("eles sao iguais")
else:
    if n1>n2:
        print(f"o {n1} é o maior numero e o {n2} o menor a diferença entre eles é de {n1-n2}")
    else:
        print(f"o {n2} é o maior numero e o {n1} o menor a diferença entre eles é de {n2-n1}")
    