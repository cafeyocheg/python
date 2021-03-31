# LESSON 1

# a = 10
# b = a ** 3
# print('(10 * (10 ** 2) =', b)
# print(type(a))
# greetings = 'hello'
# print(greetings)
# print(type(greetings))
#
# time = float(input("Введите время в секундах "))
# h = int(time / 3600)
# m = int((time / 60) - (h * 60))
# s = (time - (h * 3600) - (m * 60))
# print('Время забега в секундах: {:.2f}' .format(time))
# print('чч:мм:сс {a}:{b}:{c:.0f}' .format(a=h, b=m, c=s))
#
# n = int(input("Введите целое число (n) от 1 до 10 "))
# a = (n + (n * 11) + (n * 111) + (n * 1111) + (n * 11111))
# print('сумма n+nn+nnn+nnnn+nnnnn составит',a)
# m = int(input("введите целое число (m) от 0 до 1 "))
# print('К сожалению, вы проиграли. На этом пока остановимся')
#
# n = abs(int(input("Введите любое целое положительное число ")))
# max = n % 10
# while n >= 1:
#     n = n // 10
#     if n % 10 > max:
#         max = n % 10
#     if n > 9:
#         continue
#     else:
#         print("Максимальная цифра в числе - ", max)
#         break
#
#
#    #5
# profit = float(input("Введите выручку фирмы "))
# costs = float(input("Введите издержки фирмы "))
# if profit > costs:
#     print(f"Фирма работает с прибылью. Рентабельность предприятия составляет {profit / costs:.2f}")
#     workers = int(input("Введите количество сотрудников фирмы "))
#     print(f"Прибыль в расчете на одного сотрудника составляет {profit / workers:.2f}")
# elif profit == costs:
#     print("Фирма достигла точки безубыточности. Рентабельность равна нулю.")
# else:
#     print("Фирма работает в убыток.")
#
# a = int(input("Введите результаты пробежки первого дня в км "))
# b = int(input("Введите ваш желаемый результат в км "))
# result_days = 1
# result_km = a
# while a < b:
#         a = a * 1.1
#         result_days = result_days + 1
#         result_km = result_km + (0.1 * a)
# print("Вы достигнете желаемого результата на %d день" % result_days)
#
# color = input("whats your favorite colour user? ")
# if color == "blue":
#     print("what? blue?? are you outta yr mind?")
# elif color == "red":
#     print("red? damn are you some kind of a commy?????")
# elif color == "green":
#     print("shieeeeeeeeeeeeet.......")
# else:
#     print("GODDAMN WHAT PLANET ARE YOU FROM?? VENUS? MARS? THERES "
#           "NO SUCH COLOUR ON EARTH YOU BASTARD!!!!")
#     print("i may be made of sand but i aint no dumb you hear me")
#     answer = input("c'mon try again you idiot ")
#     if answer == "i dunno":
#         print("thats better")
#     else:
#         print("WHAT?!? im outta here")
...
# LESSON 2
#1
# my_list = [22, 'yes', 90.0, None, {1, 2, 3}, 'no']
# for el in my_list:
#     print(type(el))

# 2
# el_count = int(input("Введите количество элементов списка "))
# my_list = []
# zero = 0
# elem = 0
# while el_count > zero:
#     my_list.append(input("Введите следующее значение списка "))
#     zero += 1
# my_list_ranged = range(int(len(my_list)/2))
# # print(my_list_ranged)
# for el in my_list_ranged:
#         my_list[el], my_list[el + 1] = my_list [el + 1], my_list[el]
#         el += 2
# print(my_list)

#3
# seasons_dict = {1 : 'зима', 2 : 'весна', 3 : 'лето', 4 : 'осень'}
# seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']
# month = abs(int(input('Введите месяц в виде числа от 1 до 12 ')))
# if month == 12 or month == 1 or month == 2:
#     print(seasons_dict.get(1))
#     print(seasons_list[0])
# elif month == 3 or month == 4 or month == 5:
#     print(seasons_dict.get(2))
#     print(seasons_list[1])
# elif month == 6 or month == 7 or month == 8:
#     print(seasons_dict.get(3))
#     print(seasons_list[2])
# elif month == 9 or month == 10 or month == 11:
#     print(seasons_dict.get(4))
#     print(seasons_list[3])
# else:
#     print("В году всего 12 месяцев, так что...")
# #     print("... вы проиграли")

