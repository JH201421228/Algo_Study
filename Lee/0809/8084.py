N = int(input())
width = []
height = [] 
total = []
for i in range(6):
    Di, Lo = map(int, input().split())
    if Di == 1 or Di == 2:
        width.append(Lo)
        total.append(Lo)
    elif Di == 3 or Di == 4:
        height.append(Lo)
        total.append(Lo)

max_width = 0
for j in range(len(width)):
    if width[j] >= max_width:
        max_width = width[j]
        max_width_idx = j

max_height = 0
for k in range(len(height)):
    if k >= max_height:
        max_height = height[k]
        max_height_idx = k

p = 2 * max_height_idx
q = 2 * max_width_idx + 1

if max_height_idx - max_width_idx == 1 or -5:
    sm_height = total[(p+2)%6]
    sm_width = total[(q-2)]
elif max_width_idx - max_height_idx == 1 or -5:
    sm_height = total[p - 2]
    sm_width = total[(q + 2) % 6]

sq = max_height * max_width - sm_width * sm_height
print(N * sq)