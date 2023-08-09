# 0과 1을 바꾸는 로직은 무엇으로 사용할 것인가 1더해서 2모듈로 하자.
def change_light(a):
    return (a+1)%2

N = int(input())
onoff = list(map(int, input().split()))
studentcount = int(input())
for _ in range(studentcount):
    S, K = map(int, input().split())

    # 만약 남자라면 입력받은 수의 배수의 인덱스를 전부 바꾼다.
    if S == 1:
        for i in range(1, N//K + 1):
            onoff[K*i - 1] = change_light(onoff[K*i - 1])
    
    else:
        j = 0
        while (K-j-1 >= 0) and  K+j-1 <= N-1 and onoff[K-j-1] == onoff[K+j-1]:
            j+=1
        j -= 1
        for l in range(K-j-1, K+j):
            onoff[l] = change_light(onoff[l])

    # print(onoff)
if N > 20:
    n = N//20
    for i in range(n+1):
        print(*onoff[20*i:20*(i+1)])
else:
    print(*onoff)