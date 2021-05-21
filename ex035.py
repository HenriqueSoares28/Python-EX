
print('-='*20)
print('Analisador de Triângulo')
print('-='*20)

a = float(input('Primeiro segmento do triangulo: '))
b = float(input('Segundo segmento do triangulo: '))
c = float(input('Terceiro segmento do triangulo:   '))
if a < b + c and b < a + c and c < b + a:
    print('Os segmentos escolhidos podem formar um triângulo.')
else:
    print('Os segmentos escolhidos não podem formar um triângolo.')
