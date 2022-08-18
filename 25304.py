X = int(input())
N = int(input())
c = 0
for i in range(N):
    a,b = map(int,input().split())
    d = a*b
    c +=d
if X ==c:
    print("Yes")
else:
    print("No")