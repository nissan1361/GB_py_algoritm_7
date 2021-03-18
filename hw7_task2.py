import random

def insertion_sort(data):
    for i in range(1, len(data)):
        spam = data[i]
        j = i
        while data[j - 1] > spam and j > 0:
            data[j] = data[j - 1]
            j -=1
        data[j] = spam
        

array = [random.randint(0,50) for x in range(15)]
print("Исходный массив: {}", format(array))

insertion_sort(array)
print("Новый массив: {}", format(array))
