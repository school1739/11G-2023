'''
Entering coefficients of equation: А В и С
Coefficients - int
'''
def calculateDiscriminant(a, b, c):
  '''
  Calculates the discriminant of the equation
  Using formula D = b^2 - 4ac
  
  Input:
  a - int
  b - int
  c - int

  Output:
  descriminant 
  '''
  return b ** 2 - 4 * a * c

def squareRoot(d, a, b):
  '''
  Finding square roots of the equation
  Input:
  d - discriminant
  a - coefficient of x^2
  b - coefficient of x

  Output:
  Roots of equation or 'No roots'
  '''

  '''
  Checking if equation has roots
  '''
  if d < 0:
    print('No roots')
  else:
    return[(f'Корень 1: {(-b + d ** 0.5)/(2 * a)}'), 
 (f'Корень 2: {(-b - d ** 0.5)/(2 * a)}')]

a = int(input('Введите A'))
b = int(input('Введите B'))
c = int(input('Введите C'))

print(squareRoot(calculateDiscriminant(a, b, c), a, b))


