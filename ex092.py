from datetime import datetime
dados = dict()

dados['Nome'] = str(input('Nome: '))
ano = int(input('Ano de Nascimento: '))
dados['Idade'] = datetime.now().year - ano
dados['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano da Contratação: '))
    dados['Salário'] = float(input('Salário: '))
    dados['Aposentadoria'] = (dados['Contratação'] + 35) - ano
print('=-'*30)
for k, v in dados.items():
    print(f'- {k} tem o valor {v}')
