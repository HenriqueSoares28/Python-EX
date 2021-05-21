num = int((input('Digite um número: ')))
tot = 0
for c in range(1, num +1):
    if num % c == 0:
        print('\033[34m', end='')
        tot += 1
    else:
        print('\033[m', end='')
    print(f'{c} ', end='')
print('\033[m')
if tot == 2:
    print('O número escolhido é primo!')
else:
    print('O número escolhido não é primo!')