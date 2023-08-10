import sys
sys.stdin = open('a.txt')
from itertools import permutations

N = int(input())
K = int(input())
String = []
Final = set()
for _ in range(N):
    String.append(input())

# print(String)
for i in permutations(String, K):
    str = ''
    for k in i:
        str += k
    Final.add(str)
print(len(Final))