n = int(input("Введите число от 1 - 20: "))
percent_1 = "процент"
percent_2 = "процента"
percent_3 = "процентов"

if n <= 0:
    print("Слишком маленькое число")
elif n == 1:
    print(n, percent_1)
elif n > 1 and n < 5:
    print(n, percent_2)
elif n >= 5 and n <= 20:
    print(n, percent_3)
else:
    print("Слишком большое число")
