import sys

n = int(sys.stdin.readline())
xy_list = []

for _ in range(n):
    x, y = list(map(int,sys.stdin.readline().split()))
    xy_list.append([y,x])

xy_list.sort()
for i in range(n):
    print(xy_list[i][1], xy_list[i][0])