# # 4
# my_str = input("введите набор слов без знаков препинания... ")
# words = []
# num = 1    #список начнем с 1 номера
# for el in range(my_str.count(' ') + 1):
#     words = my_str.split()
#     if len(str(words)) <= 10:
#         print(f" {num} {words [el]}")
#         num += 1
#     elif len(str(words)) > 10:
#         print(f" {num} {words [el] [:10]}")
#         num += 1

#5
# my_list = [7, 5, 3, 3, 2]
# print(f"Рейтинг: {my_list}")
# rate = int(input("Ваша оценка от 1 до 10: "))
# while rate < 11:
#     for el in range(len(my_list)):
#         if my_list[el] == rate:     #если элемент списка равен оценке, тогда оценка встанет на следующий индекс
#             my_list.insert(el + 1, rate)
#             break
#         elif my_list[0] < rate:   #если нулевой элемент списка меньше оценки, тогда оценка попадет на 0 место
#             my_list.insert(0, rate)
#         elif my_list[-1] > rate:   #если последний(-1) элемент списка больше оценки, тогда оценка просто в конце
#             my_list.append(rate)
#         elif my_list[el] > rate and my_list[el + 1] < rate:
#             my_list.insert(el + 1, rate) #если элемент списка больше оценки а следующий за ним меньше, то оценка между ними
#     print(f"Текущий список: {my_list}")
#     rate = int(input("Ваша оценка от 1 до 10  "))

#6
# sort = ['зеленый', 'пуэр', 'улун', 'белый']       #характеристика товаров 1, 2, 3, 4.
# price = [1000, 1200, 1500, 1800]
# mass = [100, 250, 500, 1000]
# quantity = [1, 2, 3, 4]
#
# my_list = (tuple1, tuple2, tuple3, tuple4)
# print(my_list)
#
# sort = (input("Выберите сорт чая "))
# price = (input("Выберите цену "))
# mass = (input("Выберите массу в граммах "))
# quantity = (input("Выберите количество, шт "))
#
# tuple1 = (1, {'сорт': 'зеленый', 'цена': 1000, 'масса, г': 250, 'количество, шт': 2})
# tuple2 = (2, {'сорт': 'пуэр', 'цена': 1800, 'масса, г': 100, 'количество, шт': 4})
# tuple3 = (3, {'сорт': 'улун', 'цена': 1500, 'масса, г': 1000, 'количество, шт': 3})
# tuple4 = (4, {'сорт': 'белый', 'цена': 1200, 'масса, г': 500, 'количество, шт': 2})
...

# LESSON 3
# #1
# def division (a, b):
#     return a / b
# a = int(input('Введите первое число '))
# b = int(input('Введите второе число '))
# try:
#     division(a, b)
# except ZeroDivisionError:
#     print('Я вам не какая-то программа, которая делит на ноль!')
# else:
#     print(division(a, b))

# #2
# def info(name, surname, year, city, email, phone):
#     data = f"Некто называющий себя {name} {surname}, если это его настоящее имя, " \
#            f"{year}ого года рождения, живёт в городе {city}, email: {email}, телефон: {phone}"
#     return data
#
# input_name = input("Имя: ")
# input_surname = input("Фамилия: ")
# input_year = input("Год рождения: ")
# input_city = input("Город: ")
# input_email = input("Электронная почта: ")
# input_phone = input("Номер телефона: ")
#
# print(info(name=input_name, surname=input_surname, year=input_year, city=input_city,
#            email=input_email, phone=input_phone))

# #3
# def my_func(a, b, c):
#     if a >= c and b >= c:
#         return a + b
#     elif b <= a and b <= c:
#         return a + c
#     else:
#         return b + c
#
# print(f'Результат - {my_func(int(input("Введите первое число: ")), int(input("Введите второе число: ")), int(input("Введите третье число: ")))}')

