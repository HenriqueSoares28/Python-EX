from random import randint
from time import sleep
from operator import itemgetter
cont = 0
jogadores = {
            'jogador1': randint(1,6),
            'jogador2': randint(1,6),
            'jogador3': randint(1,6),
            'jogador4': randint(1,6)}

# Colocando em ordem          
ranking = dict()
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

# Enviando resultados
print('=-'*30)
print(f'{"== RANKING DOS JOGADORES ==":^40}')
for k, v in enumerate(ranking):
    cont += 1
    print(f'{k+1}° lugar: {v[0]} tirou {v[1]} no dado!')
    sleep(1)
    
