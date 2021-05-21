from time import sleep
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*20)
    if n <= 0:
        break
    for p in range(1,11):
        print(f'{n} x {p} = {n*p}')
    print('-'*20)
    sleep(2)
    print('Digite 0 para fechar o programa.')
    print('')
print('Obrigado, até logo!')