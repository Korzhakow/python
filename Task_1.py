def div(*args):
    try:
        arg1 = int(input("Введите делимое >>> "))
        arg2 = int(input("Введите делитель >>> "))
        res = arg1 / arg2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "Неверный делитель. Нельзя использовать 0 как делитель"

    return res


print(f' Результат {div()}')
