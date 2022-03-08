# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNumber:

    def __init__(self, real, im):
        self.real = real
        self.im = im

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.im + other.im)

    def __mul__(self, other):
        return ComplexNumber(
            self.real * other.real - self.im * other.im,
            self.real * other.im + self.im * other.real
        )

    def __str__(self):
        return f'{self.real}+({self.im})i'


num_1 = ComplexNumber(1, 2)
num_2 = ComplexNumber(1, -3)
print(num_1, num_2)

print(num_1 + num_2)
print(num_1 * num_2)
