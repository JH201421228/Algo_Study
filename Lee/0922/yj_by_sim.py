import sys
sys.stdin = open('youngjun.txt')

# 같은 집합인지 확인
def find(x):
    if x == parent[x]:
        return x, 0
    px, pd = find(parent[x])
    parent[x] = px
    diff[x] += pd
    return parent[x], diff[x]


def union(a, b, w):
    pa, da = find(a)
    pb, db = find(b)

    if pa != pb:
        if rank[pa] > rank[pb]:
            parent[pb] = pa
            diff[pb] = da - db + w
        else:
            parent[pa] = pb
            diff[pa] = db - da - w
            if rank[pa] == rank[pb]:
                rank[pb] += 1


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    parent = [i for i in range(N + 1)]
    diff = [0 for i in range(N + 1)]
    rank = [0 for i in range(N + 1)]

    results = []

    for _ in range(M):
        query = input().split()
        if query[0] == "!":
            a, b, w = map(int, query[1:])
            union(a, b, w)
        else:
            a, b = map(int, query[1:])
            pa, da = find(a)
            pb, db = find(b)
            if pa == pb:
                results.append(db - da)
            else:
                results.append("UNKNOWN")

    print(f"#{tc}", *results)