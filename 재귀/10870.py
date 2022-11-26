n = int(input())

F_list = [0, 1]

for i in range(2, n+1):
    F = F_list[i-1] + F_list[i-2]
    F_list.append(F)

print(F_list[n])