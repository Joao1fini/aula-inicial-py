# DESAFIO 05

# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso
# de mostrar que tipo de triângulo será formado:

# Equilátero: Todos os lados iguais
# Isósceles: Dois lados iguais
# Escaleno: Todos os lados diferentes

linha1=float(input("digite o tamanho da primeira linha: "))
linha2=float(input("digite o tamanho da segunda linha: "))
linha3=float(input("digite o tamanho da terceira linha: "))
Equilatero=linha1==linha2==linha3
isosceles=(linha1==linha2!=linha3) or (linha1==linha3!=linha2) or (linha2==linha3!=linha1)
escaleno=linha1!=linha2!=linha3
if escaleno==True:
    print(f"o triangulo é escaleno")
elif Equilatero==True:
    print(f"o triangulo é equilatero")
else:
    print(f"o triangulo é isosceles")
