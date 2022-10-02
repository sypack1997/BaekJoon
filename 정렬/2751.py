import sys

n = int(sys.stdin.readline())
num_list = []

for i in range(n):
    num = int(sys.stdin.readline())
    num_list.append(num)

num_list.sort()
for i in num_list:
    print(i)