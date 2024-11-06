import random

N = 10
random_numbers = [random.randint(1, 100) for _ in range(0, N)]
biggest_idx = 0

for i in range(1, N):
    if random_numbers[i] > random_numbers[biggest_idx]:
        biggest_idx = i

print(f"Original list  = {random_numbers}")
print(f"Largest number = {random_numbers[biggest_idx]}")
print(f"Found at index = {biggest_idx}")
