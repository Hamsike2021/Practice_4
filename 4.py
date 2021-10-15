start = int(input('Старотовое количество организмов: '))
pr = int(input('Среднесуточное увеличение в процентах: '))
days = int(input('Количество дней для увеличения: '))
print('День\tПопуляция')
for i in range(1, days + 1):
  print('{0}\t{1}'.format(i, start))
  start = round(start * (1 + pr / 100), 2)
