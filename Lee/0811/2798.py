from itertools import combinations

# N 개를 더하여 M에 가장 가깝지만 크지않은 정수 합 구하기
N, M = map(int, input().split())
Numbers = list(map(int, input().split()))
gauss = 0

for i in combinations(Numbers, 3):
    if sum(i) <= M and sum(i) >= gauss:
        gauss = sum(i)
print(gauss)