import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

word = {}
for _ in range(n):
    w = input().rstrip()
    if len(w) < m:
        continue

    if w in word:
        word[w] += 1
    else:
        word[w] = 1

ans = sorted(word.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for i in range(len(ans)):
    print(ans[i][0])