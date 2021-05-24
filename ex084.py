galera = []
dados = []
peso = []
pesomais = pesomenos = 0

# Recebendo dados
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    galera.append(dados[:])
    peso.append(dados[1])
    dados.clear()
    cont = str(input('Quer continuar? [S/N] '))
    if cont in 'Nn':
        break

# Saida dos dados
print('-='*30)
print(f'Ao todo você cadastrou {len(galera)} pessoas.')

# Saida maior peso
print(f'O maior peso foi de {max(peso):.2f}Kg. ', end='')
print('Peso de ', end='')
for p in galera:
    if p[1] == max(peso):
        print(f'{p[0]} ', end='')
print()

# Saida menor peso
print(f'O menor peso foi de {min(peso):.2f}Kg. ', end='')
print('Peso de ', end='')
for p in galera:
    if p[1] == min(peso):
        print(f'{p[0]} ', end='')
print()