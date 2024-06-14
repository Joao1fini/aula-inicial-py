# DESAFIO 03

# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
# do Campeonato Brasileiro Serie B de Futebol, na ordem de
# colocação. Depois mostre:

# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time do Santos.

import random
import time

tupla=("AMÉRICA-MG",'Goiás','Mirassol','Avaí','Santos','Sport','Ceará','Operário-PR','Coritiba','Vila Nova'
,'Novorizontino','Chapecoense','Amazonas','Ponte Preta','CRB','Paysandu','Botafogo','Ituano','Brusque','Guarani')
n=0
print(f"os 20 primeiros colocados do campeonato brasileiro serie B")
for i in range(1,21):
    print(f"{i}° {tupla[n]}")
    n+=1
print()
time.sleep(0.6)
print("vendo os primeiros e ultimos colocados.")
time.sleep(0.6)
print("vendo os primeiros e ultimos colocados..")
time.sleep(0.8)
print("vendo os primeiros e ultimos colocados...")
n1=14
for a in range(0,5):
    print(f"os cinco primeiros colocados °{1+a} {tupla[a]}")
    time.sleep(0.5)
time.sleep(1.5)
print()
print("*****tabela ultimos colocados*****")
for e in range(0,5):
    n1+=1
    time.sleep(0.7)
    print(f"os ultimos 5 colocados {tupla[n1]}")
posicao=tupla.index("Santos")
print(f"a posição do santos na tabela é {posicao+1} lugar")
print()
print(f"a seguencia alfabetica {sorted(tupla)}")



        
# tabelaBrasileirao = ('Palmeiras', 'Grêmio','Atletico - MG', 'Flamengo', 'Botafogo' ,\
#                      'Bragantino', 'Fluminense', 'Atletico - PR', 'Internacional', 'Fortaleza')


