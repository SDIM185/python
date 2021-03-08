def sum_of_numbers(value):
    n = 0
    while value != 0:
        n += value % 10
        value //= 10
    return n

list_of_numbers = []
for x in range(1, 1001, 2):
    list_of_numbers.append(x**3)
# print(list_of_numbers)

answer_a = sum(filter(lambda num: sum_of_numbers(num) % 7 == 0, list_of_numbers))

print(answer_a)

list_of_numbers_2 = []
for z in range(1, 1001, 2):
    list_of_numbers_2.append(z**3 + 17)
# print(list_of_numbers_2)

answer_b = sum(filter(lambda num: sum_of_numbers(num) % 7 == 0, list_of_numbers_2))

print(answer_b)
