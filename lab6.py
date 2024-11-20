import math
#TASK 1
def nested_sqrt(m, n):
    # Базовый случай
    if n == 1:
        return math.sqrt(m)
    # Рекурсивный случай
    else:
        return math.sqrt(m + nested_sqrt(m, n - 1))

# Пример использования
m = 5
n = 45
result = nested_sqrt(m, n)
print(f"x({n}) = {result}")

#TASK 2
def nested_sqrt_iterative(m, n):
    result = math.sqrt(m)  # Начинаем с x(1) = sqrt(m)
    for _ in range(1, n):
        result = math.sqrt(m + result)  # Вычисляем следующий член последовательности
    return result

# Пример использования
m = 5
n = 45
result = nested_sqrt_iterative(m, n)
print(f"x({n}) = {result}")


#TASK 3
def nested_sqrt_memo(m, n, memo={}):
    # Базовый случай
    if n == 1:
        return math.sqrt(m)
    # Проверка, есть ли результат в memo
    if (m, n) in memo:
        return memo[(m, n)]
    # Рекурсивный случай
    result = math.sqrt(m + nested_sqrt_memo(m, n - 1, memo))
    # Сохранение результата в memo
    memo[(m, n)] = result
    return result

# Пример использования
m = 2
n = 3
result = nested_sqrt_memo(m, n)
print(f"x({n}) = {result}")
