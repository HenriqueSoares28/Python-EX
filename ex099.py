from time import sleep
def analize(*num):
    print('Analizando os valores passados...')
    for v in num:
        print(v, end=' ')
        sleep(0.15)
    print(f'| Foram informados {len(num)} valores ao todo.')
    if len(num) == 0:
        print('O valor informado foi 0.')
    else:
        print(f'O maior valor informado foi {max(num)}.')
    print('='*40)
    sleep(3)


#main 
numeros = [4, 7, 0]


print('='*40)
analize(2, 9, 4, 5, 7, 1)
analize(numeros)
analize(1, 2)
analize(6)
analize()
