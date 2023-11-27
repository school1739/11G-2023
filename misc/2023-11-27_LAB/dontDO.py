
'''
Entering coefficients of equation: А В и С
Coefficients - int
'''
a = int(input('Введите A'))
b = int(input('Введите B'))
c = int(input('Введите C'))

d = b ** 2 - 4 * a * c # Вычисление дескриминанта 

'''
Checking if equation has roots
'''
if d < 0:
  print('No roots')
else:
  print((-b + d ** 0.5)/(2 * a))
  print((-b - d ** 0.5)/(2 * a))
