t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())

    people = [i for i in range(1, n+1)]
    
    for f in range(k):
        for r in range(1, n):
            people[r] += people[r-1]
    
    print(people[n-1])