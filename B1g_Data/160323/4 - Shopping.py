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
        {'ашан': 10.99},
        {'пятерочка': 9.99},
        {'магнит': 11.99},
    ],
    'конфеты': [
        {'ашан': 34.99},
        {'пятерочка': 32.99},
        {'магнит': 30.99}
    ],
    'карамель': [
        {'ашан': 45.99},
        {'пятерочка': 46.99},
        {'магнит': 41.99}
    ],
    'пирожные': [
        {'ашан': 67.99},
        {'пятерочка': 59.99},
        {'магнит': 62.99}
    ]
}
# Указать надо только по 2 магазина с минимальными ценами
ash_price = shops['ашан'][0]['price'] + shops['ашан'][1]['price'] + shops['ашан'][2]['price'] + shops['ашан'][3]['price']
pyat_price = shops['пятерочка'][0]['price'] + shops['пятерочка'][1]['price'] + shops['пятерочка'][2]['price'] + shops['пятерочка'][3]['price']
mag_price = shops['магнит'][0]['price'] + shops['магнит'][1]['price'] + shops['магнит'][2]['price'] + shops['магнит'][3]['price']
shop_prices = {
    'Ашан': ash_price,
    'Пятерочка': pyat_price,
    'Магнит': mag_price
}
max_price = max(shop_prices)
shop_prices.pop(max_price)
print(*shop_prices.keys())
