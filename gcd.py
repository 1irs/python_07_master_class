a: int = int(input('a'))
b: int = int(input('b'))

# программа выходит если b = 0
# !=
# Fira Code
# !=
while b != 0:
    if a > b:
        a = a - b
    else:
        b = b - a

print(a)
