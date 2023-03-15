
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
# или проще /сложнее ?
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

# TODO здесь ваш код
stol_cost = store[goods['Стол']][0]['quantity'] * store[goods['Стол']][0]['price']
stol_code = goods['Стол']
stol_item = store[stol_code][0]
stol_quantity = stol_item['quantity']
stol_price = stol_item['price']
stol_cost = stol_quantity * stol_price

print('Стол -', stol_quantity, 'шт, стоимость', stol_cost, 'руб')


styl_cost = store[goods['Стул']][0]['quantity'] * store[goods['Стул']][0]['price']
styl_code = goods['Стул']
styl_item = store[styl_code][0]
styl_quantity = styl_item['quantity']
styl_price = styl_item['price']
styl_cost = styl_quantity * styl_price

print('Стул -', styl_quantity, 'шт, стоимость', styl_cost, 'руб')


divan_cost = store[goods['Диван']][0]['quantity'] * store[goods['Диван']][0]['price']
divan_code = goods['Стол']
divan_item = store[divan_code][0]
divan_quantity = divan_item['quantity']
divan_price = divan_item['price']
divan_cost = divan_quantity * divan_price

print('Диван -', divan_quantity, 'шт, стоимость', divan_cost, 'руб')
