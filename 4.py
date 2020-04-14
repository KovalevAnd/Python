# Реализуйте базовый класс Car. У данного класса должны быть следующие
# атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних
# классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен
# показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.


class Car:
    speed = None
    color = None
    name = None
    is_police = False

    def go(self):
        print('машина поехала')

    def stop(self):
        print('машина остановилась')

    def turn(self, direction):
        print('вы повернули:', direction)

    def show_speed(self):
        print('ваша скорость:', self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('ваша скорость:', self.speed, ' - вы превысили скорость')
        else:
            print('ваша скорость:', self.speed)


class SportCar(Car):
    color = 'красный'


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('ваша скорость:', self.speed, ' - вы превысили скорость')
        else:
            print('ваша скорость:', self.speed)


class PoliceCar(Car):
    is_police = True


town_car = TownCar()
sport_car = SportCar()
work_car = WorkCar()
police_car = PoliceCar()

town_car.speed = 70
town_car.name = 'KIA'
town_car.color = 'серебристый'

sport_car.speed = 130
sport_car.name = 'FERRARI'

work_car.speed = 41
work_car.name = 'HYUNDAI'
work_car.color = 'серый'

police_car.speed = 140
police_car.name = 'BUGATTI'
police_car.color = 'синий'

print('TownCar:', town_car.speed, town_car.name, town_car.color)
print('SportCar:', sport_car.speed, sport_car.name, sport_car.color)
print('WorkCar:', work_car.speed, work_car.name, work_car.color)
print('PoliceCar:', police_car.speed, police_car.name, police_car.color)

town_car.go()
town_car.stop()
town_car.turn('налево')
town_car.show_speed()
work_car.show_speed()
police_car.show_speed()
