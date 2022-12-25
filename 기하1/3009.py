a_list = []
b_list = []
for _ in range(3):
    a,b = list(map(int, input().split()))
    a_list.append(a)
    b_list.append(b)

for i in range(3):
    if a_list.count(a_list[i]) == 1:
        a_result = a_list[i]
    if b_list.count(b_list[i]) == 1:
        b_result = b_list[i]

print(a_result, b_result)