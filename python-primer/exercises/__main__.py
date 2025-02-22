import random


def generate_list():
    return [random.randint(1, 20) for _ in range(0, 5)]


list_input = generate_list()

print(f"List = {list_input}")


# Time complexity  => O(N)
# Space complexity => O(N)
def is_distinct(list_input):
    num_set = set()

    for item in list_input:
        if item in num_set:
            return False
        num_set.add(item)

    return True


print(f"is_distinct??? {is_distinct(list_input)}")
