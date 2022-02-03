def is_prime(number: int) -> bool:
    """
    Эта функция определеят, является ли
    заданное число простым.
    :param number: Число для проверки.
    :return: True, если простое. False, если составное.
    """
    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def primes_in_range(number: int) -> list[int]:
    """
    Найти все простые числа в диапазоне от 2 до number
    :param number: Верхняя граница диапазона.
    :return: Список простых чисел.
    """
    primes: list[int] = []
    for i in range(2, number):
        if is_prime(i):
            primes.append(i)

    return primes


print(primes_in_range(10))
print(primes_in_range(20))
print(primes_in_range(100))
