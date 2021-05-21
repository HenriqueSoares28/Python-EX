tot = maismil = menor = cont = 0
barato = ''
print('-'*30)
print('LOJAS SUPER BARATÃO')
print('-'*30)
while True:
    nome = str(input('Nome do produto: '))
    preço = int(input('Preço: R$ '))
    tot += preço
    cont += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = nome
    if preço > 1000:
        maismil += 1
    continuar = str(input('Quer continuar? [S/N] ').upper())
    print('')
    if continuar in 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print('O total da compra foi R${:.2f}'.format(tot))
print(f'Temos {maismil} produto custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor}')