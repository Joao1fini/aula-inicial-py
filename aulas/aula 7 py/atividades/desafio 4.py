# DESAFIO 04

# Faça um programa que jogue par ou impar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitorias consecutivas que ele conquistou
# no final do jogo.
import random
import time
jogador=input("escola par ou impar: ")
pc=random.randint(1,10)
numero=int(input("escolha um numero d 1 a 10: "))
time.sleep(1)
print(f"O computador escolheu {pc}")
time.sleep(1)
if jogador=="impar":
    if (numero+pc)%3==0:
        print("Você ganhou")
    else:
        print("você perdeu")
elif jogador=="par":
    if (numero+pc)%2==0:
        print("Você ganhou")
    else:
        print("você perdeu")
else:
    print("error")