while True:
    try:
        number_1 = int(input("введите 1 число: "))
        number_2 = int(input("введите 2 число: "))
        number_3 = int(input("введите 3 число: "))
        number_4 = int(input("введите 4 число: "))
        operation = input("Какую операцию провести +, -, /, *, %, //: ")

        if operation == "+":
            result = number_1 + number_2 + number_3 + number_4
            print(result)
        elif operation == "-":
            result = number_1 - number_2 - number_3 - number_4
            print(result)
        elif operation == "/":
            result = number_1 / number_2 / number_3 / number_4
            print(result)
        elif operation == "*":
            result = number_1 * number_2 * number_3 * number_4
            print(result)
        elif operation == "%":
            result = number_1 % number_2 % number_3 % number_4
            print(result)
        elif operation == "//":
            result = number_1 // number_2 // number_3 // number_4
            print(result)
        else:
            print("введен неверный знак операции")

        restart_or_stop = input("Если хотите продолжить калькулятор нажмите Enter,"
                                "Но если хотите выйти напишите stop: ")
        if restart_or_stop == "stop":
            break

    except ValueError:
        print('вводи числа, ok?')