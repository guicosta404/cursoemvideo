def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos não vota.'
    elif idade >=16 and idade < 18 or idade > 65:
        return f'Com {idade} anos o voto é opcional.'
    elif idade >=18 and idade <= 65:
        return f'Com {idade} anos o voto é obrigatório.'
    

nasc = int(input('Digite o ano de nascimento: '))
print(voto(nasc))
