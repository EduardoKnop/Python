count_word = {}
count = None
word = None

file_name = input('Enter File: ')
if file_name.count('.') < 1:
    file_name += '.txt'

# Abre o Arquivo
try:
    file = open(file_name)
except FileNotFoundError:
    print('File not Found: {}'.format(file_name))
    quit()
for line in file:
    if len(line) < 2:
        continue
    # Conta quantidade de cada palavra
    words = line.strip().lower().split()
    for word in words:
        if word.isalpha() == False:
            for letter in word:
                if letter.isalpha() == False:
                    word = word.replace(letter, '')
        
        count_word[word] = count_word.get(word, 0) + 1

print(count_word)

# Conta a Palavra mais Comum
for k, v in count_word.items():
    if count == None or count < v:
        word = k
        count = v

print('Most common Word: {} appears {} times'.format(word, count))
