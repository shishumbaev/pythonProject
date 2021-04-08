text = str(input())
print(len(text))
new_text = ""
for i in range(len(text)):
    new_text += text[-i-1]
print(new_text)