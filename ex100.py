from random import choice

def sortear(nuns):
    """
    ->sla
    """
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        sorteados = choice(nuns)
        print(f'{sorteados} ', end='')
        valoresSorteados.append(sorteados)
    print('PRONTO!')


def somarPar(val):
    valoresPares = list()
    for v in val:
        if v % 2 == 0:
            valoresPares.append(v)
    print(f'Somando os valores pares de {val}, temos {sum(valoresPares)}')


#main
valoresSorteados = list()
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9,]

sortear(valores)
somarPar(valoresSorteados)
