from time import sleep 


def contagem(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i < f:
        for j in range(i, f + 1, p):
            print(j, end=' ')
            sleep(0.15)
    else:
        for j in range(i, f - 1, -p):
            print(j, end=' ')
            sleep(0.15)
    print('FIM!')
    print('=-'*15)


#main

print('=-'*15)

contagem(1, 10, 1)
contagem(10, 0, 2)

print('Agora é a sua vez de personalizar a contafgem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contagem(ini, fim, pas)