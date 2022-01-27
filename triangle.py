"""
Дано: стороны треугольника.
Определить: могут ли эти стороны быть сторонами треугольника?
"""
# Ввод данных
a: int = int(input('a: '))
b: int = int(input('b: '))
c: int = int(input('c: '))

print('Стороны треугольника', a, b, c)

ab_longer_c: bool = (a + b) > c
ac_longer_b: bool = (a + c) > b
bc_longer_a: bool = (b + c) > a

# Булева алгебра: AND
# как работает AND
# False and False    == False
# False and True     == False
# True  and False    == False
# True  and True     == True

if ab_longer_c and ac_longer_b and bc_longer_a:
    print('МОГУТ быть сторонами треугольника')
else:
    print('НЕ МОГУТ быть сторонами треугольника')
