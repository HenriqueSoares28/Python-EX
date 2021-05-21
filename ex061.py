term = int(input('Primeiro termo: '))
r = int(input('Razão: '))
fim = False
num = term
num2 = -1
while not fim:
    if num == 8*r + term:
        fim = True
    else:
        num2 += 1
        num = term + (num2*r)
        print('{} '.format(num), end='-> ')
print('Acabou')