def is_multiple(n, m):
    return m % n == 0


n = 4
m = 16
result = is_multiple(n, m)

print(f"Is {m} a multiple of {n}?\n{result}")
