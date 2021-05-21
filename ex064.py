num = int(input('Digite um número [999 para parar]: '))
parar = False
contagem = 0 
resultado = num
while not parar:
    if num == 999:
        parar = True
    else:
        num = int(input('Digite um número [999 para parar]: '))
        resultado += num
        contagem += 1
print('Você digitou {} números e a soma entre eles foi de  {}.'.format(contagem - 1, resultado - 999))
