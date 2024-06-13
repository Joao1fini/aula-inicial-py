# DESAFIO 01

# Escreva um programa que faça o computador “pensar” em um
# número inteiro entre 5 e 0 e peça para o usuário tentar descobrir
# qual foi o número escolhido pelo computador.

# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

print("*******ADIVINHE O NUMERO UOUUUUU*******")
numerousuario=int(input("digite um numero entre 0 e 5: "))

numerocomputador = random.randint(0,5)
print(f"numero escolhido pelo computador {numerocomputador}")

if numerousuario==numerocomputador:
    print("voce venceu um robo PARABENS")
else:
    print("voce perdeu seu BURRO")
