# 계수정렬
import sys

n = int(sys.stdin.readline())
num_list = [0] * 10001

for i in range(n):
    k = int(sys.stdin.readline())
    num_list[k-1] += 1

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i+1)


 # 배열의 갯수가 많을 때 Sort를 사용하게되면 정렬과정에서 시간소모를 많이 일으킨다. 이에 계수정렬을 통해 순차적으로 배열의 값을 count하여 시간소모를 줄일 수 있다.
 # 하지만 계수정렬은 배열의 최대값이 매우 클때 메모리를 비효율적으로 사용하게 된다.
'''
 ex) 배열 [5,5231568]일 경우 숫자가 두개임에도 불구하고 5231568만큼의 count배열을 만들어 주기 때문에 메모리적으로 비효율적이다.
 또한 인덱스를 통하여 count해주기 때문에 음수값이 있다면 사용할 수 없다.
'''