# DESAFIO 04

# Faça um programa que jogue par ou impar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitorias consecutivas que ele conquistou
# no final do jogo.
import random
import time
vitorias=0
while True:
    jogador=input("escola par ou impar: ")
    if jogador=="par" or jogador=="impar":
        numero=int(input("escolha um numero d 1 a 10: "))
        if numero<=10 and numero>=0:
            pc=random.randint(1,10)
            par=(numero+pc)%2==0
            time.sleep(1)
            print(f"O computador escolheu {pc}")
            time.sleep(1)
            if jogador=="impar":
                if (numero+pc)!=par:
                    print("Você ganhou")
                    vitorias+=1
                else:
                    print("você perdeu")
                    break
            elif jogador=="par":
                if par==True:
                    print("Você ganhou")
                    vitorias+=1
                else:
                    print("você perdeu")
                    break
            else:
                print("error")
        else:
            print("o numero tem que ser de 1 a 10. ")
            continue
time.sleep(1)
print("calculando.")
time.sleep(1)
print("calculando..") 
time.sleep(1)
print("calculando...")  
if vitorias>0:
    if vitorias>1:
        print(f"você venceu um total de {vitorias} vitorias consecutivas")
    else:
        print(f"você venceu {vitorias} partida")
elif vitorias==0:
    print(f"você nao venceu nenhuma partida")
input()