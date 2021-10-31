while True:
    colors = (" черный", "Белый", "Серый", "Синий", "Красный", "Голубой", "Желтый", "Оранжевый", "Зелёный", "Коричневый")
    print(colors)
    firstchoose =int(input("Введите число. (Диапозон от 0 до 4): "))
    if firstchoose < 0 or firstchoose > 4:
        print("Неправильно")
        break
    secchoose= int(input("Введите число. (Диапозон от 5 до 9): "))
    if secchoose < 5 or secchoose > 9:
        print("Неправильно")
        break
    print(colors[firstchoose:secchoose])
    break
    
    