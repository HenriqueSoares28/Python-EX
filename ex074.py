from random import randint
num = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print('Os valore sorteados foram: ', end='')
for n in num:
    print(f'{n}', end=' ')
print('')
print(f'O maior númor escolhido foi: {max(num)}')
print(f'O menor númor escolhido foi: {min(num)}')
