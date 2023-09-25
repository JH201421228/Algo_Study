import sys
sys.stdin = open('youngjun.txt')

# 두 수가 같은 집합 안에 있는지 확인하는 함수
def can_cal(n, m):
    while n != parents[n] or m != parents[m]:
        n = parents[n]
        m = parents[m]
    if n == m:
        return n
    else:
        return False

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    parents = list(range(N+1))
    distance = [dict() for _ in range(N+1)]
    print(f'#{tc}', end=' ')
    for _ in range(M):
        a, *b = list(input().split())
        b = list(map(int, b))
        if a == '!':
            parents[b[0]] = b[1]
            distance[b[0]][b[1]] = b[2]
        else:
            s = b[0]
            g = b[1]
            if can_cal(s, g):
                acc = 0
                while s != can_cal(s, g):
                    acc += distance[s][parents[s]]
                    s = parents[s]
                while g != can_cal(s, g):
                    acc -= distance[g][parents[g]]
                    g = parents[g]
                # 양 쪽에서 만나야?
                # 1이 4랑 만나려면 1도 3으로 4도 3으로 와야한다
                print(acc, end=' ')
            else:
                print('UNKNOWN', end=' ')
    print()
    # print(parents)
    # print(distance)