#    0  1  2  3  4  5
a = [6, 2, 7, 0, 1, -1, 12, 3]#?????
print('исходный массив', a)

# Переберет индексы 0, 1, 2, 3
for y in range(len(a)-1):
    for i in range(len(a)-1-y):
        # Это условие решает в каком порядке должны быть элементы массива
        if a[i] > a[i+1]:
            temp = a[i]
            a[i] = a[i+1]
            a[i+1] = temp
            print(a)

print('отсортированный массив', a)
