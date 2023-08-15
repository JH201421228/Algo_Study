import sys
sys.stdin = open('a.txt')
from itertools import permutations

# N개의 카드 중 K개를 선택하여 일렬로 나열 -> 순열 (nPk)
N = int(input())
K = int(input())
String = []
Final = set()
for _ in range(N):
    String.append(input())

# 중복을 고려해야 하므로 집합을 사용하자
for i in permutations(String, K):
    str = ''
    for k in i:
        str += k
    Final.add(str)
print(len(Final))