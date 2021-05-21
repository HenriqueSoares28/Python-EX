term = int(input('Primeiro termo: '))
r = int(input('Razão: '))
dec = term + (10 - 1) * r
for p in range(term, dec, r):
    print('{} '.format(p), end='-> ')
print('Acabou')