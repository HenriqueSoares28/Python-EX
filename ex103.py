def resp(j='<desconhecido>', g=0):
    print(f'O jogador {j} fez {gols} gol(s) no campeonato.')


#main
print('='*30)
jogador = str(input('Nome do jogador: '))
gols = str(input('Número de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if jogador.strip() == '':
    resp(g=gols)
else:
    resp(jogador, gols)