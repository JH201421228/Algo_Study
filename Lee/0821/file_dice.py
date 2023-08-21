from copy import deepcopy
import sys
sys.stdin = open('a.txt')

# 순서대로 입력받아 주사위 정보를 이중리스트에 담기
N = int(input())
Dice_list_1 = []
for _ in range(N):
    a, c, e, d, f, b = map(int, input().split())
    Dice_list_1.append([a, b, c, d, e, f])

final = 0
# print(Dice_list_1)

# 가장 밑바닥을 정하면 축에 대한 모든 정보가 결정남
def dice(n):
    Dice_list = deepcopy(Dice_list_1)
    j = 0
    while j != N:
        K = Dice_list[j].index(n)
        if  K % 2 == 0:
            Dice_list[j].pop(K)
            n = Dice_list[j].pop(K)
        else:
            Dice_list[j].pop(K)
            n = Dice_list[j].pop(K-1)
        j += 1
    return Dice_list

# print(dice(1))
# print(dice(2))

for i in range(1, 7):
    Board = dice(i)
    mid = 0
    for j in range(N):
        mid += max(Board[j])
    if mid >= final:
        final = mid

print(final)