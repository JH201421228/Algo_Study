def sudoku():  # 확실하게 채울 수 있는건 채우고, bt로 채우는 함수
    init()
    backtrack(0)


def backtrack(id):  # 백트래킹 함수
    # 2. 기저조건: 빈칸 다 채우면 end
    if id == len(zero_coor):
        return True

    # 3-1. 다음 박스로 진행해 가면서 할 작업
    x, y = zero_coor[id]

    # 1. 재귀 기본 구조(자기자신 호출)
    # 내꺼는 되면 다음칸 가기
    for num in range(1, 10):
        if is_valid(x, y, num):
            sudo[x][y] = num
            if backtrack(id + 1):
                return True
            # 위 if문에서 안걸림 = 다음칸에서 실패했다는것. 이 번호는 아닌가보다
            sudo[x][y] = 0  # 되돌리자
    return False


def init():  # 채울 수 있는건 채우는 함수
    zero_can = [set(i for i in range(1, 10)) for _ in range(len(zero_coor))]
    cnt = 0
    for x, y in zero_coor:
        for i in range(9):
            zero_can[cnt].discard(sudo[x][i])
            zero_can[cnt].discard(sudo[i][y])
        box_x, box_y = (x // 3) * 3, (y // 3) * 3
        for j in range(box_x, box_x + 3):
            for k in range(box_y, box_y + 3):
                zero_can[cnt].discard(sudo[j][k])
        cnt += 1
    print(zero_can)

    while not all(len(l) != 1 for l in zero_can):
        for i in range(len(zero_can)):
            if len(zero_can[i]) == 1:
                x, y, num = zero_coor[i][0], zero_coor[i][1], zero_can[i].pop()
                sudo[x][y] = num
                zero_can.pop(i)
                zero_coor.pop(i)
                update(x, y, num, zero_can)
                break


def update(x, y, n, lst):  # 확실하게 채울거 채우고나서 후보군 업데이트
    cnt = 0
    for nx, ny in zero_coor:
        if nx == x:
            lst[cnt].discard(n)
        if ny == y:
            lst[cnt].discard(n)
        if (x // 3 == nx // 3) and (y // 3 == ny // 3):
            lst[cnt].discard(n)
        cnt += 1


def is_valid(x, y, num):  # 유효성 검사 함수
    for i in range(9):
        if sudo[x][i] == num:
            return False
        if sudo[i][y] == num:
            return False

    box_x, box_y = (x // 3) * 3, (y // 3) * 3
    for i in range(box_x, box_x + 3):
        for j in range(box_y, box_y + 3):
            if sudo[i][j] == num:
                return False
    return True


sudo = [list(map(int, input().split())) for _ in range(9)]
zero_coor = []  # 비어있는 자리 튜플로 추가
# print(sudo)

for i in range(9):
    for j in range(9):
        if not sudo[i][j]:
            zero_coor.append((i, j))

print(zero_coor)

sudoku()
for i in sudo:
    print(*i)
