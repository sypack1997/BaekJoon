N = int(input())

for i in range(N):
    a = input()
    score = 0
    score_sum = 0
    for j in a:
        if j == 'O':
            score +=1
        else:
            score = 0
        score_sum += score
    print(score_sum)