# DESAFIO 01

# Crie um programa que leia o nome completo de uma pessoas
# e mostre O nome com todas as letras maiúsculas
# O nome com todas as letras minúsculas
# Quantas letras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome

nome = str(input("qual o seu nome?"))
mai = nome.upper()
small = nome.lower()
print(mai)
print(small)
jun=nome.replace(" ","")
print(f"{len(jun)}")
primeiro=nome.find(" ")
print(nome[:primeiro])