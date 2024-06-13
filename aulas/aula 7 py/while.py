# x=1

# while x<10:
#     print(x)
#     x=x+1
#     # x+=1 #uma forma mais otimizada de fazer a conta
# else:
#     print("acabaste")

import time
while True:
    num=0
    while num<5:
        num+=1
        if num==3:
            print(f"vamos passar para a proxima alteração {num}")
            continue
        print(f"numero: {num}")
    print("fim do loop")
    resposta=input("deseja sair? (s/n): ")
    if resposta.lower()=="s":
        print("Saindo.")
        time.sleep(0.6)
        print("Saindo..")
        time.sleep(0.6)
        print("Saindo...")
        time.sleep(0.8)
        break
    print("continuando")