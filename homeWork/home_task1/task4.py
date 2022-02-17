#4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = input('Введите целое положительное число')
number = int(number)
num = 0
max = 0
k = 1
#print(number, type(number))
while max != 9 and (number // k) != 0:
    num = (number % (k*10) // k)
    max = num if num > max else max
    print(num)
    k *= 10

print(f'Наибольшая цифра: {max}')
