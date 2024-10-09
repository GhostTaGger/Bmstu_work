import time
import matplotlib.pyplot as plt
import random

def measure_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr)
    end_time = time.time()
    return end_time - start_time
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Generate arrays of different sizes
sizes = [1000, 5000, 10000, 100000]
times = []

for size in sizes:
    arr = [random.randint(0, 1000) for _ in range(size)]
    time_taken = measure_time(quick_sort, arr)
    times.append(time_taken)

# Plot the results
plt.plot(sizes, times, marker='o')
plt.xlabel('Array Size')
plt.ylabel('Time (seconds)')
plt.title('Time Complexity of Quick Sort')
plt.grid(True)
plt.show()