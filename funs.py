def shift(l, num):
    if num > 0:
        for i in range(1, num):
            n = l.pop()
            l.insert(0, n)
            print(l)
    elif num < 0:
        for x in range(num, -1):
            n = l.pop(0)
            l.append(n)
            print(l)


num = int(input("Введи цифру: "))
l = input("Введи список чисел: ").split()
l = [int(i) for i in l]
shift(l, num)