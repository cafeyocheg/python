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
#
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
#













