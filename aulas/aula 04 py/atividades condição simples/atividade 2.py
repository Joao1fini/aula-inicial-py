# DESAFIO 02

# Escreva um programa que leia a velocidade de um carro.

# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que
# ele foi multado.

# A multa vai custar R$ 7,00 por cada Km acima do limite.

velocidade=float(input("qual velocidade você estava pilotando em kmh? "))
if velocidade>80:
        totaldamulta=(velocidade-80)*7
        print(f"sua multa foi de {totaldamulta}$ Reais")
else:
        print("Tudo bem pode passar")
        
        