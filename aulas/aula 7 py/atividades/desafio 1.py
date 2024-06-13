import random
palpites=0
vidas=10
while True:
    n1=int(input("escolha um numero: "))
    pc=random.randint(0,10)
    if vidas>0:
        if n1==pc:
            print("****você venceu****")
            print(f"voce preciscou de apenas {palpites} tentativas")
            input()
            break
        else:
            print("errou")
            palpites+=1
            vidas-=1
    else:
        print(f"voce tentou perdeu suas vidas, voce deu {palpites} palpites")
        input()
        break