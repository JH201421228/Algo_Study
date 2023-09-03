def dfs(length, start, ans, visited):   # 부분수열 길이, 탐색 시작위치, 부분합, 방문리스트
    if length == cnt:                   # 각 길이별 부분수열 (1~n까지)
        my_lst.append(ans)              # 부분수열 길이 맞으면 list에 추가
        return

    for j in range(start, n):           # 중복 피하기 위해서 시작 위치 계속 변경
        if not visited[j]:
            visited[j] = True
            dfs(length+1, j + 1, ans+arr[j], visited)   # 1개 추가했으니까 length +1
            visited[j] = False                          # j번째까지 봤으니까 다음은 j +1부터
                                                        # arr[j]를 부분합에 추가


n, s = map(int, input().split())
arr = list(map(int, input().split()))
v = [False] * n
my_lst = []

for i in range(1, n+1):     # 부분수열 길이
    cnt = i
    dfs(0, 0, 0, v)         # 함수 호출(부분수열길이, 탐색시작위치, 부분합, 방문리스트)

print(my_lst.count(s))      # 원하는 값이 몇개가 나오는가?
print(my_lst)