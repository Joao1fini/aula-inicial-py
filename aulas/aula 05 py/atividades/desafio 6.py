# DESAFIO 06

# Crie um programa que faça o computador jogar Jokenpô com
# você:

import random
import time
vez=1
ven=0
per=0
empa=0
while True:
    usuario=str(input("escolha pedra,papel ou tesoura: "))
    usuario=usuario.upper()
    opcoes=["PEDRA","PAPEL","TESOURA"]
    sorte=[random.randint(0,2)]
    pc=opcoes[random.randint(0,2)]
    if pc==usuario:
        print(f"o computador escolheu {pc} então seja")
        print("EMPATE")
        empa+=1
    elif pc!=usuario and usuario=="PEDRA" or usuario=="PAPEL" or usuario==("TESOURA"):
        if (pc=="PEDRA" and usuario=="TESOURA")or(pc=="PAPEL" and usuario=="PEDRA")or(pc=="TESOURA" and usuario=="PAPEL"):
            print(f"o computador escolheu {pc} ou ")
            print("****voce perdeu****")
            per+=1
        else:
            print(f"o computador escolheu {pc} ou ")
            print("*****voce venceu****")
            ven+=1
    else:
        print("ERROR: ESCOLHA UMAS DAS OPÇOES SUGERIDAS")
    resposta=input("deseja sair? (s/n): ")
    if resposta.lower()=="s":
        print("Saindo.")
        time.sleep(0.6)
        print("Saindo..")
        time.sleep(0.6)
        print("Saindo...")
        time.sleep(0.8)
        print(f"voce jogou {vez} vezes")
        print(f"venceu {ven} partidas")
        print(f"perdeu {per} partidas")
        print(f"empatou {empa} partidas")
        input()
        break
    else:
        vez+=1
        print("continuando")
        
    
        
#         import random

# usuario=str(input("escolha PEDRA,papel ou tesoura:  "))
# pc=random.randint(0,3)
# usuario=usuario.lower()
# if usuario=="pedra":
#     usuario==1
# elif usuario=="papel":
#     usuario==2
# elif usuario=="tesoura":
#     usuario==3
# if pc==usuario:
#     print("EMPATE")
# else:
#     if (pc==1 and usuario==3)or(pc==2 and usuario==1)or(pc==3 and usuario==2):
#         print("voce perdeu")
#     elif (usuario==1 and pc==3)or(pc==1 and usuario==2)or(pc==2 and usuario==3):
#         print("voce venceu")