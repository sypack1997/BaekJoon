n = input().upper()
n_list = list(set(n))
cnt = []

for i in n_list:
    n_cnt = n.count(i)
    cnt.append(n_cnt)

if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(n_list[cnt.index(max(cnt))])