n = int(input("Введите число: "))
sec = "сек"
min = "мин"

if n <= 60:
    print(n, sec)
elif n > 60 and n <= 3599:
    print(n // 60, min, n % 60, sec)
# if n >= 3600:
else:
    print("Алё, полегче, откуда такие цифры???\nМы это еще не проходили)")
