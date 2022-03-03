# 1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный)
# — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и
# завершать скрипт.


class TrafficLight:

    def __init__(self, color):
        self.__color = color

    def running(self):
        from itertools import cycle
        import time

        colors = ['RED', 'YELLOW', 'GREEN']
        colors_time = {'RED': 7, 'YELLOW': 2, 'GREEN': 5}

        for color in colors[colors.index(self.__color):3]:
            print(color, end='')
            time.sleep(colors_time[color])
            print(end='\r')

        for color in cycle(colors):
            print(color, end='')
            time.sleep(colors_time[color])
            print(end='\r')


traffic_light = TrafficLight('YELLOW')
traffic_light.running()
