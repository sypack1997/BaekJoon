n= list(map(int,input().split()))

n.append(n[2]-n[0])
n.append(n[3]-n[1])

print(min(n))