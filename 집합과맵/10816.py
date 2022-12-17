import sys
n = int(sys.stdin.readline())
card1 = list(map(str, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
card2 = list(map(str, sys.stdin.readline().split()))

result_list = {}
for i in card1:
    if i in result_list:
        result_list[i] += 1
    else:
        result_list[i] = 1

print(" ".join(str(result_list[i]) if i in result_list else "0" for i in card2))


''' 시간초과
import sys

n = int(sys.stdin.readline())
card1 = list(map(str, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
card2 = list(map(str, sys.stdin.readline().split()))

result = [str(card1.count(i)) for i in card2]

print(" ".join(result))
'''