def leiaInt(num):
    while True:
        resp = str(input(f'{num}')).strip()
        if resp.isnumeric():
            resp = int(resp)
            return resp
        else:
            print('ERROR! Digite um número valido')
                

#main
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')