lista = []
while True:
    valor = (int(input('Digite um valor: ')))
    if valor in lista:
        print('Valor duplicado! Não vou adicionar...')
    else:
        print('Valor adicionado com sucesso...')
        lista.append(valor)
    continuar = str(input('Quer continuar? [S/N] ').upper())
    if 'N' in continuar:
        break
print('=-'*30)
lista.sort()
print(f'Você digitou os valores {lista}')
    