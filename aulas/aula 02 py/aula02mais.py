#atribui dados digitados pleo usuario e coverte para numero inteiro
numint = int(input("digite um numero inteiro:"))
print("o numero digitado é",numint)
#atribui dados digitados pleo usuario e coverte para texto
string = str(input("escreva um texto:"))
print("voce escreveu isso:",string)
#atribui dados digitados pleo usuario e coverte para (true ou false)
booleano = bool(input("digite um valor boleano:"))
print("o valor digitado é",booleano)
#atribui dados digitados pleo usuario e coverte para numero real
numreal = float(input("digite um numero:"))
print("o valor digitado é",numreal)

#identificar o tipo de variavel

print(type(numint))
print(type(string))
print(type(booleano))
print(type(numreal))

varmisterio = 10/2<10
print(type(varmisterio))

        #*****analise da variavel*****
        
    #identificar se o valor é numerico
print(string.isnumeric())
    #identificar se o valor é string
print(string.isalpha())
    #identificar se o valor e alfanumerico
print(string.isalnum())
    #identificar se o valor tem letras maiusculas
print(string.isupper())
    #identificar se o valor tem letras minusculas
print(string.islower())
    #identificar se o valor nao tem casas decimais
print(string.isdecimal())