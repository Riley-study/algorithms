from random import randint
import time

# Обязательное ДЗ - Реализовать алгоритм пирамидальной сортировки (сортировка кучей).
arr_length = 10
init_array = [i for i in range(0, arr_length)]
for i in range(0, arr_length):
    init_array[i] = randint(0, 100)

print(*init_array)


def heapyfi(array, n, index):
    largest = index
    left = index * 2 + 1
    right = index * 2 + 2

    if left < n and array[index] < array[left]:
        largest = left
    if right < n and array[largest] < array[right]:
        largest = right
    if largest != index:
        array[index], array[largest] = array[largest], array[index]
        heapyfi(array, n, largest)


def heapSort(array):
    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        heapyfi(array, n, i)

    for i in range(n-1, 0, -1):
        array[0], array[i] = array[i], array[0]
        heapyfi(array, i, 0)

heapSort(init_array)
print(init_array)
