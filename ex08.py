file_name = input('Enter a file name: ')
if file_name.count('.') < 1:
    file_name = file_name + '.txt'

try:
    file = open(file_name)
except FileNotFoundError:
    print('File not found: {}'.format(file_name))
else:
    for line in file:
        print(line.upper(), end='')
