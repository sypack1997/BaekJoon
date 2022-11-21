n = int(input())
name_list = {} # dict형태

for _ in range(n):
    name, check = input().split()

    if check == 'enter':
        name_list[name] = check # dict에 keys = 'name', value = 'check' 넣기
    else:
        del name_list[name]

name_list = sorted(name_list.keys(),reverse = True) # 키 값으로 정렬

for i in name_list:
    print(i)