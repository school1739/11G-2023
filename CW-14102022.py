# classwork 14.10.2022
# Ввод с клавиатуры
"""a = input("Enter some passages") # default у input - str
print(a)
print(type(a)) # Вывод типа переменной а"""
"""the_spisok = [123, "123"] # создание списка
print(the_spisok)

print(the_spisok[1]) # >>> "123" / Индекс начинается с 0

the_spisok.append(321) # Добавление элемента в список

print(the_spisok[1:2]) # >>> ["123"] т.к. область определения [a, b)

print(the_spisok[2:0:-1]) # >>> [321, "123"] т.к. область определения [0,2) [b, a)"""

the_slovar = {5: 'The Null',
              1:"Sweet home Alabama",
              2: "We need no education"}
print(the_slovar) # the slovar full

print(the_slovar[5]) # The Null
the_2nd_slovar = {"City": "Zelenograd",
                  "District": 14,
                  "Building": 1435}

print(the_2nd_slovar) # full the_2nd_slovar

print(the_2nd_slovar["District"]) # >>> 14

the_3rd_slovar = {45: "The forty-five",
                  "Five": "V"}

print(the_3rd_slovar[45]) # >>> The forty-five
print(the_3rd_slovar["Five"]) # >>> V