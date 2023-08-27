import sys

sys.stdin = open('Return_room.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    visited = [0] * 201
    for i in range(N):
        p, q = map(int, input().split())
        if p > q:
            p, q = q, p
        if p % 2:
            p = p//2+1
        else:
            p = p//2
        if q % 2:
            q = q//2+1
        else:
            q = q//2
        for j in range(p, q+1):
            visited[j] += 1
    print(f'#{tc}', max(visited))