import math
T = int(input())

for i in range(T):
    H,W,N = map(int, input().split())
    if N % H == 0:
        floor = H
    else:
        floor = N % H
    room = N / H
    room_num = math.ceil(room)
    print(floor *100 + room_num)