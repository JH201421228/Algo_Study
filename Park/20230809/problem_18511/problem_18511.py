import sys
from itertools import permutations
# sys.stdin = open('input.txt')

N, K_num = map(int, input().split())
num_list = list(map(str, input().split())) # 값 입력 받음
length = len(str(N))
another_list = num_list * length
another_list.sort(reverse= True)
# print(another_list)
permutations_list = list(permutations(another_list, length))
# print(permutations_list)

for inner_str in permutations_list:
    if int(''.join(inner_str)) <= N:
        print(int(''.join(inner_str)))
        break





