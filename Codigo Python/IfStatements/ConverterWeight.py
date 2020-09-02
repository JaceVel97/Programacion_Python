# Statements of variables that I use after
weight = float(input("Enter the weight that you need to change:\n "))
letter = input('(L)bs or (K)g:\n ')
result = 0.0

if letter.lower() == 'l':
    result = weight / 2.20462
    print(f'You are {result} kilograms')
elif letter.lower() == 'k':
    result = weight * 2.20462
    print(f'You are {result} pounds')
else:
    print("The option to convert doesn't exists")