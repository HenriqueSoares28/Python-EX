numeros = []
numeros.append(int(input('Digite um valor: ')))
print('Adicionado ao final da lista...')
numeros.insert(0, (int(input('Digite um valor: '))))
print('Adicionado ma posição 0 da lista...')
numeros.insert(1,(int(input('Digite um valor: '))))
print('Adicionado ma posição 1 da lista...')
numeros.append(int(input('Digite um valor: ')))
print('Adicionado ao final da lista...')
numeros.insert(0, (int(input('Digite um valor: '))))
print('Adicionado ma posição 0 da lista...')
print('=-'*30)
for c, n in enumerate(numeros):
    if n < numeros[0]:
        numeros.insert(0, n)
    if n > numeros[-1]:
        numeros.append(n)
print(f'Os valores digitados em ordem foram {numeros}')
