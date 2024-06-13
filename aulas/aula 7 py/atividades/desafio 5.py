# DESAFIO 05

# Crie um programa que leia a idade e o sexo de varias
# pessoas. A cada pessoa cadastrada, o programa deverá
# perguntar se o usuário quer ou não continuar. No final, mostre:

# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.
maior_de_idade=0
homens=0
mulheres=0
mulher_menos_20=0
cad=str(input("quer se registrar?(s/n) "))
while True:
    if cad.lower()=="s":
        sexo=input("você é homem ou mulher?(h/m) ")
        if sexo=="h":
            homens+=1
        else:
            mulheres+=1
        idade=int(input("qual a sua idade? "))
        if idade>18:
            maior_de_idade+=1
        if sexo=="m" and idade<20:
            mulher_menos_20+=1
        pergunta=input("quer registar mais alguem?(s/n) ")
        if pergunta=="n":
            pergunta2=input("pode sair?(s/n) ")    
            if pergunta2=="s":
                break
print(f"tem {maior_de_idade} pessoas maiores de idade")
print(f"tem um total de {homens} homens")
print(f"tem {mulher_menos_20} mulheres com menos de 20 anos de idade")
input()