from random import randint
def sortear(lista):
    print('Sorteando 5 números: ', end='')
    for cont in range(0,5):
        n = randint(0,10)
        lista.append(n)
        print(f'{n} ', end='')


def soma_par(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'\nSomando os valores pares de {lista} temos {soma}')        

numeros = []
sortear(numeros)
soma_par(numeros)