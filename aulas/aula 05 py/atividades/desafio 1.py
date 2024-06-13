# DESAFIO 01

# Escreva um programa para aprovar um empréstimo bancário
# para a compra de uma casa. O programa vai perguntar o valor
# da casa, o salário do comprador e em quantos anos ele vai
# pagar.

# Calcule o valor da prestação mensal, sabendo que ela não pode
# exceder 30% do salário ou então o empréstimo será negado.

valor_casa=float(input("digite o valor da casa: "))
salario=float(input("qual o seu salario? "))
limite=salario*0.3
print(f"o valor mensal da sua parcela tem o limite de {limite}")
anos_pagar=int(input("digite em quantos anos voce quer pagar: "))
meses=anos_pagar*12
prestacao=valor_casa/meses
if limite>prestacao:
    print(f"o valor da prestaçã é: {prestacao} por mês")
else:
    print("o valor da prestação excede o limite permitido pelo seu salario")