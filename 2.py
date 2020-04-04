# Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать
# параметры как именованные аргументы. Реализовать вывод
# данных о пользователе одной строкой.


def my_func(name, surname, birth_year, city, email, phone):
    print(name, ';', surname, ';', birth_year, ';', city, ';', email, ';', phone)


my_func(name='Andrey', surname='Kovalev', birth_year='1984', city='Colorado Spring', email='AndColorado@yandex.ru',
        phone='19181234567')
