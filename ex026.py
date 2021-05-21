fra = str(input('Digite uma frase: ')).strip().lower()
print ('A letra A apareceu {} vezes na frase'.format(fra.count('a')))
print ('A prmeira letra A apareceu na posição {}'.format(fra.find('a')+1))
print ('A ultima letra A apareceu na posição {}'.format(fra.rfind('a')+1))