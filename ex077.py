palavras = ('APRENDER', 'PROGRAMAR','LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS',
             'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for c in range(len(palavras)):
    print(f'Na palavra: {palavras[c]} temos: ', end='')
    if 'A' in palavras[c]:
        print('a', end=' ')
    if 'E' in palavras[c]:
        print('e', end=' ')
    if 'I' in palavras[c]:
        print('i', end=' ')
    if 'O' in palavras[c]:
        print('o', end=' ')
    if 'U' in palavras[c]:
        print('u', end=' ')
    print('')