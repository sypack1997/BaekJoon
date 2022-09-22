n = int(input())
n_list = []

while n != 1:
    for i in range(2, n+1):
        if n % i == 0:
            n_list.append(i)
            n = n / i
            break
        else : 
            continue

print(n_list, end = '\n')