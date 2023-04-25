# Есть словарь магазинов с распродажами

shops = {
    'ашан':
        [
            {'name': 'печенье', 'price': 10.99},
            {'name': 'конфеты', 'price': 34.99},
            {'name': 'карамель', 'price': 45.99},
            {'name': 'пирожное', 'price': 67.99},
        ],
    'пятерочка':
        [
            {'name': 'печенье', 'price': 9.99},
            {'name': 'конфеты', 'price': 32.99},
            {'name': 'карамель', 'price': 46.99},
            {'name': 'пирожное', 'price': 59.99},
        ],
    'магнит':
        [
            {'name': 'печенье', 'price': 11.99},
            {'name': 'конфеты', 'price': 30.99},
            {'name': 'карамель', 'price': 41.99},
            {'name': 'пирожное', 'price': 62.99},
        ],
}

# Создайте словарь цен на продкты следующего вида (писать прямо в коде)
sweets = {
    'печенье': [
      {'shop': 'ашан', 'price': 10.99},
      {'shop': 'пятерочка', 'price': 9.99},
      {'магнит': 'ашан', 'price': 11.99}
    ],
  
  'конфеты': [
      {'shop': 'ашан', 'price': 34.99},
      {'shop': 'пятерочка', 'price': 32.99},
      {'магнит': 'ашан', 'price': 30.99}
    ],
  
  'карамель': [
      {'shop': 'ашан', 'price': 45.99},
      {'shop': 'пятерочка', 'price': 46.99},
      {'магнит': 'ашан', 'price': 41.99}
    ],

  'пирожное': [
      {'shop': 'ашан', 'price': 67.99},
      {'shop': 'пятерочка', 'price': 59.99},
      {'магнит': 'ашан', 'price': 62.99}
    ],
}
# Указать надо только по 2 магазина с минимальными ценами

pricesDict = {
  "Ашан": 0,
  "Пятёрочка" : 0,
  "Магнит" : 0
}

for i in range(4):
  pricesDict['Ашан'] = round(pricesDict['Ашан'] + shops['ашан'][i]['price'], 2)
  pricesDict['Пятёрочка'] = round(pricesDict['Пятёрочка'] + shops['пятерочка'][i]['price'], 2)
  pricesDict['Магнит'] = round(pricesDict['Магнит'] + shops['магнит'][i]['price'], 2)

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

# Указать надо только по 2 магазина с минимальными ценами

print("Самые дешманские магазины:")

print(f'{get_key(pricesDict, min(pricesDict.values()))} ({min(pricesDict.values())})')

pricesDict.pop(get_key(pricesDict, min(pricesDict.values())))
print(f'{get_key(pricesDict, min(pricesDict.values()))} ({min(pricesDict.values())})')