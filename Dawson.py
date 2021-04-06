number = int(input("Введите число от 1 до 100\n"))
print(number)
guess = 50
max = 100
min = 50
count = 1
print(guess)
while guess != number:
    if guess > number:
        print("less then", guess)
        max = guess
        guess = min//2
        print("new guess = ", guess)
    elif guess < number:
        print("more then", guess)

        guess = (max-guess)//2+guess
        min = guess
        print("new guess = ", guess)

    count += 1
print("you're right!, the number is", guess)
print("grats, you have", count, "tries")
