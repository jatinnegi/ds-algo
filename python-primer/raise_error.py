import math


def sqrt(x):
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric")
    elif x < 0:
        raise ValueError("x must be positive")

    return math.sqrt(x)


try:
    print(sqrt(-24))
except ValueError as e:
    print(e)

try:
    print(sqrt("invalid???"))
except TypeError as e:
    print(e)

try:
    print(sqrt(4))
except Exception as e:
    print(e)
