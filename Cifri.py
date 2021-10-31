numbers = (314, 257, 100, 200)
for num in numbers:
    print(num)
user = int(input("Введите трехзначное числно: "))
if user == numbers[0] or user == numbers[2] or user == numbers[3] or user == numbers[1]:
    print(numbers.index(user))