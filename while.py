#57
#sexo = str(input('Digite seu sexo[M ou F]: ')).strip().upper()[0]

#while sexo not in 'MF':
#    sexo = str(input('Dado inválido. Digite novamente: ')).strip().upper()
#print(f'Sexo {sexo} registrado com sucesso!')    


#58

#import random

#num_random = random.randint(0, 10)
#tentativas = 0
#acertou = False
#while not acertou:
#    num = int(input('Digite um numero de 0 a 10: '))
#    tentativas += 1
#    if num == num_random:
#        print(f'Acertou!')
#        acertou = True
#    else:
#        if num < num_random:
#            print('Mais...')
#        else:
#            print('Menos...')    
#print(f'Acertou em {tentativas} tentativas.')               

    
#59

#num1 = int(input('Digite o primeiro número:'))
#num2 = int(input('Digite o segundo número: '))
#escolha = 0
#while escolha != 5:
#    escolha = int(input('[1]soma\n[2]sub\n[3]mult\n[4]div\n[5]sair'))
#    if escolha == 1:
#        print(f'Resultado da soma = {num1 + num2}')
        
#    elif escolha == 2:
#        print(f'Resultado da subtração = {num1-num2}')
#        
#    elif escolha == 3:
#        print(f'Resultado da mult = {num1*num2}')
        
#    elif escolha == 4:
#        print(f'Resultado da div = {num1/num2}')
        
#    elif escolha == 5:
#        break

#    else:
#        escolha = int(input('Escolha invalida, digite novamente: '))        


#60 

#n = int(input('Digite um número'))
#fatorial = 1
#c = n
#while c > 0:
#    print(c, end = '')
#    print('x' if c > 1 else ' = ', end ='')
#    fatorial *= c
#    c -= 1
    
#print(fatorial)    


# 61 e 62
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
c = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print(f'{termo} > ', end='')
        termo += razao
        c += 1
    print('Pausa')
    mais = int(input('Deseja mais quantos termos? 0 para sair: '))
print(f'Finalizado com {total} termos mostrados.')