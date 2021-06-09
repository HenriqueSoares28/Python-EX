soma = 0 
golsc = list()
dados = dict()
dados['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for p in range(partidas):
    golsc.append(int(input(f'Quantos gols na partida {p + 1}? ')))
for g in golsc:
    soma += g
dados['gols'] = golsc[:]
dados['total'] = soma
print('-='*30)
print(dados)
print('-='*30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {dados["nome"]} jogou {partidas} partidas.')
for c in range(partidas):
    print(f'    => Na partida {c + 1}, fez {golsc[c]} gols.')
print(f'Foi um total de {soma} gols.')
print('-='*30)