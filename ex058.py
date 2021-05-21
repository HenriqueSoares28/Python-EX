from random import randint
num = randint(0,10)
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que voçê consegue adivinhar qual foi?')
acertou = False
escolha = int(input('Qual será seu palpite? '))
palpites = 0

while not acertou:
    palpites += 1
    if escolha == num:
        acertou = True
    elif escolha < num:
       escolha = int(input('Mais... Tente novamente: '))
    elif escolha > num:
       escolha = int(input('Menos... Tente novamente: '))
print('Parabéns voçê acertou!!')
print('Voçê precisou de {} chances para acertar.'.format(palpites))