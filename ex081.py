num = []
while True:
    num.append(int(input('Digite um número: ')))
    r = str(input('Deseja continuar: [S/N] ').upper())
    if 'N' in r:
        break
print('=-'*30)
print(f'Você digitou {len(num)} valores.')
num.sort(reverse = True)
print(f'A lista de valores em ordem decrescente é: {num}')
if 5 in num:
    print('O valor 5 foi digitado.')
else:
    print('O valor 5 não foi digitado.')
    
