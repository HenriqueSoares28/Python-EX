def leiaInt():
    while True:
        try:
            i = int(input('Digite um Inteirto: '))
        except:
            print('ERRO: por favor, digite um número inteiro válido.')
        else:
            return i
        


i = leiaInt()

while True:
    try:
        r = float(input('Digite um número real: '))
    except:
        print('Erro: por favor digite um número real.')
        continue
    else:
        break
print(f'O valor inteiro foi {i} e o real foi {r}')