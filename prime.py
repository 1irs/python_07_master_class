a: str = input('Введите число N: ')
print(a)
n: int = int(a)
print(n)
# 5: %1 = 0; 5%2 = 1; 5 % 3 = 2; 5 % 4 = 1; 5 % 5 = 0
# 6: 6 % 1 = 0; 6 % 2 = 0; 6 % 3 = 0; 6 % 4 = 2; 6 % 5 = 1; 6 % 6 = 0
# range (1,5, N) = 1,2,3,4 : 1

for numberEasy in range(2, n):
    delitel: int = 0
    for i in range(2, numberEasy):
        #print(i)
        if numberEasy % i == 0:
            delitel = delitel + 1
            #print(f'Число {numberEasy} поделилось на {i} без остатка')
    #print(f'Количество делителей числа {numberEasy}', delitel)
    if delitel == 0:
        print(f'Число {numberEasy} простое')
    #else:
        #print(f'Число {numberEasy} составное')