# #4
# def my_func1(x, y):
#     return x ** y
#
# def my_func2(x, y):
#     return pow(x, y)
#
# def my_func3(x, y):               #например x равен 4
#     result = x           #по умолчанию результат равен 4, т.е y равен 1
#     while y != 1:
#         result = result / x   #игрек допустим -2 , тогда результат равен  4/4 = 1
#         y += 1              #циклов будет 1+1+1, пока y доходит до 1, результат: 1 -> 1/4 -> 0.25/4 -> 0.0625
#     return result
#
# a = int(input("Введите действительное положительное число x: "))
# b = int(input("Введите целое отрицательное число y: "))
#
# print(f"x в степени y равно {my_func1(a, b)} или же: {my_func2(a, b)} или же: {my_func3(a, b)}")

# # 5
# sum = 0
#
# def summ_func(x):
#     global sum                           #вывел переменную за пределы функции
#     for number in x.split():              #разделил строку из чисел по пробелу
#         sum = sum + int(number)      #теперь все что будет добавлено в строку будет превращаться в числовой элемент и суммироваться с предыдущей суммой
#     return f"Сумма чисел: {sum}"               #получилась функция sum_func, возвращающая ф-строку с переменной суммы
#
# while True:
#     data = input("Введите строку чисел, разделённых пробелом или f для выхода: ")
#     if data.find("f"):
#         if data.endswith("f"):            #если строка data имеет f на конце
#             data = data.replace("f", "")      #тогда f в строке заменяется на пробел
#             print(summ_func(data))         #выводит вышеуказанную функцию и ликвидируется
#             break
#         else:
#             print(summ_func(data))            #если в строке нет f на конце, просто выполняется дальше
#     else:
#         break                  #если в строке вообще нет f тогда идет по циклу, снова клянчит строки

# 6
# def int_func(words):
#     result = ""
#     for el in words:
#         el = el[0].upper() + el[1:]
#         result += el + " "
#     return result
# string = str(input("Введите строку из слов но без заглавных букв: "))
# print(int_func(string.split()))
...

# LESSON 4

# #1
# def salary():
#     try:
#         time = float(input('Ваше время: '))
#         hour_rate = float(input('Почасовая ставка: '))
#         prize = float(input('Премия: '))
#         result = ((time * hour_rate) + prize) * 0.87
#         print(f"Ваша заработная плата c вычетом НДС составит: {result}")
#     except ValueError:
#         print("Это не число!")
# salary()

# #2
# list = [23, 21, 77, 343, 9000, 32, 766]
# new_list = [el for ind, el in enumerate(list) if list[ind] > list[ind-1]]     #даст генератор счётчик(ind)+элемент(el) для элементов list
# print(f'Исходный список {list}')
# print(f'Новый список {new_list}')

#3
# print([el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0])

#4
# list1 = [23, 212, 88, 765, 90, 433, 433, 65, 2, 2, 54, 34, 34, 88, 33, 90]
# print(f'Список: {list1}')
# print(f"Числа из списка без повторений: {[el for el in list1 if list1.count(el) == 1]}")

#5
# from functools import reduce
#
# def umnozhenie(el1, el2):
#     return el1 * el2
#
# print(f'Результат умножения всех элементов списка: {reduce(umnozhenie, [el for el in range(100, 1001) if el % 2 == 0])}')

#6a
# import itertools
# for i in itertools.count(100, 2):
#     print(i)
#
#     if i >= 105:
#         break

#6b
# import itertools
#
# c = 0
# for a in itertools.cycle('empire'):
#     if c >= 12:
#         break
#     print(a)
#     c += 1

# #7
# from itertools import count
# from math import factorial
#
# def generator():
#     for el in count(1):
#         yield factorial(el)
#
# gen = generator()
# c = 0
# for i in gen:
#     if c > 5:                                   # n = 5
#         break
#     print(i)
#     c += 1
...

...
# LESSON 5

#1
# out_file = open("my_text.txt", "x")
# out_file.writelines(input("Запись в файл следующего: "))
# print("")
# out_file.close

#2
# my_text2.txt
# I was following the
# I was following the pack
# All swallowed in their coats
# With scarves of red tied round their throats

