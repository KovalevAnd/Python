# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def my_func(x, y):
    while True:
        if y == 0:
            y = int(input('введите число не равное 0: '))
        else:
            z = x / y
            break
    return z


print(my_func(int(input('введите x: ')), int(input('введите y: '))))
