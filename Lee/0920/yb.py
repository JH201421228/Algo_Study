# 쓰거나 안쓰거나 그렇게 가보자

di = [[-1, -1, 0], [-1, -1, 0]]
dj = [[-1, 0, -1], [0, 1, 1]]


# 2*2 사각형이 있는지 확인하기
def check_nemo(i, j):
    # 첫째 행, 열은 검사할 필요없음
    if i == 0 or j == 0:
        return False
    for k in range(2):
        cnt = 0
        for dk in range(3):
            ni = i + di[k][dk]
            nj = j + dj[k][dk]
            if 0 <= ni < N and 0 <= nj < M:
                # 넴모가 없으면
                if arr[ni][nj] == 0:
                    continue
                # 아니면 카운트
                cnt += 1
                if cnt == 3:
                    return True
    return False


def put_nemo(now_i, now_j):
    global ans
    print('now', now_i, now_j)
    # 이게 마지막 칸이면 카운트 올리고 종료
    if now_i == N:
        ans += 1
        print(arr)
        return

    is_end = False

    for i in range(now_i, N):
        for j in range(M):
            # 방문했으면 다음칸 조사
            if visited[i][j] == 1:
                continue
            # 이 칸에 넴모를 놓는 경우
            # print('i, j', i, j)
            visited[i][j] = 1
            arr[i][j] = 1
            # 첫째 행, 열은 검사할 필요없음
            is_end = check_nemo(i, j)
            print(is_end, i, j)
            # 검사해서 네모다? 그럼 중지
            # 이걸 여기서 하면 여기에 넴모 안놓는 경우를 조사안해서 그런것 같은디?
            # [[0,0], [1,0]] , [[0,0],[0,1]] 이런애들 없음
            # is_end를 전달해주는 식으로 바꾸면 될것같은데 잘 안바꿔짐..ㅜ
            if is_end:
                return
            # 함수 드가자
            # 끝에 도달했으면
            if j == M - 1:
                # 다음행 조사
                # print('a', i+1, 0)
                put_nemo(i + 1, 0)
            else:
                # 아니면 다음칸 조사
                # print('b', i, j+1)
                put_nemo(i, j + 1)

            # 넴모 안놓는 경우
            arr[i][j] = 0
            if j == M - 1:
                # print('c', i+1, 0)
                put_nemo(i + 1, 0)
            else:
                # print('d', i, j+1)
                put_nemo(i, j + 1)
            visited[i][j] = 0


N, M = map(int, input().split())

arr = [[0] * M for _ in range(N)]

visited = [[0] * M for _ in range(N)]

ans = 0

if N == 1:
    print(2 ** M)
elif M == 1:
    print(2 ** N)
else:
    # 판별해서 개수 프린트
    put_nemo(0, 0)

    print(ans)