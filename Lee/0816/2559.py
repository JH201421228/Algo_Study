import sys
sys.stdin = open('a.txt')

# 시간을 단축하려고 쇼를 함
N, M = map(int, input().split())
temp = list(map(int, sys.stdin.readline().split()))
# 처음 M개의 합을 기본으로 설정하고 최종 값도 일단 걔로 설정
mid_sum = sum(temp[:M])
final = mid_sum
i = 0
# 이제 리스트를 순회하면서 젤 앞에 있는 친구 빼고 가장 가까운 새친구 넣어서 합을 초기화
while i != N-M:
    mid_sum -= temp[i]
    mid_sum += temp[M+i]
    if final <= mid_sum:
        final = mid_sum
    i += 1

print(final)