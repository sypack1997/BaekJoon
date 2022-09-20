n = int(input())
a = list(map(int, input().split()))
cnt = 0

for i in a:
    error = 0
    if a == 1:
        continue
    for j in range(2, i+1):
        if i % j == 0:
            error +=1
    if error == 1:
        cnt += 1

print(cnt)