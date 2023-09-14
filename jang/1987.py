import sys

direct = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def backtrack(x, y, cnt):
    global result
    if result < cnt:
        result = cnt
    if result == 26:
        print(26)
        exit(0)
    for i in range(4):
        dx = x + direct[i][0]
        dy = y + direct[i][1]
        if 0 <= dx < R and 0 <= dy < C and MAP[dx][dy] not in char:
            char.add(MAP[dx][dy])
            backtrack(dx, dy, cnt + 1)
            char.remove(MAP[dx][dy])


R, C = map(int, sys.stdin.readline().strip().split())
MAP = []
for _ in range(R):
    word = sys.stdin.readline().strip()
    num = [ord(w) for w in word]
    MAP.append(num)
char = set()
char.add(MAP[0][0])
result = 0
backtrack(0, 0, 1)
print(result)