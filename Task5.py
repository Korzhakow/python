profit = int(input("Введите прибыль >>> "))
cost = int(input("Введите издержки >>> "))

if profit > cost:
    pc = profit / cost
    print(f"Компания работает с рентабельностью в {pc}")
    s = int(input("Введите количество сотрудников >>> "))
    ps = profit / s
    print(f"Прибыль на одного сотрудника {ps}")
else:
    print("Компания работает в убыток")
