'''
설계
1. 다익스트라로 각 노드에서 X번 노드에 갈 때 최단거리 계산
    - X번 노드 까지 거리 확정 시 추가 탐색 없이 함수 종료 되도록 하기
2. 다익스트라로 X 노드에서 각 노드까지의 전체 최단거리 테이블 작성
'''
import heapq


def go_daik(i):
    heap = [(0, i)]
    distance = [int(1e9)] * (N + 1)
    distance[0] = distance[i] = 0

    while heap:
        dist, now_node = heapq.heappop(heap)  # 힙을 사용하므로 now_node == 방문 노드가 되는거임
        if now_node == X:  # 갈 때는 X 노드 까지의 최단거리가 확정되면 함수 종료
            return distance[X]

        if distance[now_node] < dist:  # 이 부분에서 q에 남아있는 최단거리가 아니 였던 부분들이 다 처리됨
            continue

        for next_node in Arr[now_node]:
            cost = dist + next_node[1]
            if cost < distance[next_node[0]]:
                distance[next_node[0]] = cost
                heapq.heappush(heap, (cost, next_node[0]))


def back_daik(i):
    heap = [(0, i)]
    distance = [int(1e9)] * (N + 1)
    distance[0] = distance[i] = 0

    while heap:
        dist, now_node = heapq.heappop(heap)
        if distance[now_node] < dist:
            continue

        for next_node in Arr[now_node]:
            cost = dist + next_node[1]
            if cost < distance[next_node[0]]:
                distance[next_node[0]] = cost
                heapq.heappush(heap, (cost, next_node[0]))
    return distance


T = int(input())
for test_case in range(1, T + 1):
    N, M, X = map(int, input().split())

    Arr = [[] for _ in range(N + 1)]
    min_ls = [0] * (N + 1)

    for _ in range(M):
        a, b, c = map(int, input().split())
        Arr[a].append((b, c))

    # 각 노드별 X번으로 가는 최단 거리 계산
    for i in range(1, N + 1):
        go_res = go_daik(i)
        if go_res:
            min_ls[i] += go_res

    # X번에서 각 노드로 가는 최단 거리 계산
    back_res = back_daik(X)
    for i in range(1, N + 1):
        min_ls[i] += back_res[i]

    print(f'#{test_case} {max(min_ls)}')