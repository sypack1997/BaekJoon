m = int(input())
n = int(input())
num_list = []

for i in range(m, n+1):
    error = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                error += 1
                break
        if error == 0:
            num_list.append(i)

if len(num_list) > 0:
    print(sum(num_list))
    print(min(num_list))
else:
    print(-1)