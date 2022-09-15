import math
a,b,v = map(int,input().split())
day = (v-b) / (a-b)
print(math.ceil(day))






# 시간초과
'''
a,b,v = map(int,input().split())
cnt = 0
sum = 0

while sum < v:
    cnt +=1
    sum = sum + a
    if sum >= v:
        break 
    sum = sum - b

print(cnt)
'''