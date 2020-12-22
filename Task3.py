n = int(input("Введите n >>> "))
tmp = str(n)
tmp1 = tmp + tmp
tmp2 = tmp + tmp + tmp
sum = n + int(tmp1) + int(tmp2)
print(f"Сумма = {sum}")
