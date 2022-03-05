# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def consumption(self, clth_param):
        pass

    @abstractmethod
    def full_name(self):
        pass


class Coat(Clothes):

    def __init__(self, name):
        self.name = name

    def consumption(self, clth_param):
        return clth_param / 6.5 + 0.5

    @property
    def full_name(self):
        return self.name


class Suit(Clothes):

    def __init__(self, name):
        self.name = name

    def consumption(self, clth_param):
        return 2 * clth_param + 0.3

    @property
    def full_name(self):
        return self.name


coat = Coat('Tommy Hilfiger')
suit = Suit('Lacoste')

print(coat.full_name)
print(suit.full_name)
print(f'Fabric consumption for coat {coat.full_name} = {coat.consumption(10):.2f}')
print(f'Fabric consumption for coat {suit.full_name} = {suit.consumption(20):.2f}')
