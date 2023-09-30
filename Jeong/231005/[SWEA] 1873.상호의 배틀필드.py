'''
설계
1. 전차의 움직임과, shoot 2가지 함수 만들어서 처리하기
2. 현재 바라보는 방향을 숫자로 기록하여 기억하고 있기
'''


# 전차의 움직임을 di,dj로 반환하는 dictionary형성 , 숫자 부분은 shoot 함수에서 사용하기 위함
play = {
    'U' : [(-1,0),'^'],
    'R': [(0, 1),'>'],
    'D': [(1, 0),'v'],
    'L': [(0, -1),'<'],
    '^': 'U',
    '>': 'R',
    'v': 'D',
    '<': 'L'
}


def find_start():
    for i in range(H):
        for j in range(W):
            if Arr[i][j] in ('^', '>', 'v', '<'):
                dir_alpa = play[Arr[i][j]]
                return dir_alpa,i,j

def moving(dir_alpa,i,j):       # 전차의 움직임을 처리하는 함수
    di,dj = play[dir_alpa][0]
    ni,nj = i+di,j+dj

    if 0<=ni<H and 0<=nj<W:     # 해당하는 방향이 맵안에 있고,
        if Arr[ni][nj] == '.':  # 평지이면,
            Arr[i][j] = '.'     # 기존 위치를 평지로 바꾸고
            i,j = ni,nj         # 해당 위치로 이동


    Arr[i][j] = play[dir_alpa][1]   # 탱크가 위치하게 되는 곳에서 현재 바라보는 방향을 표시
    # if에 걸리지 않는 경우는 다른 연산 없이 함수 아래로 넘어 가므로 위에서 바뀐 dir_num과 기존의 i,j return 함
    return dir_alpa,i,j

def shoot(dir_alpa,i,j):
    flag = True
    di,dj = play[dir_alpa][0]      # 현재 바라보는 방향에 해당하는 delta 값

    while flag:
        ni, nj = i + di, j + dj
        if 0<=ni<H and 0<=nj<W:              # 슈팅 시 탄이 맵 내부에 있는 경우
            if Arr[ni][nj] in ['*','#']:     # 탄이 벽을 만나면
                if Arr[ni][nj] == '*':       # 벽돌벽은
                    Arr[ni][nj] = '.'       # 평지로 바꾸기
                    flag = False
                else:                        # 강철벽은 skip
                    flag = False
            else:                            # 맵 내부면서 벽이 아닌 경우는 계속 탐색
                i,j = ni,nj
        else:
            flag = False                    # 탄이 맵 밖으로 나가는 경우 함수 종료

T = int(input())
for test_case in range(1,T+1):
    H,W = map(int,input().split())
    Arr=[list(input()) for _ in range(H)]
    N = int(input())
    action = input()

    dir_alpa,i,j = find_start()


    for now in action:
        if now in ('U','R','D','L'):
            dir_alpa,i,j = moving(now,i,j)
        else:
            shoot(dir_alpa,i,j)


    print(f'#{test_case} ',end='')
    for row in Arr:
        for alpa in row:
            print(alpa,end='')
        print()