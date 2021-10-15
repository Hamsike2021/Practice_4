print('Вводите положительные числа')
s = 0
while True:
  n = int(input())
  if n < 0: break
  else:
    s += n
print('Сумма: {0}'.format(s))
