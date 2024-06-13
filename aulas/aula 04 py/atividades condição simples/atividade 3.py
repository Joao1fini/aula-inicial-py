# DESAFIO 03

# Desenvolva um programa que pergunte a distância de uma
# viagem em Km. Calcule o preço da passagem cobrando R$
# 0,50 por Km para viagens de até 200 Km e R$ 0,45 para
# viagens mais longas.
viagem=float(input("quantos km você pretende viajar? "))
if viagem<=200:
    passagem=viagem*0.50
    print(f"o total da passagem é {passagem}")
else:
    passagem=viagem*0.45
    print(f"o total da passagem é {passagem}")