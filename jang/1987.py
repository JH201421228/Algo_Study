import sys

direct = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def backtrack(x, y, cnt):
    global result
    if result < cnt:
        result = cnt

    # 알파벳 26개 다 돌면 더이상 조사 X
    if result == 26:
        print(26)
        exit(0)

    # 사방 돌면서 갈 수 있는지 없는지 조사
    for i in range(4):
        dx = x + direct[i][0]
        dy = y + direct[i][1]

        # 중복되지 않는 경우
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