# f = open("my_text2.txt", "r")
# content = f.read()
# print(f'Что в файле: \n{content}')
#
# f = open("my_text2.txt", "r")
# content = f.readlines()
# print(f'Количество строк: {len(content)}')
#
# f = open("my_text2.txt", "r")
# content = f.readlines()
# for el in range(len(content)):
#     print(f'Количество слов в {el} строке: {len(content[el].split())}')
#
# f.close

#3
# my_text
# Понасенков 250000
# Оклугин 20000
# Валерианкова 195750
# Карташев 9200
# Младший 19500

# with open("my_text.txt", "r") as f:
#     content = f.read().split('\n')
#     print(content)
#     success = []
#     unsuccess = []
#     salary = []
#     for el in content:
#         el = el.split()
#         if int(el[1]) <= 20000:
#             unsuccess.append(el[0])
#         else:
#             success.append(el[0])
#         salary.append(el[1])
#     average_salary = sum(map(int, salary)) / len(salary)
#     print(f"Сотрудники с окладом меньше 20000: {unsuccess}, сотрудники с окладом больше 20000: {success}")
#     print(f"Средний оклад сотрудников: {average_salary}")

#4
# to_rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}    #словарь перевода en в ru
# newfile = []                                                  #в новый файл
# with open('my_text3.txt', 'r') as f:
#     content = f.read().split('\n')                      #разделил содержимое по переносу строки
#     print(content)
#     for el in content:
#         el = el.split(' ', 1)                          #разделил каждый 'one - 1' по пробелу через 1
#         newfile.append(to_rus[el[0]] + ' ' + el[1])    #добавил в новый список ключ en
#     print(newfile)
#
# with open('my_text4.txt', 'w') as f2:
#     f2.writelines(newfile)

#5
# def summary():
#     try:
#         with open('my_text5.txt', 'w') as f:
#             line = input('Введите цифры через пробел: ')
#             f.writelines(line)
#             numbers = line.split()                               #разделил на числа
#
#             print(sum(map(int, numbers)))                         #каждый элемент превратит в int, суммирует
#     except ValueError:
#         print('Ошибка ввода-вывода, введены не цифры и даже не числа')
# summary()

#6
# my_text6.txt
# Информатика 100 50 20
# Физика 30 70 00
# Химия 30 00 00
# Гончарство 190 10 00

# hours = {}
# with open('my_text6.txt', 'r') as f:
#     for line in f:
#         subject, lect, pract, lab = line.split()
#         hours[subject] = int(lect) + int(pract) + int(lab)
#     print(f'количество занятий по предмету - \n {hours}')


#7
# my_text7.txt
# firm_1 ООО 10000 5000
# firm_2 ООО 20100 29000
# firm_3 ООО 78000 2000
# firm_4 ООО 10500 75000
# firm_5 ООО 99000 0

# import json
#
# profit = {}
# all_profit = 0
# average_profit = 0
# numb_plus_firm = 0
# with open('my_text7.txt', 'r') as f:
#     for line in f:
#         name, form, plus, minus = line.split()
#         profit[name] = int(plus) - int(minus)
#         if profit.setdefault(name) >= 0:
#             all_profit = all_profit + profit.setdefault(name)
#             numb_plus_firm += 1
#     if numb_plus_firm != 0:
#         average_profit = all_profit / numb_plus_firm
#         print(f'Cредняя прибыль фирм вышедших в плюс - {average_profit:.2f}')
#     else:
#         print(f'Прибыли вообще нет, все фирмы в убытке')
#     pr = {'средняя прибыль': round(average_profit)}
#     profit.update(pr)
#     # profit = list(profit)
#     print(f'Прибыль каждой компании - {profit}')                    #в список этот кортеж не получается поместить
#
# with open('my_text7.json', 'w') as f_js:
#     json.dump(profit, f_js)
#
#     js_str = json.dumps(profit)
#     print(f'Создан файл .json: \n 'f'{js_str}')
...

...
# LESSON 6
#1
# import time
# from time import sleep
#
# class TrafficLight:
#     __color = ["red", "yellow", "green"]
#
#     def running(self):
#         print('Lets start')
#         color = 0
#         while color < 3:
#             print(f'Traffic light is {TrafficLight.__color[color]}')
#             if color == 0:
#                 sleep(7)
#             elif color == 1:
#                 sleep(5)
#             elif color == 2:
#                 sleep(30)
#             color += 1
#         else:
#             print("Something is wrong here")
#
# TrafficLight = TrafficLight()
# TrafficLight.running()

