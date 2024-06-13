# DESAFIO 04

# A confederação Nacional de Natação precisa de uma programa
# que leia o ano de nascimento de uma atleta e mostre sua
# categoria, de acordo com a idade.

# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 24 anos: SÊNIOR
# Acima: MASTER

ano=int(input("em que ano você nasceu? "))
idade=2024-ano
if idade<=9:
    print(f"Você tem {idade} anos de idade,Você esta na classificação mirim")
elif idade<=14 and idade>9:
    print(f"Você tem {idade} anos de idade,Você esta na classificação infantil")
elif idade<=19 and idade>14:
    print(f"Você tem {idade} anos de idade,Você esta na classificação Junior")
elif idade<=24 and idade>19:
    print(f"Você tem {idade} anos de idade,Você esta na classificação Sênior")
else:
    print(f"Você tem {idade} anos de idade,Você esta na classificação MASTER")