# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname,
# position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на
# словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы
# получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).


class Worker:
    name = None
    surname = None
    position = None
    _income = {'wage': None, 'bonus': None}


class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        print(Worker._income['wage'] + Worker._income['bonus'])


a = Position()
a.name = 'Андрей'
a.surname = 'Гикбрэйнсов'
a.position = 'Студент'
a._income['wage'] = 10000
a._income['bonus'] = 2000

print(a.name)
print(a.surname)
print(a.position)
print(a._income)

a.get_full_name()
a.get_total_income()
