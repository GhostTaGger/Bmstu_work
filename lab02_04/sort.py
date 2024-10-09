import random
import timeit
import functools
import matplotlib.pyplot as plt
import numpy as np

def shaker_sort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1
    while swapped:
        swapped = False
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        end -= 1
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        start += 1

@functools.lru_cache(maxsize=None)
def timing_decorator(ndigits: int, number: int) -> callable:
    def decorator(func: callable) -> callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> float:
            usage_time = timeit.timeit(
                lambda: func(*args, **kwargs),
                number=number,
            )
            return round(usage_time / number, ndigits)

        return wrapper

    return decorator

max_n = 100001
max_vector = np.array([random.randint(1, 100) for _ in range(max_n)])

ndigits = 6
number_of_runs = 5

n_values = [100, 1000, 2000, 3500, 5000, 10000, 20000, 25000]
average_times_shaker_sort = []

@timing_decorator(ndigits, number_of_runs)
def calculate_shaker_sort(vector):
    shaker_sort(vector)

for n in n_values:
    print(n)

    average_time = calculate_shaker_sort(max_vector[:n].copy())
    average_times_shaker_sort.append(average_time)

plt.plot(n_values, average_times_shaker_sort, linestyle='-', color='r')
plt.title('Зависимость времени сортировки перемешиванием от n')
plt.xlabel('n')
plt.ylabel('Среднее время выполнения (секунды)')

plt.savefig('shaker_sort_time_.png')