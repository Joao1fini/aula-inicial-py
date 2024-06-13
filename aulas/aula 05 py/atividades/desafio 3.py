# DESAFIO 03

# Crie um programa que leia duas notas entre 0 a 10 de um aluno
# e calcule sua média, mostrando uma mensagem no final, de
# acordo com a média atingida.

# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 a 6.9: RECUPERAÇÃO
# Média igual ou superior a 7.0: APROVADO

print("insira suas notas de 0 a 10")
n1=int(input("insira a nota da prova: "))
n2=int(input("insira a nota da redação: "))
media=(n1+n2)/2
if media>7:
    print(f"PARABENS SUA MEDIA FOI {media}, VOCÊ PASSOU")
elif media>5 and media<6.9:
    print(f"VOCÊ ESTA DE RECUPERAÇÃO, POIS SUA MEDIA FOI {media} COM {7-media} pontos abaixo do necessario")
else:
    (f"PARABENS VOCÊ ESTA OFICIALMENTE REPROVADO")