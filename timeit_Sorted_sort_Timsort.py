import random
import timeit

# Алгоритм сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Алгоритм сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Генерація випадкових даних
def generate_random_data(size):
    return [random.randint(0, 10000) for _ in range(size)]

# Тестування алгоритмів
def time_sorting_algorithm(sort_func, data):
    data_copy = data.copy()  # Копіюємо дані
    start_time = timeit.default_timer()
    sort_func(data_copy)
    return timeit.default_timer() - start_time

# Параметри тестування
sizes = [100, 1000, 5000, 10000]
results = []

for size in sizes:
    data = generate_random_data(size)
    merge_time = time_sorting_algorithm(merge_sort, data)
    insertion_time = time_sorting_algorithm(insertion_sort, data)
    timsort_time = time_sorting_algorithm(sorted, data)  # Використання Timsort

    results.append((size, merge_time, insertion_time, timsort_time))

# Виведення результатів
print("Size | Merge Sort | Insertion Sort | Timsort")
for size, merge_time, insertion_time, timsort_time in results:
    print(f"{size:4} | {merge_time:.6f} | {insertion_time:.6f} | {timsort_time:.6f}")

# Висновки:
# Порівнявши три алгоритми сортування: злиттям, вставками та Timsort за часом виконання де використали модуль timeit, 
# маємо можливість зробити висновки не теоретичні, а практичні, приведені в таблиці розрахунків де видно, 
# що використання вбудованих в Python алгоритмів значно ефективніші ніж самостійне кодування.
# Розрахунки показують що, сортування злиттям займає час O(n log n), а сортування вставками O(n) у найкращому випадку, а найгіршому O(n^2), 
# Timsort O(n log n) у середньому та найгіршому випадках, O(n) у найкращому. 
# Найефективніше працює Timsort, особливо це помітно при зростанні розміру данних.