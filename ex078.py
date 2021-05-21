lista = []
for cont in range(0, 5):
    lista.append(int(input(f'Digite um valor para a Posição {cont}: ')))
print(f'Você digitou os valores: {lista}')
print(f'O maior valor digitado foi {max(lista)} nas posições ', end='')
for c, v in enumerate(lista):
    if v == max(lista):
        print(f'{c}... ', end='')
print(f'\nO menor valor digitado foi {min(lista)} nas posições ', end='')
for c, v in enumerate(lista):
    if v == min(lista):
        print(f'{c}... ', end='')