#АНАГРАММА
import random
WORDS = ("питон", "анаграмма", "простая", "сложная", "ответ", "подстаканник")
word = random.choice(WORDS)
correct = word
jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position+1):]

print("Hello, если не знаешь ответ, пиши 'хз'")
print("Анаграмма: ", jumble)
count = 0
stat = 10
print("Первая попытка без штрафа")
guess = input("Пробуем: ")
while guess !=correct and guess != "":
    print("loh")
    guess = input("now again")
    if count == len(correct):
        print("Ну ты и лох")
        break
    if guess == "хз":
        print(count+1, "буква", correct[count])
        stat -= 1
        count += 1

print("Твои баллы:", stat)
