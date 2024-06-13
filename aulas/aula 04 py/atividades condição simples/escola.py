
nota=int(input("qual foi sua nota: "))
faltas=int(input("quantas vezes você faltou: "))
nfaltas=100-faltas
if nota>=6 and nfaltas>70:
        print("Você esta aprovado")
elif (nota>5 and nota<6 )or(nfaltas<70 and nfaltas>60):
    print("Você esta de recuperação")
else:
    print("REPROVADO")