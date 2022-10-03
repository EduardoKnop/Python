def computepay(hours, rate):
    if hours <= 40:
        return hours * rate
    return (hours - 40) * rate * 1.5 + 40 * rate


try:
    pay = computepay(float(input('Enter Hours: ')),
    float(input('Enter Rate: R$ ')))
except Exception:
    print('Error, please enter numeric input')
    quit()
print('Pay: R$ {:.2f}'.format(pay))
