prices = [10, 20, 30, 40]
result = 0

for value in prices:
    result += value

print(f'The totally cost is: {result}')

numbers = [25, 310, 65, 45, 65, 12, 65, 65, 65]
largest_number = 0
for i in numbers:
    if i > largest_number:
        largest_number = i
print(largest_number)

for i in numbers:
    if numbers.count(i) != 1:
        numbers.remove(i)
print(numbers)

name_number = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}
phone = input("Phone: ")
phoneL = ''
for i in phone:
    phoneL += name_number.get(i, '$') + ' '
print(phoneL)
