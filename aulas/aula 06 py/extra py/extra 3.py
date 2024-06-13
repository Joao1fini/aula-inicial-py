qnt_analisadas=int(input("quantas pessoas deseja analisar? "))
soma=0
for i in range(1,qnt_analisadas+1):
    temperatura=float(input(f"digite a temperatura: "))
    print(f"paciente: {i}")
    if temperatura<=37.2:
        print("estado normal")
    elif temperatura>37.3 and temperatura<38:
        print("estado febril")
    elif temperatura==38 and temperatura<39:
        print("com febre")
    else:
        print("FEBRE ALTA")
    soma=soma+temperatura
media= soma/qnt_analisadas
print(f"temperatura media {media}°C calculo feito com {qnt_analisadas} de pessoas")