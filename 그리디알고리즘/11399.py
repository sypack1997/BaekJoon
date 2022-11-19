n = int(input())
p = list(map(int,input().split()))

p = sorted(p)
result = 0
for i in range(n):
    for j in p[:i+1]:
        result += j

print(result)