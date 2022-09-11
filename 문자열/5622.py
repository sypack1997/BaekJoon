n = input()
alp = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
num = 0

for i in range(len(n)):
    for j in alp:
        if n[i] in j:
            num += alp.index(j) +3

print(num)