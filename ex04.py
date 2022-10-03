extra = 0.0
try:
    hours = float(input('Enter Hours: '))
    rate = float(input('Enter Rate: R$ '))
except Exception:
    print('Error, please enter numeric input')
    quit()

if hours > 40:
    extra = (hours - 40) * rate
pay = hours * rate
pay += extra
print('Pay: R$ {:.2f}'.format(pay))
