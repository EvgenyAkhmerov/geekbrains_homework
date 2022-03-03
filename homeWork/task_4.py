# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула
# (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('The car has just gone')

    def stop(self):
        print('The car has just stoped')

    def turn(self, direction):
        print(f'The car has just turned {direction}')

    def show_speed(self):
        print(f'Current speed = {self.speed}')


class TownCar(Car):

    def show_speed(self):
        if self.speed >= 60:
            print(f'Be careful, over speed! | current speed = {self.speed}')


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if self.speed >= 40:
            print(f'Be careful, over speed! | current speed = {self.speed}')


class PoliceCar(Car):
    pass


Nissan = TownCar(70, 'black', 'Nissan Almer')
Ferrari = SportCar(150, 'red', 'Ferrari Enzo')
Gaz = WorkCar(80, 'white', 'Gazel Next')
UAZ = PoliceCar(60, 'blue', 'UAZ Patriot', is_police=True)

print(Nissan.speed, Nissan.is_police, Nissan.name, Nissan.color)
print(UAZ.speed, UAZ.is_police, UAZ.name, UAZ.color)
print(Ferrari.speed, Ferrari.is_police, Ferrari.name, Ferrari.color)
print(Gaz.speed, Gaz.is_police, Gaz.name, Gaz.color, end='\n'*2)
Nissan.show_speed()
Ferrari.show_speed()
UAZ.show_speed()
Gaz.show_speed()
