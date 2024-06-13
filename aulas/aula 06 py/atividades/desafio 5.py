# DESAFIO 05

# Desenvolva um programa que leia seis números inteiros e
# mostre a soma apenas daqueles que forem pares. Se o valor
# digitado for impar desconsidere-o.
soma=0
for i in range(1,7):
    if i%2==0:
        print("esse é par")
        soma=soma+i
    else:
        print("esse é impar")
print(f"a soma de todos {soma}")
