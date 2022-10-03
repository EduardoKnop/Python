total = 0.0
count = 0
n = None

while True:
    n = input('Enter a number: ')
    if n == 'done':
        break

    try:
        n = float(n)
    except Exception:
        print('Invalid input')
    else:
        total += n
        count += 1
try:
    average = total / count
except ZeroDivisionError:
    average = 0
print(total, count, average)
