#Faça um programa que leia nome e média de um aluno, guardando também a 
# situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

situacao = {
    "nome" : "",
    "media" : 0.0,
    "situacao" : ""
}

situacao["nome"] = str(input("Digite o nome do aluno: "))
situacao["media"] = float(input("Digite a média do aluno: "))
if situacao["media"] >= 6.0:
    situacao["situacao"] = "APROVADO"
else:
    situacao["situacao"] = "REPROVADO"    
for k,v in situacao.items():
    print(f"{k} é igual a {v}.")

