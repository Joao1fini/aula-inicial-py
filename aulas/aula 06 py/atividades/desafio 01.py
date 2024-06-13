# DESAFIO 01

# Faça um programa que mostre na tela uma contagem
# regressiva para o estouro de fogos de artificio, indo de 10 até 0,
# com uma pausa de 1 segundo entre eles.
import time
for tempo in range(10,-1,-1):
    print(tempo)
    time.sleep(1)
    if tempo==0:
        print("*****FOGOS*****")