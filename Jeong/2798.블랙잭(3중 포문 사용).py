'''
문제구상
1. 3중포문 으로 가능한 모든 합 구하기
'''

N,M = map(int,input().split())
nums = list(set(list(map(int,input().split())))) #중복된 숫자 제거
result = []
for i in range(N-2): #첫 번째 고정수는 뒤에서 세번째 까지 순회
    for j in range(i+1, N-1): #두 번째 고정수는 첫 번째 고정수 다음 ~ 뒤에서 두번째 까지 순회
        for k in range(j+1, N): #세 번째 고정수는 두 번째 고정수 다음 ~ 마지막 까지 순회
            num = nums[i] + nums[j] + nums[k]
            if num <= M:
                result.append(num)

print(max(result))