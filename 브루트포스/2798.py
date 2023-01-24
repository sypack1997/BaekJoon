a, b  =  map(int,input().split())
num = list(map(int,input().split()))
sum_list = []

for i in range(a):
    for j in range(i+1, a):
        for k in range(j+1, a):
            sum = num[i] + num[j] + num[k]
            if sum <= b:
                sum_list.append(sum)

sum_list = sorted(sum_list)
print(sum_list[-1])
