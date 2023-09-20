import sys
sys.stdin = open('hanaro.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    carte_x = list(map(int, input().split()))
    carte_y = list(map(int, input().split()))
    E = float(input())
    print(carte_x, carte_y, E)