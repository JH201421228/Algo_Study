from collections import deque
from itertools import combinations
import sys

sys.stdin = open('17471.txt')
input = sys.stdin.readline

# BFS를 돌면서 인구수를 세면서 나갈 것임
def BFS(L):
    Q = deque([L[0]])
    # visited를 set으로 설정하면 if 문 조건이 편함
    visited = set()
    visited.add(L[0])
    popu = population[L[0]]
    while Q:
        now = Q.popleft()
        for next in Adj[now]:
            # 방문한 적 없고 같은 집합 안에서만 BFS 돌린다.
            if next not in visited and next in L:
                Q.append(next)
                visited.add(next)
                popu += population[next]
    # 방문한 곳이랑 리스트 길이랑 같으면 다 연결되어 있다는 뜻
    if len(visited) != len(L):
        return 0
    return popu

# 노드 개수와 각 인구수 입력받기
N = int(input())
population = list(map(int, input().split()))
# 연결 정보 입력
Adj = [[] for _ in range(N)]
for i in range(N):
    a, *b = map(int, input().split())
    Adj[i].extend([k - 1 for k in b])
# print(Adj)
total = set(range(N))
answer = 10 ** 9

# 두 파트로 나누기(집합을 사용)
for r in range(1, N // 2 + 1):
    for c in combinations(range(N), r):
        A = (set(c))
        B = total - A
        A = list(A)
        B = list(B)
        print(A, B)
        # A와 B인구수를 입력 받는데 만약 연결되어 있지 않다면 0으로 리턴됨
        a_population = BFS(A)
        b_population = BFS(B)
        # 만약 둘 중 하나라도 0이 있다면 if 문을 통과하지 못할 것임
        if a_population and b_population:
            gap = abs(a_population - b_population)
            answer = min(answer, gap)

# 한 번도 if 문을 통과하지 않았다면 -1을 출력
if answer == 10 ** 9:
    print(-1)
else:
    print(answer)
