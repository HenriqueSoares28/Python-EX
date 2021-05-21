itens = ('Lápis', 'Borracha', 'Caderno', 'Estojo', 'Transferidor', 'Compasso', 'Mochila', 'Canetas', 'Livros')
preços = (1.75, 2.00, 15.90, 20.00, 4.20, 9.99, 120.32, 22.30, 34.90)
print('-'*40)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('-'*40)
for c in range(0,len(itens)):
    print(f'{itens[c]:.<30}', f'R${preços[c]:>7.2f}')

print('-'*40)