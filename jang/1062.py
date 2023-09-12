import sys

# 순열로 필요한 문자(need_char) 중 need_cnt 만큼 뽑아서 select_lst에 모두 담기
def select_char(n, cnt):
    if cnt == need_cnt:
        select_lst.append(list(char)[:])
        return
    if n >= len(need_char):
        return
    char.add(need_char[n])
    select_char(n+1, cnt+1)
    char.remove(need_char[n])
    select_char(n+1, cnt)

N, K = map(int, sys.stdin.readline().strip().split())
words = [sys.stdin.readline().strip() for _ in range(N)]

# 무조건 필요한 단어 anta-tica => a n t i c
char = {'a', 'n', 't', 'i', 'c'}
need_char = set()

# a n t i c 제외하고 새롭게 배울 수 있는 단어의 수
need_cnt = K - 5

# anta-tica 도 못 배운다면 배울 수 있는 단어 존재 X
if need_cnt < 0:
    print(0)
    exit(0)
else:
    # 새롭게 배워야 하는 단어 (a n t i c 제외) need_char에 넣기
    for word in words:
        for w in word:
            if w not in char:
                need_char.add(w)

    need_char = list(need_char)

    # 새롭게 배워야 할 모든 단어의 수 == 새롭게 배울 수 있는 단어의 수이면 모든 단어 배울 수 있음
    if len(need_char) < need_cnt:
        print(len(words))
        exit(0)



    select_lst = []
    select_char(0, 0)

    result = 0

    # select_lst 돌면서 배울 수 있는 단어 수 찾기
    for select in select_lst:
        result_cnt = 0
        for word in words:
            word_cnt = 1
            for w in word:
                # 문자열 돌면서 만약 select에 포함되지 않은 단어가 존재하면 word_cnt 0 대입 후 break
                if w not in select:
                    word_cnt = 0
                    break
            result_cnt += word_cnt
        # 최댓값 갱신
        if result < result_cnt:
            result = result_cnt

    print(result)
