# Напишите функцию, которая находит
# наибольший общий делитель двух натуральных чисел
# На входе два числа, на выходе их НОД.

def NOD(a, b):
    nod = 1
    for i in range(max(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i
