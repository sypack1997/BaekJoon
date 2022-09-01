a = list(map(int, input().split()))

a[0] = 1 - a[0]
a[1] = 1 - a[1]
a[2] = 2 - a[2]
a[3] = 2 - a[3]
a[4] = 2 - a[4]
a[5] = 8 - a[5]

for i in range(6):
    print(a[i], end = ' ')


# other code
chess = [1, 1, 2, 2, 2, 2, 8]
a = list(map(int, input().split()))

for i in range(6):
    print(chess[i] - a[i], end = ' ')