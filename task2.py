# Напишите функцию int(int(num)
#number_to_words(num), которая принимает
# в качестве аргумента натуральное число num и возвращает
# его словесное описание на русском языке.
#
# Примечание 1.
# Считайте, что число 1 ≤ num ≤ 99.
#
# Примечание 2.
# Следующий программный код:
#
# print(number_to_words(7))
# print(number_to_words(85))
# должен выводить:
#
# семь
# восемьдесят пять
def number_to_words(num):
    #num = int(num)
    a = ["один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь",
         "девять", "десять"]
    if num >= 1 and num <= 10:
        print(a[num-1])
    elif 10 > num < 20:
        if num == 11 or num == 13:
            print(a[num-1] + "надцать")
        elif num == 12:
            print("двенадцать")
        else:
            print(a[num-1][::len(a[num-1])]+"надцать")
    elif 20 <= num < 90:
        if num % 10 == 0:
            if num == 20 or num == 30:
                print(a[num//10 - 1] + "дцать")
            elif num == 40:
                print("сорок")
            elif num == 50 or num == 60 or num == 70 or num == 80:
                print(a[num // 10 - 1] + "десят")
            elif num == 90:
                print("девяносто")
        elif num % 10 != 0:
            if num//10 == 2 or num//10 == 3:
                print(a[num//10 - 1] + "дцать" + " " + a[num%10 - 1])
            elif num//10 == 4:
                print("сорок" + " " + a[num%10 - 1])
            elif num//10 == 5 or num//10 == 6 or num//10 == 7 or num//10 == 8:
                print(a[num // 10 - 1] + "десят" + " " + a[num%10 - 1])
            elif num//10 == 9:
                print("девяносто" + " " + a[num%10 - 1])
    elif num>=90:
        if num % 10 == 0:
            print("девяносто")
        else:
            print("девяносто" + " " + a[num%10-1])
#number_to_words((k for k in range(1, 100)))
for i in range(1, 100):
    number_to_words(i)