def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p == 1 
    print(f'Contagem de {i} a {f} de {p} em {p}: ')    
    if i < f:
        cont = i
        while cont<= f:
            print(f'{cont} ', end='')
            cont += p
        print('Fim')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ',end='')
            cont -= p
        print('Fim')    
    
#programa principal 
contador(1,10,1)
contador(10,0, 2)
print('Personalizar contagem')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)