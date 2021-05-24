from random import sample
from time import sleep
jogos = list()
print('-'*30)
print(f'{" SORTEANDO JOGOS ":-^30}')
print('-'*30)
num_jogos = int(input('Quantos jogos você quer sortear? '))
print('{:-^30}'.format(' SORTEANDO JOGOS '))
for c in range(num_jogos):
    a = sorted(sample(range(1,61),6))
    jogos.append(a[:])
    print(f'Jogo {c+1}: {jogos}')
    jogos.clear()
    sleep(0.5)
print(f'{" BOA SORTE! ":-^30}')