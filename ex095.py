golsc = list()
jogador = dict()
jogadores = list()
while True:
    golsc.clear()
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for p in range(partidas):
        golsc.append(int(input(f'Quantos gols na partida {p + 1}? ')))
    jogador['gols'] = golsc[:]
    jogador['total'] = sum(golsc)
    jogadores.append(jogador.copy())
    while True:
        cont = str(input('Quer continuar? [S/N] '))
        if cont in 'NnSs':
            break
        else:
            print('ERRO! Responda apenas com S ou N.')
    if cont in ('Nn'):
        break
print('=-'*30)
print(f'{"cod name":19}{"gols":15}{"total":6}')
print('-'*40)
for c in range(len(jogadores)):
    print(f"{c:>3} {jogadores[c]['nome']:15}{str(jogadores[c]['gols']):15}{jogadores[c]['total']:5}")
print('-'*40)
while True:
    j = int(input('Mostrar dados de qual jogador? (999 pra parar) '))
    if j == 999:
        break
    print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[j]["nome"]}')
    for g in range(len(jogadores[j]['gols'])):
        print(f'    No jogo {g} fez {jogadores[j]["gols"][g]}')
print('-'*40)
