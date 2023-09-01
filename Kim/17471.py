from collections import deque

def dfs(start, length, v):
    if len(stack) == length:
        section.append(stack[:])
        return

    for j in range(start, n):
        if not v[j]:
            v[j] = True
            stack.append(j)
            dfs(j, length, v)
            stack.pop()
            v[j] = False

def bfs(lst):
    q = deque()
    q.append(lst[0])
    v[lst[0]] = True
    cnt = 1
    while q:
        node = q.popleft()
        for j in graph[node]:
            if j in lst and not v[j]:
                v[j] = True
                cnt += 1
                q.append(j)
        if cnt == len(lst):
            return True
    return False

n = int(input())
people = list(map(int, input().split()))
graph = [[] for _ in range(n)]
stack, section, lst, group1, group2 = [], [], [], [], []
p = list(range(n))
ans = float('inf')
flag = False
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(temp[0]):
        graph[i].append(temp[j+1]-1)

visited_dfs = [False] * n
for i in range(1, n):
    dfs(0, i, visited_dfs)

for s in section:
    temp1 = 0
    for j in range(len(s)):
        temp1 += people[s[j]]
    if (sum(people) - 2 * temp1) >= 0:
        lst.append((sum(people) - 2 * temp1))
        group1.append(s)
        temp2 = []
        for k in range(n):
            if p[k] not in s:
                temp2.append(p[k])
        group2.append(temp2)

# print(group1)
# print(group2)
# print(lst)
for i in range(len(group1)):
    v = [False] * n
    g1 = bfs(group1[i])
    g2 = bfs(group2[i])
    if g1 and g2:
        flag = True
        ans = min(ans, lst[i])

if flag:
    print(ans)
else:
    print(-1)
