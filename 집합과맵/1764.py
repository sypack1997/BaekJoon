n, m = map(int, input().split())
n_list = []
m_list = []

for _ in range(n):
    name_n  = input()
    n_list.append(name_n)

for _ in range(m):
    name_m  = input()
    m_list.append(name_m)

nm_list = set(n_list) & set(m_list)
nm_list = sorted(nm_list)
print(len(nm_list))
for i in nm_list:
    print(i)


'''
n,m = map(int, input().split())

a = set()
for _ in range(n):
    a.add(input())

b = set()
for _ in range(m):
    b.add(input())

result = sorted(list(a&b))

print(len(result))
for i in result:
    print(i)
'''