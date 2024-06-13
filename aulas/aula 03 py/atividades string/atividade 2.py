# DESAFIO 02

# Crie um programa que leia o nome de uma cidade e siga se ela
# começa ou não com o nome “Santo”.
cidade= input("qual o nome da sua cidade? ")
divide=cidade.split()
print(f"{cidade} tem santo no nome? {'SANTO'in cidade.upper()}")
print(f"{cidade} como com o nome santo? {'SANTO'in {divide[0]}}")