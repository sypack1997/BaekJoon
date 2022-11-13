import sys

n = int(sys.stdin.readline())
xy_list = []

for _ in range(n):
    x, y = list(map(int,sys.stdin.readline().split()))
    xy_list.append([x,y])

xy_list.sort()

for i in range(n):
    print(xy_list[i][0], xy_list[i][1])