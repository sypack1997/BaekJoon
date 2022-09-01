C = int(input())

for i in range(C):
    N = list(map(int, input().split()))
    cnt = 0
    for j in N[1:]:
        sum_N = sum(N[1:])
        len_N = len(N[1:])
        avg_N = sum_N / len_N
        if j > avg_N:
            cnt += 1
    print(format(cnt / len_N * 100, ".3f")+"%")




# other code
avg_N = sum(N[1:]) / N[0]
print(f'{cnt / N[0] * 100:.3f}%') # print(f'~~{숫자}~~') 형식으로 사용 / 숫자뒤에 :.자릿수f를 사용하여 원하는 자릿수 출력