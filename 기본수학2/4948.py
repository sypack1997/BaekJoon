def prime_list(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

primes_list = list(range(2, 246912))
sosu = []

for i in primes_list:
    if prime_list(i):
        sosu.append(i)

while True:
    cnt = 0
    num = int(input())

    if num == 0:
        break
    for i in sosu:
        if num < i < 2*num+1:
            cnt+=1
    print(cnt)