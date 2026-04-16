#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
#Guarde esses resultados em um dicionário em Python. No final,
#  coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter
jogadores = {
    "jogador1" : randint(1,6),
    "jogador2" : randint(1,6),
    "jogador3" : randint(1,6),
    "jogador4" : randint(1,6)

}
# jogadores = {
#     "jogador1": 0,
#     "jogador2": 0,
#     "jogador3": 0,
#     "jogador4" : 0
# }
# random = []

# for c in range(0,5):
#     random.append(randint(1,6))
# print(random)

# jogadores["jogador1"] = random[0]
# jogadores["jogador2"] = random[1]
# jogadores["jogador3"] = random[2]
# jogadores["jogador4"] = random[3]

for k,v in jogadores.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)

# Coloca um dict em ordem, transformado para lista.    
jogadores_em_ordem = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

print('='*5, 'RANKING', '=*5')
for i, v in enumerate(jogadores_em_ordem):
    print(f'{i+1}º lugar: {v[0]} com {v[1]} pontos.')