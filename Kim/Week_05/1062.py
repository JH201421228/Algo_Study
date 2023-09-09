import sys

base_char = ['a', 'n', 't', 'i', 'c']


def dfs(cnt, start, stack, lst, v):     # 조합 만드는 dfs
    if cnt == possible:
        combination.append(stack[:])
        return

    for i in range(start, len(lst)):
        if not v[i]:
            v[i] = True
            stack.append(lst[i])
            dfs(cnt + 1, i + 1, stack, lst, v)
            stack.pop()
            v[i] = False


N, K = map(int, sys.stdin.readline().split())
flag = True

if K <= 4:          # 가르칠수 있는 글자 수가 4개 이하면
    flag = False    # 완성시킬수 있는 글자가 1개도 없음

if flag:
    word = []
    possible = K - 5    # 기본 글자 5개 제외
    for _ in range(N):
        word.append(set(sys.stdin.readline().strip()))
    char_lst = set()    # 기본 글자 5개 제외한 글자 모음
    char = [[] for _ in range(N)]   # 기본글자 5개 제외한 단어

    for i in range(len(word)):
        for j in word[i]:
            if j not in base_char:
                char[i].append(j)
                char_lst.add(j)

    if len(char_lst) <= possible:   # 가르쳐야 하는 글자보다 가르칠 수 있는 글자가 더 많다면?
        print(N)                    # 모든 글자 읽을 수 있다
        exit(0)                     # 강제 종료

    combination = []
    visited = [False] * len(char_lst)
    dfs(0, 0, [], list(char_lst), visited)      # 가르칠 수 있는 글자 수(possible)로 이루어진 조합

    max_count = 0   # 최대 단어 개수
    for k in range(len(combination)):   # 조합 종류 수만큼
        cnt = 0             # 단어 개수 초기화
        if max_count == N:  # 만약 최대 개수 == 단어 개수
            break           # 이미 최대값 도달 = break (시간 단축)

        for i in range(len(char)):
            temp = 0        # 각 글자가 지금 참조하고 있는 조합글자에 포함 되어 있는가?
            for j in range(len(char[i])):
                if char[i][j] in combination[k]:
                    temp += 1       # 포함 되어 있다면 temp + 1
            if temp == len(char[i]):    # temp와 단어 길이가 같다면
                cnt += 1            # 읽을 수 있는 글자
        max_count = max(max_count, cnt) # 최대값 비교 (리스트에 다 넣고 비교하면 시간초과남)
    print(max_count)

else:       # K가 4보다 작으면 무조건 0
    print(0)