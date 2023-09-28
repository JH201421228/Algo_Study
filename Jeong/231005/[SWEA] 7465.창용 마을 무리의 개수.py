'''
설계
1. 유니온 파인드로 집합 갯수 찾기
'''

def find_parent(x):
    if parents[x] != x:
        parents[x] = find_parent(parents[x])
    return parents[x]

def union(a,b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b


T = int(input())
for test_case in range(1,T+1):
    N, M = map(int,input().split())
    parents=[0] * (N+1)

    for i in range(N+1):
        parents[i] = i


    for _ in range(M):
        a,b = map(int,input().split())
        union(a,b)

    for i in range(1,N+1):      #무리와 무리가 만나는 node가 마지막 input이 되면 갱신이 안되므로 전체 갱신
        find_parent(i)

    res = len(set(parents))-1   # 0번 노드는 없으므로 1 빼기

    print(f'#{test_case} {res}')
