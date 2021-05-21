numex = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
'treze', 'quatorze', 'quinze', 'desesseis', 'desessete',
'dezoito', 'dezenove', 'vinte')
num = int(input('Digite um número entre 0 e 20: '))
while True:
    if num > 20 or num < 0:
        num = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    else:
        break
print(f'Você digitou o número {numex[num]}.')