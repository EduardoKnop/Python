# Aula Condições
# Este programa te dá uma multa se passar acima de 80 km/h
# Autor: Eduardo Knop

print('\n\n*-* Este programa te dará uma multa se passar acima de 80 km/h. Cuidado!!! *-*\n\n')

v = float(input('Qual a sua velocidade atual? '))

if v <= 80:
    print('UFA!!! Você passou abaixo da velocidade máxima. {:.1f} km/h'.format(v))
else:
    print('Você tomou uma multa de R$ {:.2f} por passar a {:.1f} km/h'.format((v - 80)*7, v))
