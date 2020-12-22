seconds = int(input("Введите время в секундах >>> "))
minutes = 0
hours = 0
if seconds < 0:
    print("Введено отрицательное время")

elif seconds >= 60:
    for seconds in range(60, seconds + 1):
        minutes = seconds // 60
        seconds = seconds % 60
    for minutes in range(60, minutes + 1):
        hours = minutes // 60
        minutes = minutes % 60
    print(f"{hours} ч, {minutes} м, {seconds} с")
