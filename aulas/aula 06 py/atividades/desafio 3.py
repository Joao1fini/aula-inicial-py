# DESAFIO 03

# Faça um programa que calcule a soma entre todos os números
# ímpares que são múltiplos de três e que se encontram no
# intervalo de 1 até 500.

# soma=0
# n1=0
# for numero in range(1,500):
#     for n1 in range(0,11):
#         if numero==3*n1:
#             print(numero)
#             soma=soma+numero
# print(f"A soma total foi: {soma}")


# for i in range (1,501):
#     if i%2 != 0:
#         print(i) #é impar!
     
#Versão 2 completo      
soma=0  
for i in range (1,501,2):#é impar!
    if i%3 == 0: #é multiplo de 3
        # print(i)
        soma=soma+i      
print(f"Soma = {soma}")