# #2
# class Road:
#     def __init__(self, _length, _width, _mass_to_1cm, _thickness):
#         self._length = _length
#         self._width = _width
#         self._mass_to_1cm = _mass_to_1cm
#         self._thickness = _thickness
#
#     def mass(self):
#         return self._length * self._width * self._thickness * self._mass_to_1cm
#
#
# result = Road(5000, 5, 5, 5)                   # длина 5000м, ширина 5м, на 1см - 5кг, толщина 5см
# print(result.mass())

#3
# class Worker:
#     def __init__(self, name, surname, position, _income):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._income = {"wage": wage, "bonus": bonus}
#
# class Position(Worker):
#     def __init__(self, name, surname, position, wage, bonus):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self.wage = wage
#         self.bonus = bonus
#
#     def get_full_name(self):
#         return self.name + ' ' + self.surname
#
#     def get_total_income(self):
#         return self.wage + self.bonus
#
# worker1 = Position('Yes', 'Ornot', 'Self-entertainer', 250000, 125000)
# print(worker1.get_full_name())
# print(worker1.position)
# print(worker1.get_total_income())

#4
# class Car:
#     def __init__(self, speed, color, name, is_police):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = is_police
#
#     def go(self):
#         return f'{self.name} is gone mad'
#
#     def stop(self):
#         return f'{self.name} has stoped'
#
#     def turn_left(self):
#         return f'{self.name} omg TUUUUURNS left!'
#
#     def turn_right(self):
#         return f'{self.name} goes all right'
#
#     def show_speed(self):
#         return f'Your current speed is {self.speed}'
#
# class TownCar(Car):
#     def __init__(self, speed, color, name, is_police):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = is_police
#
#     def show_speed(self):
#         print(f'Current speed of town car {self.name} is {self.speed}')
#
#         if self.speed > 60:
#             return f'Goddamn! Your speed is {self.speed}! Slow down!'
#         else:
#             return f'Speed of {self.name} is okay. For now.'
#
#     def police(self):
#         if self.is_police:
#             return f'{self.name} is from police department. Please show us your documents'
#         else:
#             return f'{self.name} is not from police department'
#
# class WorkCar(Car):
#     def __init__(self, speed, color, name, is_police):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = is_police
#
#     def show_speed(self):
#         print(f'Current speed of your car {self.name} is {self.speed}')
#
#         if self.speed > 40:
#             return f'Speed of {self.name} is higher than allowed, sir. Please reduce the speed to the recommended level'
#         else:
#             return f'Speed of {self.name} is okay. Thank you, drive freely'
#
#     def police(self):
#         if self.is_police:
#             return f'{self.name} is from police department. Please show us your documents'
#         else:
#             return f'{self.name} is not from police department'
#
# class PoliceCar(Car):
#     def __init__(self, speed, color, name, is_police):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = is_police
#
#     def police(self):
#         if self.is_police:
#             return f'{self.name} is from police department. Please show us your documents'
#         else:
#             return f'{self.name} is not from police department'
#
#
# TownCar1 = TownCar(150, 'White', 'Accelerator3000', is_police=False)
# print(TownCar1.show_speed())
# print(TownCar1.police())
# print(TownCar1.go())


# #5
# class Stationary:
#     def __init__(self, title):
#         self.title = title
#
#     def draw(self):
#         return f'Start rendering {self.title}'
#
# class Pen(Stationary):
#     def __init__(self, title):
#         self.title = title
#
#     def draw(self):
#         return f'{self.title} is in your hands. Start rendering by pen!'
#
# class Pencil(Stationary):
#     def __init__(self, title):
#         self.title = title
#
#     def draw(self):
#         return f'{self.title} is in your hands. Start rendering by pencil!'
#
# class Handle(Stationary):
#     def __init__(self, title):
#         self.title = title
#
#     def draw(self):
#         return f'{self.title} is in your hands. Start rendering by handle!'
#
# pen1 = Pen('The pen')
# pencilW = Pencil('The pencil')
# handleF = Handle('The handle')
# print(pen1.draw())
# print(pencilW.draw())
# print(handleF.draw())
...

