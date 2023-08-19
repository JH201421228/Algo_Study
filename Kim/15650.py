n, m = map(int, input().split())
s = []
v = [False] * (n+1)

def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(start, n+1):     # start부터 시작
        if i not in s:
                s.append(i)
                dfs(i)
                s.pop()

dfs(1)