'''
설계
1. 그래프상 5명 이상의 사람이 일렬로(?) 연결되어 있으면 1, 아니면 0을 출력
2. dfs 매개변수로 cnt+1를 던지면서 dfs 깊이가 4(깊이 0부터 시작)가 되면 dfs 종료
3. dfs 구조상 시작 node에 따라 깊이가 다르므로 모든 노드를 시작점으로 다 탐색해보기
'''
def dfs(L, cnt):
    global result
    if cnt == 4:
        result = 1
        return True

    visited[L] = 1
    for next in Arr[L]:
        if not visited[next]:
            if dfs(next, cnt+1):       # 그래프 깊이가 4가되면 호출된 재귀 함수가 연속적으로 True를 반환하고 함수 종료
                return True
    visited[L] = 0
    return False

N, M = map(int, input().split())
Arr = [[] for _ in range(N)]
visited = [0] * N

for _ in range(M):
    p1, p2 = map(int, input().split())
    Arr[p1].append(p2)
    Arr[p2].append(p1)

result = 0
for i in range(N):
    if dfs(i, 0):
        result = 1
        break

print(result)
