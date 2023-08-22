# 부분수열의 합
import sys
sys.stdin = open('1182.txt')

# 리스트 개수와 목표 합 작성, 리스트 받기
N, G = map(int, input().split())
numbers = list(map(int, input().split()))
cnt = 0

# 2**N 경우의 수를 순회하며
for i in range(1 << N):
    # 각 경우마다의 부분합을 구할것이며 더해갈 것이므로 0으로 설정하자
    mid = 0
    # 비트 연산을 통해 j번째 원소를 사용했는지 확인 (했다면 if 문으로, 아니면 비켜서 간다)
    for j in range(N):
        if i & (1 << j):
            mid += numbers[j]
    # 목표에 도달했다면 cnt를 1 증가 시키자(시작이 0이다보니 목표가 0이었다면 처음 공집합때 cnt가 1증가될 것)
    if mid == G:
        cnt += 1
if G == 0:
    print(cnt - 1)
else:
    print(cnt)