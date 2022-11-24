n=int(input())

num=list(map(int,input().split()))
num_list=sorted(set(num))# 메모리관리를 위해 중복 값 삭제, sorted를 통해 num_list 값 정렬

dic={num_list[i]: i for i in range(len(num_list))}

for i in num:
    print(dic[i], end=' ')