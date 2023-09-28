'''
설계
1. 크루스칼 알고리즘으로 최소 신장 트리 구하기
2. X,Y로 node가 주어 지지만 각 개별 리스트로 인풋이 주어지니까, 리스트 index로 그래프 컨트롤하기
3. 주어진 모든 노드들이 연결되어 있다고 생각하고 크루스칼 알고리즘 돌리기
'''

def cal_Len():                 # 모든 노드들이 연결되어 있다고 가정하고 모든 node들의 (거리값,x1,x2) 를 deque에 넣기
    for i in range(N-1):
        for j in range(i+1,N):
            dist = ((li_x[i] - li_x[j]) ** 2 + (li_y[i] - li_y[j]) ** 2) ** (1 / 2)
            q.append((dist,i,j))
    q.sort(reverse=True)
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
    N = int(input())
    parents = [0] * N
    q = []
    res = 0
    li_x = list(map(int,input().split()))
    li_y = list(map(int,input().split()))

    E = float(input())

    for i in range(N):
        parents[i] = i

    cal_Len()

    while q:
        dis, i1, i2 = q.pop()
        if find_parent(i1) == find_parent(i2):
            continue
        union(i1,i2)
        res += (E * (dis**2))
    res = int(round(res,0))
    print(f'#{test_case} {res}')
