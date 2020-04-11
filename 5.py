# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('my_f_5.txt', 'w') as f:
    a = []
    while True:
        b = input('введите число или q для выхода: ')
        if b == 'q':
            break
        a.append(b)
    c = ' '.join(a)
    f.write(c)

with open('my_f_5.txt', 'r') as f:
    a = f.readline()
    b = 0
    for el in a.split():
        b = b + int(el)
    print(b)
