#угадай слово
import random
WORDS = ("питон", "анаграмма", "простая", "сложная", "ответ", "подстаканник")
word = random.choice(WORDS)
correct = word
print("В слове", len(correct), "букв")
guess = ""
for i in range(5):
    print("Введите букву: ")
    guess = input()
    if guess in word:
        print("да")
    else:
        print("нет")
print("Напишите слово целиком: ")
answer = input()
if answer == word:
    print("YES")
else:
    print("loh")
