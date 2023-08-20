'''
문제구상
1. 조합으로 모든 조합의 수 만든 다음 조건에 맞는 조합 개수 추출
2. 조합은 DFS + Stack으로 구현
3. 조합은 현재 선택한 원소 뒤에 있는 원소들로 선택하면 됨(수기로 조합 만들때 생각해보기)
'''
def combination(nums, K):
    stack = [([num],i) for i,num in enumerate(nums)]            # 현재 선택한 마지막 원소 다음부터 순회하기 위해 튜플로 인덱스 번호 추출
    result = []
    while stack:
        num, idx = stack.pop()
        result.append(list(map(int,num)))
        for i in range(idx+1,N):                                # idx+1 == N 이 되면 에러가 아니고 범위가 빈걸로 되어 실행이 안되는 걸로 간주됨
            stack.append((num + [nums[i]], i))

    return result

N, M = map(int,input().split())
nums = input().split()

comb = combination(nums,3)
count = 0
for com in comb:
    if sum(com) == M:
        count += 1

print(count)







