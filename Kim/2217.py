n = int(input())

rope = []
for _ in range(n):
    rope.append(int(input()))

rope.sort(reverse=True)

weight = []
cnt = 1
for i in rope:
    weight.append(i * cnt)
    cnt += 1

print(max(weight))
