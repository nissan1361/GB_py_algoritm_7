import random

def bubble_sort(data):
    n = 1
    while n < len(data):
        for i in range(len(data) -1 ):
            if data[i] < data[i + 1]:
                data[i], data[i+1] = data[i+1], data[i]
        n += 1


array = [random.randint(-100,100) for x in range(20)]
print(array)

bubble_sort(array)
print(array)

