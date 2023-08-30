import sys
sys.stdin = open('17298.txt')

N = int(input())
numbers = list(map(int, input().split()))
final = [-1] * N
check_list = []

for i in range(N-1):
    if numbers[i] < numbers[i+1]:
        final[i] = numbers[i+1]
        for j in check_list:
            if numbers[j] < numbers[i+1]:
                final[j] = numbers[i+1]
    else:
        check_list.append(i)
print(*final)