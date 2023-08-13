'''
문제구상
1. 나열된 카드중 k개 원소를 가지는 순열 형성(DFS 이용)
2. 완성된 순열들을 set에 담아서 중복숫자 제거
'''

def dfs(L) :                        #L은 만들고자 하는 순열요소의 자리 위치를 의미함
    if L == k:                      #만들고자 하는 순열 요소 갯수가 k개가 됐을 경우
        result.add(''.join(num))
    else:
        for i in range(n):
            if not checklist[i]:    #해당 숫자를 아직 사용하지 않았으면
                checklist[i] = 1    #해당 숫자를 사용 처리하고
                num[L] = nums[i]    #순열에 해당 숫자를 반영
                dfs(L+1)            #순열 다음 위치로 dfs 반복
                checklist[i] = 0    #dfs 재귀함수가 끝나고 돌아오면서 checklist i 를 0으로 만들어야 다른 순열에 해당 숫자를 사용 가능함

n = int(input())
k = int(input())
nums = [input() for _ in range(n)]
checklist = [0] * n     #각 요소를 사용했는지 여부를 확인하는 리스트
num = [0] * k           #각 순열의 값을 담을 리스트
result = set()          #완성된 모든 순열을 담을 세트
dfs(0)
print(len(result))



