numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x * x, numbers))

print(f"Original list = {numbers}")
print(f"Computed list  = {squares}")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(f"\nOriginal list = {numbers}")
print(f"Computed list = {even_numbers}")
