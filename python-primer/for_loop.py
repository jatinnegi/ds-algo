import random

random_numbers = [random.randint(1, 10) for _ in range(0, 10)]

total = 0

for number in random_numbers:
    total += number

print(random_numbers)
print(total)
