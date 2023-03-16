# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')



# Вывести стоимость каждого вида товара на складе:
# один раз распечать сколько всего столов и их общая стоимость,
# один раз распечать сколько всего стульев и их общая стоимость,
#   и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб


table_cost = store[goods['Стол']][0]['quantity'] * store[goods['Стол']][0]['price']
table_code = goods['Стол']
table_quantity = 0
table_cost = 0

for count in range(len(store[table_code])):
  table_item = store[table_code][count]
  temp_table_quantity = table_item['quantity']
  table_price = table_item['price']
  table_quantity += temp_table_quantity
  table_cost += temp_table_quantity * table_price
print('Стол -', table_quantity, 'шт, стоимость', table_cost, 'руб')



coach_cost = store[goods['Диван']][0]['quantity'] * store[goods['Диван']][0]['price']
coach_code = goods['Диван']
coach_quantity = 0
coach_cost = 0

for count in range(len(store[coach_code])):
  coach_item = store[coach_code][count]
  temp_coach_quantity = coach_item['quantity']
  coach_price = coach_item['price']
  coach_quantity += temp_coach_quantity
  coach_cost += temp_coach_quantity * coach_price
print('Диван -', coach_quantity, 'шт, стоимость', coach_cost, 'руб')




chair_cost = store[goods['Стул']][0]['quantity'] * store[goods['Стул']][0]['price']
chair_code = goods['Стул']
chair_quantity = 0
chair_cost = 0

for count in range(len(store[chair_code])):
  chair_item = store[chair_code][count]
  temp_chair_quantity = chair_item['quantity']
  chair_price = chair_item['price']
  chair_quantity += temp_chair_quantity
  chair_cost += temp_chair_quantity * chair_price
print('Стул -', chair_quantity, 'шт, стоимость', chair_cost, 'руб')
