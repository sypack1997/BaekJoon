n = int(input())
result = 0

for i in range(1, n):
    sum_i = i
    string_i = str(i)
    for j in string_i:
        sum_i += int(j)
    if sum_i == n:
        result = i
        break

print(result)