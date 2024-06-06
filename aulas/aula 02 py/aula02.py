print ("senai")

nome="Joao"

salario=1800
salariobruto=2200 #camecase
salario_bruto=2200 #snake_case

print("salario bruto =",salariobruto)
print("salario comum =",salario)
print("valor dos beneficios =",salariobruto-salario)
salario= salario+150
print("com bonus =",salario)

print("*********operadores*********")

n1=2
n2=4
soma=n1+n2
sub=n1-n2
mult=n1*n2
div=n1/n2
print("soma=",soma)
print("soma2=",str(n1+n2)) #usando o string ""str(n1+n2)"
print("subtracao=",sub)
print(f"subtracao={n1-n2}") #usando o F
print("multiplicacao",mult)
print("divisao=",div)

print("*********aritmeticos*********")
#operador de divisão inteira
divisaointeira = n1//n2
#operador de potência
potencia = n1**n2
#operador de modulo
restodadivisao= n1%n2

print("divisao inteira=",divisaointeira)
print("potencia =",potencia)
print("resto da divisao =",restodadivisao)