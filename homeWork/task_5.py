# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное
# сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Drawing has just been started')


class Pen(Stationery):

    def draw(self):
        print('Drawing has just been started by pen')


class Pencil(Stationery):

    def draw(self):
        print('Drawing has just been started by pencil')


class Handle(Stationery):

    def draw(self):
        print('Drawing has just been started by handle')


smth = Stationery('abstraction')
blue_pen = Pen('people')
grey_pencil = Pencil('Fores')
black_handle = Handle('Graffiti')

smth.draw()
blue_pen.draw()
grey_pencil.draw()
black_handle.draw()
