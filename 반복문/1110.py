N = int(input())
n= 0
new = N

while True:
    a = new // 10
    b = new % 10
    c = (a+b) % 10
    new = (b*10) + c
    n +=1

    if N == new:
        break
print(n)