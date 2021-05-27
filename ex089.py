from time import sleep 
dados = [[], [], []]
aluno = 0

# Coleta de dados
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    dados[0].append(nome)
    dados[1].append(nota1)
    dados[2].append(nota2)

# Variavel de continuação
    resposta = str(input('Quer continuar? [S/N] '))
    if resposta in 'Nn':
        break

# Formatação da tabela
print('-='*14)
print(f'{"No.":<4}{"NOME":<13}{"MÉDIA":<9}')
print('-'*28)

# Dados da tabela
for c in range(len(dados[0])):
    media = ((dados[1][c]) + (dados[2][c])) / 2
    print(f'{c:<4}{dados[0][c]:<13}{media:>5.1f}')
print('-'*28)

# Seleção de aluno
while aluno != 999:
    aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if aluno < len(dados[0]):
        print(f'As notas de {dados[0][aluno]} são {dados[1][aluno]}, {dados[2][aluno]}')
    else:
        if aluno != 999:
            print('Número invalido, tente outra vez!')
            sleep(1)
    print('-'*28)

# Finalização
print('FINALIZANDO...')
sleep(0.5)
print('<<< VOLTE SEMPRE >>>')