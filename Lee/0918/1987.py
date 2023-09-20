import sys
sys.stdin = open('1987.txt')
input = sys.stdin.readline

# 델타 탐색
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


# DFS를 통해 거리도 재고 visited도 데려가자
# (i, j)까지 오는데 거리가 cnt고, 그까지 왔을 때 밟았던 알파벳 스트링이 visited
def DFS(i, j, cnt, visited):
    global final
    stack = [(i, j, cnt, visited)]
    while stack:
        now = stack.pop()
        for k in range(4):
            ni = now[0]+dx[k]
            nj = now[1]+dy[k]
            if 0<=ni<R and 0<=nj<C and Board[ni][nj] not in now[3]:
                dist = now[2] + 1
                if dist > final:
                    final = dist
                stack.append((ni, nj, dist, now[3]+Board[ni][nj]))



R, C = map(int, input().split())
Board = [list(input()) for _ in range(R)]
final = 1
visited = Board[0][0]

DFS(0, 0, 1, visited)
print(final)