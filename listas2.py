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
