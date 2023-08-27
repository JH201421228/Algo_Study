def backTracking(rowPos):
    global answer

    # 퀸을 모두 배치했다면 끝
    if rowPos == N:     
        answer += 1
        return

    for col in range(N):
        flag = True
        # 이전 행들에 대해서
        for row in range(rowPos):
            # 같은 열에 위치해있거나 대각선에 퀸이 이미 존재한다면 가지치기
            if queenLocation[row] == col or rowPos - row == abs(col - queenLocation[row]):
                flag = False
                break
        if flag:
            queenLocation[rowPos] = col
            backTracking(rowPos+1)


N = int(input())        # 체스판 크기
answer = 0              # 최종 경우의 수
# 각 row 마다 queen 이 위치하는 인덱스를 저장하는 리스트
queenLocation = [0]*N   # 각 인덱스번째 행의 퀸의 위치
backTracking(0)         # 0번째 행부터 출발
print(answer)