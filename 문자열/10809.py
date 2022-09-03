n = input()
word = list(range(97,123))

for i in word:
    print(n.find(chr(i)), end = ' ')