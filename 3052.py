a_list = []

for i in range(10):
    a_list.append(int(input()) % 42)

a = set(a_list)
print(len(a))



# len 함수 : 문자열의 길이 반환 / 내부에 있는 문자의 개수(공백포함) 계산
# count함수 : 문자열 내부에서 특정문자, 헉은 문자열이 포함되어있는지 계산해서 반환
a = 'Materials'
print(a.count('a')) # 2
print(a.count('k', 2, 6)) #  2 : index 시작 / 6 : index 끝