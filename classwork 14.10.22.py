# Classwork 14.10.22
'''print('Hello, world!')
a=input("Enter some shit")) # Сохраняется как str
print(a)
print(type(a)) # Ввод типа переменной a
'''
'''the_spisok=[123, "123"] # Создание списка (массива данных разных типов)
print(the_spisok) # >>> [123, "123"]
print(the_spisok[1]) # >>> '123' / Индекс начинается с 0

the_spisok.append(321) # Добавление элемента в список
print(the_spisok) # >>> [123, '123', 321]
print(the_spisok[1:2]) # >>> ['123']
                       # Т.к область определения [a; b)
print(the_spisok[2:0:-1]) # >>> [321, '123']
                          # Т.к область оперделения [c; a)
'''
the_slovar = {0: "The zero",
              1: "Sweet home alabama",
              2: "Paint it black"}
print(the_slovar)
print(the_slovar[2])
the_2nd_slovar={"City": "Zelenograd",
                "District": 14,
                "Building": 1435}
print(the_2nd_slovar)
print(the_2nd_slovar["District"]) # >>> 14
the_3rd_slovar={45: "The forty-five",
                "Five": "V"}
print(the_3rd_slovar[45])
print(the_3rd_slovar["Five"])
