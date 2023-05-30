# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

def find_indexes(arr, min_val, max_val):
    return [i for i, num in enumerate(arr) if min_val <= num <= max_val]


# Пример использования функции
nums = [10, 5, 1, 12, 10, 7, 9]
min_value = 5
max_value = 10
result = find_indexes(nums, min_value, max_value)
print("Индексы элементов в заданном диапазоне:", result)