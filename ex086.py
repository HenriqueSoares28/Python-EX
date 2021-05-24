matriz = [[],[],[]]
for p in range(0,3):
    for c in range(0,3):
        valor = (int(input(f'Digite um valor para [{p}, {c}]: ')))
        matriz[p].append(valor)
print('-='*30)
for p in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[p][c]: ^5}]', end='')
    print()