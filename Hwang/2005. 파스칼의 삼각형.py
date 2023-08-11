T = int(input())

def SUM(x, y):
    if x == 0 or y == 0:
        arr[x][y] = 1

    else:
        arr[x][y] = arr[x - 1][y - 1] + arr[x - 1][y]
    return arr[x][y]

for t in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i < j:
                continue
            else:
                SUM(i, j)

    print(*arr[i][j+1])

    # filtered_arr = [[value for value in row if value != 0] for row in arr]
    #
    # print(f'#{t}')
    # for row in filtered_arr:
    #     for element in row:
    #         print(element, end=' ')
    #     print()