#Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
# O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de 
# gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, 
# incluindo o total de gols feitos durante o campeonato.

dados = {}
gols_jogo = []
cont = 0
total_gols = 0
dados["nome"] = str(input("NOME: "))
jogos = int(input("PARTIDAS JOGADAS: "))
while cont < jogos:
    gols = int(input(f"Quantos gols no {cont+1}º"))
    gols_jogo.append(gols)
    cont += 1

dados["gols"] = gols_jogo[:]
for g in gols_jogo:
    total_gols += g    
dados["total"] = total_gols 
print("-="*30)
print(dados)  
print("-="*30)
for k,v in dados.items():
    print(f"{k} tem o valor {v}")
print("-="*30)      


for i, g in enumerate(gols_jogo):
    print(f"No {i+1}º jogo, {dados["nome"]} fez {g} gols.")
print(f"No total {dados['nome']} fez {dados['total']} gols.")