# 5. Crie um programa que dados o valor, a taxa e o tempo, efetuar o cálculo do valor de uma prestação em atraso, utilizando a fórmula:

taxa = 30
tempo = 6
valor = 100
prestação = valor+(valor*(taxa/100)*tempo)
print (f"o valor da prestação de serviço é {prestação} reais com uma taxa diaria de {(valor*(taxa/100))/tempo} com um total de {valor*(taxa/100)}")
input()