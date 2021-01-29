# try:
#    a = input("hello")
#    x = a + 1
# except TypeError:
#     print("не складывай число и строку")
# except ZeroDivisionError:
#     print("Привет")
# finally:
#     print("Finally сработал")

# while True:
#     try:
#         num1 = int(input("enter fist number"))
#         num2 = int(input("enter second number"))
#         znak = input("enter sign")
#         if num1 is None or num2 is None or znak is None:
#             raise ValueError
#         num1 = int(num1)
#         num2 = int(num2)
#         if znak == "+":
#             print(num1 + num2)
#         try:
#             if znak == "/":
#                 print(num1 / num2)
#         except ZeroDivisionError:
#             print("На ноль делать нельзя")
#             continue
#
#         break
#     except ValueError:
#             print("введите еще раз")
#             continue
#
# try:
#     print(1 + '1')
# except TypeError:
#     print("Ошибка типа")
# else:
#     print("Все хорошо")

stroki = 'stroka'
spisok = [1, 2, 3, 'asd', [1, 2, 3, [123]]]
spisok_stroka = list(stroki)
# print(spisok stroka)
chislo = 1
drob = 1.2
boolean = True  # 1
boolean_2 = False  # 0
mnojestvo = {1, 2, 3,}
x = 'j-hope'
s = set(x)
# print(x)
slovar = {'First value': 'Привет Ким Намджун'}
cortej = (1, 2, 3,)
cortej_2 = tuple(x)

f_s = frozenset(x)
n = None
