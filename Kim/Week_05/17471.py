from collections import deque


def dfs(start, length, v):      # 조합 생성
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


def bfs(lst):               # 방문 가능한지 검증할 것
    q = deque()
    q.append(lst[0])
    v[lst[0]] = True
    cnt = 1
    while q:
        node = q.popleft()
        for j in graph[node]:
            if j in lst and not v[j]:       # 방문 횟수 == 그룹속 선거구 수
                v[j] = True                 # 방문 가능
                cnt += 1
                q.append(j)
        if cnt == len(lst):
            return True                     # 방문 가능하다면 True 반환
    return False    # 아니면 False

n = int(input())    # 선거구 갯수
people = list(map(int, input().split()))    # 선거구별 사람 수
graph = [[] for _ in range(n)]              # 인접 리스트
stack, section, lst, group1, group2 = [], [], [], [], []    # 조합리스트(임시), 조합리스트, 인원수차이, 그룹1, 그룹2
p = list(range(n))      # 선거구 번호
ans = float('inf')      # 정답 (최소값 구하려고 inf 넣어둠)
flag = False            # 선거구를 나눌 수 있는가?
for i in range(n):      # 인접 리스트 생성
    temp = list(map(int, input().split()))
    for j in range(temp[0]):
        graph[i].append(temp[j+1]-1)

visited_dfs = [False] * n   # dfs 즉 조합 생성시 사용할 방문리스트
for i in range(1, n // 2 + 1):
    dfs(0, i, visited_dfs)

for s in section:   # 각 조합 케이스 별로
    temp1 = 0       # 해당 조합 사람 수
    for j in range(len(s)):
        temp1 += people[s[j]]
    if (sum(people) - 2 * temp1) >= 0:      # 0보다 작은경우는 존재할 수 없음
        lst.append((sum(people) - 2 * temp1))   # 전체 사람수 - 2 * 1구역 사람 수 == 인원차이
        group1.append(s)        # 그룹 1
        temp2 = []
        for k in range(n):
            if p[k] not in s:
                temp2.append(p[k])
        group2.append(temp2)   # 그룹1에 안들어가면 무조건 그룹 2

# print(group1)
# print(group2)
# print(lst)
for i in range(len(group1)):
    v = [False] * n
    g1 = bfs(group1[i])
    g2 = bfs(group2[i])
    if g1 and g2:       # 둘다 방문 처리 가능하다면 두 선거구로 나눌 수 있다
        flag = True     # 선거구를 나눌 수 있다
        ans = min(ans, lst[i])  # 최소값 찾기

if flag:
    print(ans)
else:
    print(-1)
