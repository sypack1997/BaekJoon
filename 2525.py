a,b = map(int, input().split())
c = int(input())

if (b+c) >= 60:
    if (b+c) % 60 == 0:
        d = (b+c) // 60
        a = a+d
        if a // 24 >= 1:
            a = a % 24
        b =0
        print(a,b)
    else:
        a = a + ((b+c) // 60)
        if a // 24 >=1:
            a = a % 24
        b = (b+c) % 60
        print(a,b)

elif (b+c) <60:
    print(a,(b+c))




# other code
a,b = map(int, input().split())
c = int(input())

a += c//60
b += c %60

if b >=60:
    a +=1
if a >= 24:
    a-=24

print(a,b)