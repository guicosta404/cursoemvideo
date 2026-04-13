# teste = list()
# teste.append("Gustavo")
# teste.append(40)
# galera = list()
# galera.append(teste[:])
# teste[0] = "Maria"
# teste[1] = 22
# galera.append(teste[:])
# print(galera)


# galera = [['Joao', 19], ['Ana', 33], ['Joaquim', 13],['Maria', 45]]
# # print(galera[2][1])
# for pessoa in galera:
#     print(f"{pessoa[0]} tem {pessoa[1]} anos de idade.")


# galera = []
# dado = []
# maior = 0
# menor = 0
# for c in range(0,3):
#     dado.append(str(input("Nome: ")))
#     dado.append(int(input("Idade: ")))
#     galera.append(dado[:])
#     dado.clear()
# print(galera)

# for pessoa in galera:
#     if pessoa[1] >= 21:
#         print(f"{pessoa[0]} é maior de idade")
#         maior += 1
#     else:
#         print(f"{pessoa[0]} é menor de idade")    
#         menor +=1
# print(f"Temos {maior} de idade e {menor} menores.")



# 84

# lista = list()
# dados = list()
# maior = 0
# menor = 0

# while True:
#     dados.append(str(input("Digite seu nome: ")))
#     dados.append(float(input("Digite seu peso: ")))
#     if len(lista) == 0:
#         maior = menor = dados[1]
#     else:
#         if maior < dados[1]:
#             maior = dados[1]
#         if menor > dados[1]:
#             menor = dados[1]        
#     lista.append(dados[:])
#     dados.clear()
#     sair = str(input("Deseja registrar outro? (s/n) ".lower()))
#     if 'n' in sair:
#         break

# print(f"Ao total foram cadastradas {len(lista)} pessoas.")    
# print(f"O maior peso foi {maior} de ", end='')
# for p in lista:
#     if p[1] == maior:
#         print(f'[{p[0]}] ', end=' ')
# print(f'\nO menor peso foi {menor} de', end='')
# for p in lista:
#     if p[1] == menor:
#         print(f"[{p[0]}] ", end='')

# 85

# valores = [[], []]
# valor = 0

# for c in range(0,8):
#     valor = int(input("Digite um valor: "))
#     if valor % 2 == 0:
#         valores[0].append(valor)
#     else:
#         valores[1].append(valor)    

# valores[0].sort()
# valores[1].sort()
# print(f"Os valores pares foram {valores[0]}")
# print(f"Os valores ímpares foram {valores[1]}")
# print(valores[0])   


#86

# matriz = [[0,0,0], [0,0,0], [0,0,0]]

# for linha in range(0,3):
#     for coluna in range(0,3):
#         matriz[linha][coluna] = int(input(f'Digite um valor para {linha}, {coluna}: '))
# for linha in range(0,3):
#     for coluna in range(0,3):
#         print(f'[{matriz[linha][coluna]}]', end='')
#     print()    
    


