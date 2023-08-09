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
for j in width:
    if j >= max_width:
        max_width = j

max_height = 0
for k in height:
    if k >= max_height:
        max_height = k

        
sq = max_height * max_width - sm_width * sm_height
print(N * sq)