l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
area = l*a
tinta = area/2
print('Sua parede tem a dimenção de {} x {} e sua area é de {}m².'.format(l,a,area))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))