data = [1, 2, 3, 4]

iterator = iter(data)

while True:
    try:
        item = next(iterator)
        print(item)
    except StopIteration:
        break
