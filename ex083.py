expre = str(input('Digite a expressão: '))
par1 = expre.count('(')
par2 = expre.count(')')
if par1 == par2:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')