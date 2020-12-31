def pow(x, y):
    if x == 0: return 0
    if y < 0:
        x = 1.0 / x
        y = -y
    res = 1
    while y > 0:
        res = res * x
        y = y - 1
    return res


print(f"{pow(x=int(input('Введите x ')), y=int(input('Введите y ')))}")
