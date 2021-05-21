num =  int(input('Digite um número para calcular o seu fatorial: '))
multi = num 
fat = num
fim = False
while not fim:
    if multi == 1:
        fim = True
    if multi > 1:
        multi += -1
        fat = fat * multi
       
print('O calculo de {}! é: {}'.format(num, fat))