def prime_list(num):
    if num == 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            return False
    return True

T = int(input())

for i in range(T):
    n = int(input())
    a, b = n//2, n//2

    while a > 0:
        if prime_list(a) and prime_list(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1