# DESAFIO 05

# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o ultimo nome
# separadamente

nome=input("escreva seu nome: ")
nomeseparado=nome.split()
print(f"seu primeiro nome {nomeseparado[0]}")
print(f"e o ultimo nome é {nomeseparado[-1]}")