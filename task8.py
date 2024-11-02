# Напишите рекурсивную функцию, которая
# раскладывает натуральное число на простые сомножители.
#
# Пример:
# Ввод:
# 378
# Вывод:
# 2*3*3*3*7

def to_primes(N):
    for i in range(2, int(N ** 0.5) + 1):
        if N % i == 0:
            return str(i) + '*' + to_primes(N // i)
    return str(N)

print(to_primes(int(input())))


