def fibonacci():
    a = 0
    b = 1

    while True:
        yield a
        future = a + b
        a = b
        b = future


N = 5
output = fibonacci()
series_str = ""

for val in range(0, N):
    series_str += f"{val}, "

series_str = series_str[:-2]

print(series_str)
