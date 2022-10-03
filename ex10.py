words_dict = {}
common_dict = {}

# Get file`s name, 'Book.txt' by default
nfile = input('Enter File: ')
if nfile.count('.') < 1:
    nfile += '.txt'

# Opens the file
try:
    file = open(nfile)
except FileNotFoundError:
    print('File Not Found: {}'.format(nfile))
    quit()
except Exception:
    print('Sorry, an Error occurried! Try again.')
    quit()

# Reads each word of the file and makes a histogram
for line in file:
    if len(line) < 2:
        continue

    words = line.lower().strip().split()
    for word in words:
        if word.isalpha() == False:
            for letter in word:
                if letter.isalpha() == False:
                    word = word.replace(letter, '')
        
        if len(word) > 0:
            words_dict[word] = words_dict.get(word, 0) + 1

# Lambda to sort things in dicts by value
common_dict = sorted([(v, k) for k, v in words_dict.items()], reverse=True)

print('The most common Words are: ')
for v, k in common_dict[:10]:
    print('Word "{}" appears {} times'.format(k, v))
