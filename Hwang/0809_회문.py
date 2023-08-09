T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    Next_arr = [[arr[j][i] for j in range(N)] for i in range(N)]

    for i in range(N):
        for j in range(N - M + 1):
            if arr[i][j:j + M + 1] == arr[i][j:j + M + 1][::-1]:
                result = arr[i][j:j + M + 1]
            if Next_arr[i][j:j + M + 1] == Next_arr[i][j:j + M + 1][::-1]:
                result = Next_arr[i][j:j + M + 1]

    print(f'#{t} ', *result, sep="")