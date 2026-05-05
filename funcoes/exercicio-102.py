def calcula_fatorial(n, show=False):
    """
    Calcula o fatorial de um número:
    n - número a ser calculado;
    show - opcional, mostrar ou não a conta
    return - o valor do fatorial do número n
    """
    fatorial = 1
    for c in range(n,0, -1):
        if show == True:
            print(c, end='')
            if c > 1:
                print(' x ', end = '')
            else:
                print(' = ', end='')    
        fatorial *= c
    return fatorial     
    
    

print(calcula_fatorial(5, show=True))    
help(calcula_fatorial)