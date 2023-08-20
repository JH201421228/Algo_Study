'''
문제구상
1. 나열된 원소중 원소 3개 짜리 부분 집합 형성 하여 sum
'''

N,M = map(int,input().split())
nums = list(map(int,input().split()))

#원소 3개짜리 부분집합 생성
part_ls = []

for i in range(1<<N):
    part = []
    if bin(i).count('1') == 3:
        for j in range(N):
            if i & (1<<j):
                part.append(nums[j])
        part_ls.append(part)

#각 부분 집합별 합 구하기 + M에 가장 가까운 수 구하기
result = []
for num in part_ls:
    total = sum(num)
    if total <= M: #합 중에 M과 같거나 작은수만 저장
        result.append(total)

print(max(result))
