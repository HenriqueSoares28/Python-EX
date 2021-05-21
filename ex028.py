import random
l = [1,2,3,4,5]
r = random.choice(l)
num = int(input('Escolha um número de 0 a 5: '))
if (num == r):
    print('Parabéns você acertou!')
else:
    print('Você errou, tente outra vez!')