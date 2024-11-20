import random


def pseudo_random_generator():
    yield random.randint(1, 100)


# Generate a list of 10 random numbers between 1-100
random_numbers = [next(pseudo_random_generator()) for _ in range(0, 10)]

print(random_numbers)
