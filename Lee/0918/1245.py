from collections import deque
import sys
sys.stdin = open('1245.txt')
input = sys.stdin.readline

# 델타 탐색(8방향 -> 다이얼 방향(12369874)
di = [-1, -1, -1, 0, 1, 1, 1, 0]
dj = [-1, 0, 1, 1, 1, 0, -1, -1]

# Check 함수(8방향에 더 큰 수가 존재하는가?) -> 존재하면 False , 없다면 True, 같은 애들은 리스트로 반환
def check(i, j):
    center = Board[i][j]
    more = []
    for k in range(8):
        ni = i + di[k]
        nj = j + dj[k]
        if ni>=N or ni<0 or nj>=M or nj<0:
            continue
        if visited[ni][nj] == 0:
            if Board[ni][nj] > center:
                return False
            elif Board[ni][nj] < center:
                visited[ni][nj] = 1
            else:
                more.append((ni, nj))
                visited[ni][nj] = 1
        else:
            continue
    if more:
        return more
    else:
        return True

def BFS(i, j):
    global cnt
    Q = deque([(i, j)])
    while Q:
        now = Q.popleft()
        A = check(now[0], now[1])
        if A == True:
            continue
        elif type(A)== bool:
            cnt += 1
        elif type(A)==list:
            Q.extend(A)




N, M = map(int, input().split())
Board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(M):
        if visited[i][j] == 1:
            continue
        else:
            BFS(i, j)
print(cnt)



# 1. 완전탐색(이중포문)

# 2. 주변과 비교하여 더 큰 친구가 있는가?
# 2-(큰 애가 있다). Continue
# 2-(같은 애가 있다.) 탐색을 끝낸 후 같은 애도 2번을 적용
# 2-(작은애들 뿐이다.) cnt += 1

# 3. 함수 구성
# 3-1. check 함수(주변에 큰 친구가 있는가?)
# 3-2. BFS 함수(주변에 같은 친구가 나오면 Q에 넣고 다시 check)
