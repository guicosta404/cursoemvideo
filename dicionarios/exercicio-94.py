grupo: list = []
pessoa: dict = {}
sair: str = ""
idade_total: int = 0
while True:
    pessoa["nome"] = str(input("Digite o nome: "))
    while True:
        pessoa["sexo"] = str(input("Digite o sexo (M/F): ")).lower()[0]
        if pessoa["sexo"] in "mf":
            break
        print("Inválido. Tente novamente.")
    pessoa["idade"] = int(input("Digite a idade: "))
    idade_total += pessoa["idade"]
    grupo.append(pessoa.copy())
    pessoa.clear()
    while True:
        sair = str(input("Deseja sair? (s/n)")).lower()
        if sair in 'sn':
            break
        print("Inválido. Tente novamente.")
    if "s" in sair:
        break

print(F"{len(grupo)} pessoas cadastradas.")

print(f"A idade total do grupo é {idade_total} anos.")
media = idade_total / len(grupo)
print(f"A idade média é {media}")
print("As mulheres cadastradas foram: ",end='')
for p in grupo:
    if p["sexo"] == 'f':
        print(f"[{p['nome']}] ",end='')
print()

print("Pessoas acima da média: ", end='')
for p in grupo:
    if p["idade"] > media:
        print(f"[{p['nome']}] ",end='')        