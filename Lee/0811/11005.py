# 10이상인 나머지들은 (+ 55한다음 캐릭터)
N, M = map(int, input().split())
Q = N // M
R = N - Q * M

List = [R]
while Q != 0:
    N = Q
    Q = N // M
    R = N - Q * M
    List.insert(0, R)

for i in range(len(List)):
    if List[i] >= 10:
        List[i] += 55
        List[i] = chr(List[i])
    else:
        List[i] += 48
        List[i] = chr(List[i])

print(''.join(List))