...
# LESSON 7
# 1
# class Matrix:
#     def __init__(self, list_1, list_2):                     #аргументы - два объекта
#         self.list_1 = list_1
#         self.list_2 = list_2
#
#     def __add__(self):
#         new_matr = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#
#         for i in range(len(self.list_1)):
#             for j in range(len(self.list_1[i])):
#                 new_matr[i][j] = self.list_1[i][j] + self.list_2[i][j]
#         return str('\n'.join(['\t'.join([str(j) for j in i]) for i in new_matr]))
#
#     # def __str__(self):
#     #     return str('\n'.join(['\t'.join([str(j) for j in i]) for i in new_matr]))
#
# my_matrix = Matrix([[19, 18, 17], [16, 15, 14], [13, 12, 11]], [[11, 12, 13], [14, 15, 16], [17, 18, 19]])
# print(my_matrix.__add__())


# #2
# class Clothes:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def get_square_coat(self):
#         return self.width / 6.5 + 0.5
#
#     def get_square_suit(self):
#         return self.height * 2 + 0.3
#
#     @property                                 # декоратор сделал функцию атрибутом
#     def get_full_square(self):
#         return str(f'FULL square is: {float(self.width / 6.5 + 0.5) + float(self.height * 2 + 0.3)}')
#
# class Coat(Clothes):
#     def __init__(self, width, height):
#         super().__init__(width, height)                         # Одежда отдала функцию init Пальто
#         self.square_coat = float(self.width / 6.5 + 0.5)
#
#     def __str__(self):            # площадь ткани для пальто
#         return f'Square of coat is {self.square_coat}'
#
# class Suit(Clothes):
#     def __init__(self, width, height):
#         super().__init__(width, height)
#         self.square_suit = float(self.height * 2 + 0.3)
#
#     def __str__(self):                # площадь ткани для костюма
#         return f'Square of suit is {self.square_suit}'
#
# coatA = Coat(6.5, 2)
# suitA = Suit(3, 1.5)
# clothes = Clothes(6.5, 1.5)
#
# print(coatA)
# print(suitA)
# print(suitA.get_square_suit())
# print(coatA.get_square_coat())
# print(clothes.get_full_square)

#3
# class Cell:
#     def __init__(self, quantity):
#         self.quantity = int(quantity)
#
#     def __str__(self):
#         return f'{self.quantity * "@"}'
#
#     def __add__(self, other):
#         return Cell(self.quantity + other.quantity)
#
#     def __sub__(self, other):                          # находит разницу двух клеток независимо от того где ячеек больше
#         if self.quantity > other.quantity:
#             return Cell(self.quantity - other.quantity) if self.quantity - other.quantity > 0 else "отрицательное значение!"
#         else:
#             return Cell(other.quantity - self.quantity) if other.quantity - self.quantity > 0 else "отрицательное значение!"
#
#     def __truediv__(self, other):
#         if self.quantity > other.quantity:
#             return Cell(self.quantity // other.quantity)
#         else:
#             return Cell(other.quantity // self.quantity)
#
#     def __mul__(self, other):
#         return Cell(int(self.quantity * other.quantity))
#
#     def make_order(self, one_row_cells):             # one_row_cells - сколько ячеек в 1 ряду, по 5
#         row = '\n'
#         for i in range(int(self.quantity / one_row_cells)):
#             row += f'{"@" * one_row_cells} \n'                         # заполненные ряды
#         row += f'{"@" * (self.quantity % one_row_cells)}'              # остатки (неполный ряд)
#         return row
#
# cells1 = Cell(18)
# cells2 = Cell(3)
# print(f'first cell looks like this: {cells1}')
# print(f'second cell looks like this: {cells2}')
# print(f'cell sum is: {cells1 + cells2}')
# print(f'cell subtraction is: {cells1 - cells2}')
# print(f'cell division is: {cells1 / cells2}')
# print(f'cell multiplication is: {cells1 * cells2}\n')
#
# print(cells1.make_order(5))
# print(cells2.make_order(5))
