n = input()
alp = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in alp:
    n = n.replace(i,'*')

print(len(n))