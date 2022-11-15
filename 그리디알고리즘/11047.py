n, k = map(int,input().split())
coin_list = []

for _ in range(n):
    coin_list.append(int(input()))

cnt = 0
for i in reversed(range(n)):
    if k == 0:
        break
    if k//coin_list[i] > 0:
        cnt += k//coin_list[i]
        k = k%coin_list[i]
print(cnt)