from os import sep


n = int(input())
n_list = []

while n != 1:
    for i in range(2, n+1):
        if n % i == 0:
            n_list.append(i)
            n = int(n / i)
            break
        else : 
            continue
for i in n_list:
    print(i)



'''
other code
n = int(input) ; i = 2
while n != 1:
    if n % i == 0:
        print(i)
        n = n // i
    else:
        i += 1 
'''