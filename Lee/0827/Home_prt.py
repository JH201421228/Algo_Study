import sys
sys.stdin = open('Home_prt.txt')
# k는 범위, i,j는 보드 인덱스
def search(k, i, j):
    global N
    global M
    global final
    hm_cnt = 0
    for m in range(-k+1, k):
        for n in range(-k+1+abs(m), k-abs(m)):
            if (0 <= i+m < N) and (0 <= j+n < N):
                hm_cnt += Board[i+m][j+n]
    local = []
    if hm_cnt*M >= k*k + (k-1)*(k-1):
        if hm_cnt >= final:
            final = hm_cnt

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Board = [list(map(int, input().split())) for _ in range(N)]
    final = 0

    # 보드를 순회하면서 어떤 범위를 줬을 때
    # 만족하는 경우가 있는지 확인하자.
    # 범위는 큰 것부터 작은 순서로 내려온다.
    # 최대는 N+1이 될 것이다.
    for k in range(N+1, 0, -1):
        for i in range(N):
            for j in range(N):
                search(k, i, j)
        if final != 0:
            break

    print(f'#{tc}', final)