from itertools import combinations

# N 개 중 3개를 더하여 M에 가장 가깝지만 크지않은 정수 합 구하기
N, M = map(int, input().split())
Numbers = list(map(int, input().split()))
gauss = 0

# N개 중 3개를 선택하여 더하므로 조합(nC3)
for i in combinations(Numbers, 3):
    if (sum(i) <= M) and (sum(i) >= gauss):
        gauss = sum(i)
print(gauss)
