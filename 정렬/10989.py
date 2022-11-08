import sys
n = int(sys.stdin.readline())
num_list = [0] * 10001

for _ in range(n):
    num_list[int(sys.stdin.readline())] += 1 

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)





'''
import sys
num_list = []

for _ in range(int(sys.stdin.readline())):
    num_list.append(int(sys.stdin.readline()))

num_list.sort()

for i in num_list:
    print(i)
'''