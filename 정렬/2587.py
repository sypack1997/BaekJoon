n_list = []

for i in range(5):
    n = int(input())
    n_list.append(n)

print(int(sum(n_list) / 5))
print(sorted(n_list)[2])