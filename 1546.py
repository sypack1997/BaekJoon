N = int(input())
num = list(map(int,input().split()))
num2 = num.sort()

for i in range(N):
    num[i] = num[i] / num[N-1] * 100

print(sum(num[:]) / len(num))
