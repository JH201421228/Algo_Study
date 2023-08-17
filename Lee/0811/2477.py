import sys
sys.stdin = open('a.txt')

N = int(input())
List = []
for _ in range(6):
    direction, length = map(int, input().split())
    List.append(length)

maximum = 0
max_idx = 0
for i in range(len(List)):
    if List[i] >= maximum:
        maximum = List[i]
        max_idx = i

if List[(max_idx-1)%6] > List[(max_idx+1)%6]:
    Big = List[(max_idx - 1) % 6] * maximum
    Small = List[(max_idx - 3) % 6] * List[(max_idx + 2) % 6]
else:
    Big = List[(max_idx + 1) % 6] * maximum
    Small = List[(max_idx + 3) % 6] * List[(max_idx - 2) % 6]

print(N*(Big-Small))