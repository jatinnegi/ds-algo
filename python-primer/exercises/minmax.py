import random


def minmax(numbers):
    min_num = numbers[0]
    max_num = numbers[0]

    for i in range(1, len(numbers)):
        if numbers[i] < min_num:
            min_num = numbers[i]

        if numbers[i] > max_num:
            max_num = numbers[i]

    return min_num, max_num


numbers = [random.randint(1, 100) for _ in range(0, 10)]

min_num, max_num = minmax(numbers)

print(f"List = {numbers}")
print(f"Min = {min_num}")
print(f"Max = {max_num}")
