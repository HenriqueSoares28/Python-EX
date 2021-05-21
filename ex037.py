num = int(input('Digite um número: '))
print('''Escolha uma das bases de conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converte para HEXADECIMAL''')
opção = int(input('Digite sua opção: '))
if opção == 1:
    print('A conversão de {} para BÍNARIO é {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('A conversão de {} para OCTAL é {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('A convesão de {} para HEXADECIMAL é {}'.format(num,hex(num)[2:]))
else:
    print('Opção invalida. Tente novamente.')