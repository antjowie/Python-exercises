import random


with open('sowpods.txt','r') as f:
    words = [word.strip() for word in f.readlines()]
    
word = words[random.randint(0,len(words)-1)]
print(word)