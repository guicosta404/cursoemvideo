# Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(larg, comp):
    a = larg * comp
    print(f'Area do terreno = {a}')

l = float(input("Largura: "))
c = float(input("Comprimento"))
print('-'*20)
area(l,c)