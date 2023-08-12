'''
문제구상
1. 나열된 카드중 k개 원소를 가지는 부분집합 형성(비트연산자)
2. 부분집합 별 숫자 조합하기(순열)
3. 중복 숫자 제거(set이용)

개선점
1. 굳이 부분집합 형성 없이 바로 전체 카드 중 k개를 뽑아 순열로 만드는게 효율적일듯?
'''

n= int(input())
k = int(input())
nums = [int(input()) for _ in range(n)]

nums = list(set(nums)) #input 값의 중복된 숫자 제거
n = len(nums) #중복된 input값이 제거된 새로운 리스트의 길이 할당

result = [] # 원소의 갯수가 k개인 부분 집합을 담을 리스트

#원소의 갯수가 k개인 부분 집합 구하기
for i in range(1<<n):               # nums의 가능한 부분집합
    part_ls = []                    #result에 append하기 전 담을 list 생성
    if (bin(i).count('1') == k):    #원소의 개수가 k(이진수의 1이 k개)인 부분 집합 비교군 일 때만
        for j in range(n):
            if (i & (1<<j)):        #이진수 1에 해당 하는 원소 추출
                part_ls.append(nums[j])
        result.append(part_ls)
    else:
        continue

#각 부분집합 별 순열 생성하기
