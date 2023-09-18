from collections import deque
import sys
sys.stdin = open('1240.txt')
input = sys.stdin.readline

def BFS(start, goal):
    visited = [0]*(N+1)
    # Q에 넣을 때 (위치, 쌓인 거리)로 넣을 것
    # (5, 10): 5까지 오는데 10이 걸렸다는 의미
    # (시작점, 0)으로 시작
    Q = deque([(start,0)])
    while Q:
        # 언패킹 목적지, 쌓인 거리
        now, dist = Q.popleft()
        # 방문 표시
        visited[now] = 1
        # 갈 수 있는 곳을 찾음(여기서의 next는 튜플 형태)
        for next in adj[now]:
            # 방문한 적이 없다면
            if visited[next[0]] == 0:
                # 다음 목적지와, 그 목적지까지의 거리를 튜플로 큐에 추가
                Q.append((next[0], dist+next[1]))
                # 만약 도착했다면 거리를 반환(만약 못가는 문제라면 조건 추가)
                if next[0] == goal:
                    return dist+next[1]


N, M = map(int, input().split())
# 연결 정보를 연결리스트로 표현(인접행렬에 비해 빠름)
# 그런데 간선에 가중치가 있기 때문에 튜플의 형태로 저장
# (5, 3) 은 5까지의 거리가 3이라는 의미
adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))
    adj[b].append((a, c))
print(adj)


for _ in range(M):
    d, e = map(int, input().split())
    print(BFS(d, e))