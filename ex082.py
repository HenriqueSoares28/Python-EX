lista_a = []
lista_b = []
lista_c = []
while True:
    lista_a.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
for n in lista_a:
    if n % 2 == 0:
        lista_b.append(n)
    else:
        lista_c.append(n)
print('=-'*30)
print(f'A lista completa é: {lista_a}')
print(f'A lista de pares é: {lista_b}')
print(f'A lista de ímpares é: {lista_c }')