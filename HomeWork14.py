# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4 

import os, time
if os.name == 'nt':
    os.system('cls')  # очистить консоль на Windows
else:
    os.system('clear')  # очистить консоль на остальных операционных системах
def sum(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return sum((a & b) << 1, a ^ b)

def sum_by_one(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return sum_by_one(a-1, b) + 1

def sum_two(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return sum_two(a-1, b-1) + 2

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

start_time = time.time()
result = sum(a, b)
end_time = time.time()
print("Результат сложения через битовые операции: ", result)
print("Время выполнения:", end_time - start_time, "секунд")

start_time = time.time()
result = sum_by_one(a, b)
end_time = time.time()
print("Результат сложения через операции +1 и -1: ", result)
print("Время выполнения:", end_time - start_time, "секунд")

start_time = time.time()
result = sum_two(a, b)
end_time = time.time()
print("Результат сложения через две операции -1 и одну операцию +2: ", result)
print("Время выполнения:", end_time - start_time, "секунд")