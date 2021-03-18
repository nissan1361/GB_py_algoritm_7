import random

array = [random.randint(0,35) for x in range(11)]

print(array)

def mediana(data, first, last):

    data = data.copy()
    md = len(data) // 2

    if first >= last:
        return data[md]

    flag = data[md]
    i = first
    j = last

    while i <= j:

        while data[i] < flag:
            i += 1

        while data[j] > flag:
            j -= 1

        if i <= j:
            data[i], data[j] = data[j], data[i]
            i += 1
            j -= 1

    if md < i:
        data[md] = mediana(data, first, j)

    elif j < md:
        data[md] = mediana(data, i, last)

    return data[md]

res = mediana(array, 0, len(array) -1)
print(res)

