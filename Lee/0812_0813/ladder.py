import sys
from copy import deepcopy
sys.stdin = open('input (4).txt')

for _ in range(1):
    testcase = int(input())
    Board = [list(map(int, input().split())) for _ in range(10)]
    Copied = deepcopy(Board)
    start_list = []
    # 길을 찾는 로직
    # 첫 줄의 1 을 기준으로 1씩 내려갈 것
    # 아래 두 개를 만족하는 함수를 만들자
    # 좌/ 우 의 1 을 만나면 그 쪽으로 가자
    # 좌/ 우 의 방향이 정해지면 계속 그 방향으로 쭉 가다가 0을 만나면 다시 아래로
    # 2를 만나면 최종 종료

    # 먼저 1이 들어있는 출발선의 인덱스를 찾자
    for i in range(10):
        if Board[0][i] == 1:
            start_list.append(i)

