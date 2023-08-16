import sys
sys.stdin = open('input.txt')


def what_the(N, start):
    global ans
    global min_val

    if ans > min_val:
        return

    if len(arr) == N:

        if min_val > sum(arr):
            min_val = sum(arr)
            return
        else:
            return

    for i in range(N):
        if not y_index_info[i]:
            y_index_info[i] = 1
            arr.append(matrix[start][i])
            ans += matrix[start][i]
            start += 1
            what_the(N, start)
            y_index_info[i] = 0
            arr.pop()
            start -= 1
            ans -= matrix[start][i]


Test_Case = int(input())

for test_case in range(Test_Case):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    arr = []
    y_index_info = [0]*N
    min_val = 10*N
    ans = 0
    what_the(N, 0)
    print(f'#{test_case+1} {min_val}')