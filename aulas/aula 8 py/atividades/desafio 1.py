# DESAFIO 01

# Crie um programa que tenha uma tupla totalmente preenchida com
# uma contagem por extenso, de zero até vinte.

# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e
# mostra-lo por extenso.
extenso=('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dezeseis','dezessete','dezoito','dezenove','vinte')
num=int(input("escolha um numero de 0 a 20: "))
print(f"o {num} por extenso é: {extenso[num]}")