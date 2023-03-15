# Есть список песен группы Depeche Mode со временем звучания с точностью до долей минут

violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

# Распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате
#   Три песни звучат ХХХ.XX минут
# Точность указывается в функции round(a, b)
# где a, это число которое надо округлить, а b количество знаков после запятой
# более подробно про функцию round смотрите в документации https://docs.python.org/3/search.html?q=round
Time3 = 0
for song, time in violator_songs:
    if song in ('Halo','Enjoy the Silence','Clean'):
        Time3 += time
Time3 = round(Time3,2)
print(f'Три песни звучат {Time3} минут')
# Есть словарь песен группы Yellow со временем звучания с точностью до долей минут
pocket_universe_songs = {
    'Solar Driftwood': 1.85,
    'Celsius': 5.98,
    'More': 6.65,
    'On Track': 5.55,
    'Monolith': 6.35,
    'To the Sea': 5.77,
    'Magnetic': 5.88,
    'Liquid Mountain': 2.97,
    'Pan Blue': 5.52,
    'Resistor': 7.22,
    'Beyond Mirrors': 5.82,
}
# Распечатайте общее время звучания трех песен: 'On Track', 'To the Sea' и 'Beyond Mirrors'
# А другие три песни звучат приблизительно ХХХ минут
TimeOther, Time3, CountOther = 0, 0, 0
for song, time in pocket_universe_songs.items():
    if song in ('On Track','To the Sea','Beyond Mirrors'):
        Time3 += time
    else:
        TimeOther += time
        CountOther += 1
Time3 = round(Time3,2)
TimeOther = round(TimeOther / CountOther * 3, 2)
print(f'Три песни звучат {Time3} минут')
print(f'А другие три песни звучат приблизительно {TimeOther} минут')
# Обратите внимание, что делать много вычислений внутри print() - плохой стиль.
# Лучше заранее вычислить необходимое, а затем в print(xxx, yyy, zzz)
