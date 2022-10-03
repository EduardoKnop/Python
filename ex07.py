str = 'X-DSPAM-Confidence: 0.8475  '

n = float(str[str.find(':') + 1:].strip())
print(n)
