start, finish, interval = input("Введите начальное и конечное значения, а так же интервал:\n").split()
print("Начало счета:", start, "Конец счета:", finish, "Интервал:", interval)
for i in range(int(start),int(finish),int(interval)):
    print(i)