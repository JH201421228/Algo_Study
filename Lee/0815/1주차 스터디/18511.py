from itertools import product

# N개 중 중복을 허용하여 K개를 뽑고 나열 -> 중복 순열(n파이k) = n**k
N, n = input().split()
Number = set(input().split())  # 중복을 허용하므로 집합 사용
List = []


# 모든 경우의 수 확인하여
for j in range(len(N)):
    for i in product(Number, repeat=len(N)-j):
        '''
        str = ''
        for k in i:
            str += k
        if int(N) >= int(str):
            List.append(int(str))
        else:
            continue
            '''
        print(i)
    # 최댓값 출력
print(max(List))
