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





















