# Aula String
# Este programa indica se uma dada cidade começa com a palavra 'Santo'
# Autor: Eduardo Knop

print('\n\n*-* Este programa informa se uma dada cidade começa com a palavra Santo *-*\n\n')

city = input('Digite o nome de uma cidade: ')
city = city.strip()
city = city.lower().split()
print('\nA cidade informada começa com Santo? {}'.format('santo' in city))
