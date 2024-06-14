# DESAFIO 02

# Crie um programa que vai gerar cinco números aleatórios e colocar
# em uma tupla.

# Depois disso, mostre a listagem de números gerados e também
# indique o menor e o maior valor que estão na Tupla.
import random
lista=[]
for i in range(5):
    i+=1
    num_aleatorio=random.randint(0,101)
    lista.append(num_aleatorio)
tupla=tuple(lista)
print(tupla)
print(f"o valor minimo da lista é {min(lista)}")
print(f"o valor maximo da lista é {max(lista)}")
