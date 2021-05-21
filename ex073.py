times = ('Flamengo', 'Internacional', 'Atlético-MG', 'São Paulo', 'Fluminense', 'Grêmio', 'Palmeiras', 'Santos', 'Athletico-PR', 'Corinthians', 'Bragantino', 'Ceará',
'Atlético-GO', 'Sport', 'Bahia', ' Fortalesa', 'Vasco', 'Goiás', 'Coritiba', 'Botafogo')
#for cont in range(0, len(times)):
print('-='*50)
print(f'Lista dos times do Brasileirão: {times}')
print('-='*50)
print(f'Os 5 primeiros times são: {times[0:5]}')
print('-='*50)
print(f'Os 4 últimos times são: {times[-4:]}')
print('-='*50)
print(f'Tmes em ordem alfabética {sorted(times)}')
print('-='*50)
print(f'O Atletico-MG está na {times.index("Atlético-MG")+ 1}° posição.')
print('-='*50)