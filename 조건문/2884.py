H,M = map(int,input().split())

if M >= 45:
    M = M-45
elif M < 45:
    if H != 0:
        M = M+15
        H = H-1
    else:
        M = M+15
        H = 23

print(H, M)