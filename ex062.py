term = int(input('Primeiro termo: '))
r = int(input('Razão: '))
num = term
cont = 1
total = 0
mais = 10
while mais !=0:
    total = total + mais
    while cont <= total:
        print('{} -> '. format(num), end='')
        num += r
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Fim')