import sys
sys.stdin = open('input (11).txt')

Testcase = int(input())
for test in range(Testcase):
    Board = [list(map(int, input().split())) for _ in range(9)]
    check_list = []
    for i in range(9):
        check = True
        for j in range(1, 10):
            if j not in Board[i]:
                check = False
                break
        check_list.append(check)

    for i in range(9):
        col = []
        check = True
        for j in range(9):
            col.append(Board[j][i])
        for k in range(1, 10):
            if k not in col:
                check = False
                break
        check_list.append(check)

    for i in [0, 3, 6]:
        for j in [0, 3, 6]:
            box = []
            check = True
            for k in range(3):
                for l in range(3):
                    box.append(Board[i+k][j+l])
            for m in range(1, 10):
                if m not in box:
                    check = False
                    break
            check_list.append(check)

    if False in check_list:
        print(f'#{test+1}', 0)
    else:
        print(f'#{test+1}', 1)