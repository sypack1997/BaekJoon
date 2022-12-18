n = input()
n_list = []

for i in range(len(n)):
    for j in range(i, len(n)):
        n_list.append(n[i:j+1])

print(len(set(n_list)))
