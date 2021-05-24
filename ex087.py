matriz = [[],[],[]]
soma = soma_coluna = 0
for p in range(0,3):
    for c in range(0,3):
        valor = (int(input(f'Digite um valor para [{p}, {c}]: ')))
        matriz[p].append(valor)

# Matriz
print('-='*30)
for p in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[p][c]: ^5}]', end='')
    print()
print('-='*30)

# Soma dos pares
for c in matriz:
    for j in c:
        if j % 2 == 0:
            soma += j
print(f'A soma dos valores pares é {soma}.')

# Soma dos valores da terceira coluna
for p in range(0,3):
    soma_coluna += matriz[p][2]
print(f'A soma dos valores da terceira coluna é {soma_coluna}.')

# Maior valor da segunda linha
print(f'O maior valor da segunda coluna é {(max(matriz[1]))}.')
