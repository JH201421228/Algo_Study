'''
문제구상
1. 중복 순열로 N과 같은 길이의 숫자 중 결과값 찾기
- > (dfs 순열에서 체크리스트를 빼 버리면 될듯?)
2. 1의 결과가 없으면 리스트 중 가장 큰 원소의 len(N)-1 의 size를 갖는 중복 숫자가 결과 값
'''
#N의 길이와 같은 size의 중복순열 생성
def permutation(L):
    global result
    if L == size:
        if int(''.join(num)) <= int(N):     #생성된 순열을 N과 비교하여 크거나 작을경우
            result = int(''.join(num))
            return result

    else:
        for i in range(int(K)):
            num[L] = nums[i]
            permutation(L+1)

N, K = input().split()
size = len(N)
nums = input().split()
nums.sort()         #오름차순을 통해 result에 조건을 만족하는 가장 큰 값이 마지막에 덮음
num = [0] * size    #각 순열 생성시 순열을 저장할 공간
result = 0
permutation(0)


if result == 0: #N과 같인 길이인 순열중 만족하는 결과 값이 없으면
    result = '' #Type에러 방지를 위해 빈 result 빈 문자열로 변경
    for i in range(size-1):
        result += nums[-1] #N보다 길이가 1 작은 수 중 가장 큰 값 출력
    print(int(result))
else:
    print(result)



