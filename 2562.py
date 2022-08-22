a_list = []
while True:
    try:
        a = int(input())
        a_list.append(a)
    except:
        break

print(max(a_list), a_list.index(max(a_list)) + 1, sep = "\n")




# other code
num_list = []
for  i in range(9):
    num_list.append(int(input()))

print(max(num_list))
print(num_list.index(max(num_list)) + 1)