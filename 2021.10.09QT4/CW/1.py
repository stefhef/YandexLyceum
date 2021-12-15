import random


f = open('lines.txt', encoding='UTF-8')
text = f.readlines()
f.close()
if text:
    print(random.choice(text))
