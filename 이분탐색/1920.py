n = int(input())
n_lst = set(map(int, input().split()))
print(n_lst)

m = int(input())
m_lst = list(map(int, input().split()))
print(m_lst)

for answer in m_lst:
    if answer in n_lst:
        print(1)
    else:
        print(0)