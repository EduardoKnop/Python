extra = 0.0
hours = float(input('Enter Hours: '))
rate = float(input('Enter Rate: '))
if hours > 40:
    extra = (hours - 40.0) * rate * 0.5
pay = hours * rate
pay += extra
print('Pay: R$ {:.2f}'.format(pay))
