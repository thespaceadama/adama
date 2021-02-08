print('+ : Плюс')
print('- : Минус')
print('* : Умножение')
print('/ : Деление')
print('//: Целочисленное деление')
print("%: Остаток")
select = input('Введите знак для операции: ')
number_1 = int(input('Ввведите первое число: '))
number_2 = int(input('Ввведите второе число: '))
number_3 = int(input('Ввведите третье число: '))
number_4 = int(input('Ввведите четвертое число: '))
if select == '+':
    result = number_1 + number_2 + number_3 + number_4
    print(number_1, '+', number_2, '+', number_3, '+', number_4, '=', result)
if select == '-':
    result = number_1 - number_2 - number_3 - number_4
    print(number_1, '-', number_2, '-', number_3, '-', number_4, '=', result)
if select == '*':
    result = number_1 * number_2 * number_3 * number_4
    print(number_1, '*', number_2, '*', number_3, '*', number_4, '=', result)
if select == '/':
    result = number_1 / number_2 / number_3 / number_4
    print(number_1, '/', number_2, '/', number_3, '/', number_4, '=', result)
if select == '//':
    result = number_1 // number_2 // number_3 // number_4
    print(number_1, '//', number_2, '//', number_3, '//', number_4, '=', result)
if select == '%':
    result = number_1 % number_2 % number_3 % number_4
    print(number_1, '%', number_2, '%', number_3, '%', number_4, '=', result)
