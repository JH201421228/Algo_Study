import sys
input = sys.stdin.readline

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def dfs(x, y):
    global max_len

    max_len = max(max_len, len(ans))
    for k in range(4):
        nx = x + di[k]
        ny = y + dj[k]
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] not in ans:
            ans.add(arr[nx][ny])
            dfs(nx, ny)
            ans.remove(arr[nx][ny])

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
ans = set()         # 아니 리스트는 안되고 set은 되는 이유? 중복제거때문에?
max_len = 0
ans.add(arr[0][0])
dfs(0, 0)
print(max_len)

# set => append == add
# pop or del == remove