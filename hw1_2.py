# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды
# и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

sec = int(input('введите время в секундах: '))
hour = sec // 3600
mnt = (sec - (hour * 3600)) // 60
sec_f = sec - (hour * 3600) - (mnt * 60)

hour_0 = hour
if hour < 10:
    hour_0 = '0' + str(hour)

mnt_0 = mnt
if mnt < 10:
    mnt_0 = '0' + str(mnt)

sec_0 = sec_f
if sec_f < 10:
    sec_0 = '0' + str(sec_f)

print(hour_0, ':', mnt_0, ':', sec_0)

