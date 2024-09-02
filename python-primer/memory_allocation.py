var_1 = 98.6
var_2 = var_1

print(hex(id(var_1)))
print(hex(id(var_2)))

var_2 = 100

print(hex(id(var_1)))
print(hex(id(var_2)))
