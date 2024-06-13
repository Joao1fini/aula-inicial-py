# DESAFIO 03

# Crie um programa que leia vários números inteiros pelo
# teclado. No final da execução, mostre a média entre todos os
# valores e qual foi o maior e o menor valores lidos. O programa
# deve perguntar ao usuário se ele quer ou não continuar a
# digitar valores

vez=0
n1=0
menor=0
maior=0
soma=0
while True:
    if n1<menor:
        menor=n1
    if n1>maior:
        maior=n1
    n1=int(input("digite um numero: "))
    soma=soma+n1
    menor=n1
    vez+=1
    pergunta=input("que finalizar o jogo? (s/n) ")
    if pergunta=="s":
        media=soma/vez
        print(f"o maior valor foi {maior} e o menor foi {menor} e a media dos valores digitados foi {media}")
