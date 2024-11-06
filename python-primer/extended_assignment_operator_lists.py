alpha = [1, 2, 3]
beta = alpha

beta += [4, 5]  # Mutates the same list
beta = beta + [6, 7]  # Re-assigns a new list to beta

print(f"alpha = {alpha}")
print(f"beta  = {beta}")
