#Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e 
# cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, 
# o dicionário receberá também o ano de contratação e o salário. 
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date
dados: dict = {}

dados["nome"] = str(input("Digite o nome: "))
nascimento = int(input("Digite o ano de nascimento: "))
dados["idade"] = date.today().year - nascimento
dados["ctps"] = int(input("CTPS (0 se não tiver): "))
if dados["ctps"] != 0:
    dados["contratacao"] = int(input("Digite o ano de contratação: "))
    dados["salario"] = float(input("Digite o salário: "))
    dados["aposentadoria"] = dados["idade"] + ((dados["contratacao"] + 35) - date.today().year) 
for k, v in dados.items():
    print(f"  - {k} tem o valor {v}.")