print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
numero = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
penultimo = t1
antepenultimo = t2
prox = 0
fim = 2
print('{}, {}'.format(t1, t2),end='-> ')
while fim != numero:
    prox = penultimo + antepenultimo
    penultimo = antepenultimo
    antepenultimo = prox
    print(prox, end='-> ')
    fim += 1
print('Fim')
