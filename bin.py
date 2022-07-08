password = 'sunshine'
size = len(password)
value = "1"*size
value_int = int(value, 2)
test=bin(value_int)
print(test[2:])