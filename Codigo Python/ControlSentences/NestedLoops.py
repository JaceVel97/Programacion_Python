numbers = [5, 2, 5, 2, 2]
value = ''
for x in numbers:
    for y in range(x):
        value += 'x'
    print(value)
    value = ''