def d(n):
    n = n + sum(map(int,str(n)))
    return n

nonSelfNum = set()

for i in range(1, 10001):
    nonSelfNum.add(d(i))

for i in range(1,10001):
    if i not in nonSelfNum:
        print(i)