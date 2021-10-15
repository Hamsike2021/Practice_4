s = int(input('Какая скорсоть транспортного средства в км/ч? '))
t = int(input('Сколько часов оно двигалось? '))
f1 = [[str(i), str(s * i)] for i in range(1, t + 1)]
print(f'Час\tПройденное расстояние')
print('-' * len(f'Час\tПройденное расстояние') + '----')
for el in f1:
  print('\t'.join(el))
