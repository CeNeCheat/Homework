list = []
friends = [input("Добавьте трех друзей: ").capitalize(), input().capitalize(), input().capitalize()]
for s in friends:
    list.append(s)
while True:
    user= input("Хотите добавить еще? ").capitalize()
    if user == "Да" or user == "Yes":
        friend = input("Введите имя друга: ").capitalize()
        list.append(friend)
        for s in list:
            print(s)
    elif user == "Нет" or user == "No":
        for s in list:
            print(len(list))
        break
    else:
        print("Что ты ввел? Алло! Ответь да или нет! Не строй из себя умника!")


