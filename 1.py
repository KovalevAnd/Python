# Реализовать скрипт, в котором должна быть предусмотрена функция расчета
# заработной платы сотрудника. В расчете необходимо использовать
# формулу: (выработка в часах*ставка в час) + премия. Для выполнения
# расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

script_name, hour, st, bonus = argv
hour = int(hour)
st = int(st)
bonus = int(bonus)


def zp_func(hour, st, bonus):
    zp = 0
    zp = (hour * st) + bonus
    return zp


print(zp_func(hour, st, bonus))
