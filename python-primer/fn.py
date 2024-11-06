import random

N = 10
data = [random.randint(1, 10) for _ in range(0, N)]
target = 8


def count(data, target):
    occurrence = 0

    for number in data:
        if number == target:
            occurrence += 1

    return occurrence


result = count(data, target)

print(f"Original list = {data}")
print(f"Target number = {target}")
print(f"Occurrences   = {result}")

data = [random.randint(1, 10) for _ in range(0, 10)]


def contains(data, target):
    for val in data:
        if val == target:
            return True

    return False


target = random.randint(1, 10)

print(f"Original list = {data}")
print(f"Contains {target}???")
print(contains(data, target))
