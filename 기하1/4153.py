while True:
    a, b, c = sorted(list(map(int,input().split())))
    if a == 0:
        break

    if c**2 == b**2 + a**2:
        print("right")
    else : 
        print("wrong")