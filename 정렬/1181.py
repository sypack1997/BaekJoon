n  = int(input())
word_list = []

for _ in range(n):
    word_list.append(input())

result = list(set(word_list))
result.sort()
result.sort(key = len)

for i in result:
    print(i)