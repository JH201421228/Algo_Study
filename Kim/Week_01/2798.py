n, m = map(int, input().split())

lst = list(map(int, input().split()))

lst.sort(reverse=True)   # DESC

score_lst = []

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n): # 카드는 3장밖에 못고르니까 모든 경우 계산
            score = 0
            score += lst[i] + lst[j] + lst[k]
            score_lst.append(score)

score_lst.sort(reverse=True)
ans = 0

for i in score_lst:     # m을 넘지않는 최대값 구하기
    ans = i
    if i <= m:  
        break

print(ans)

# 5 21
# 5 6 7 8 9