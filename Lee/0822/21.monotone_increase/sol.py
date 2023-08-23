import sys
sys.stdin = open('s_input.txt')

Testcase = int(input())
for test in range(Testcase):
    N = int(input())
    numbers = list(map(int, input().split()))
    # 단조증가 조건을 만족하는 애들을 모을 리스트
    final = []
    # 이건 혹시 모를 반례 때문에 넣어둠
    if N == 1:
        final.append(N)
    # 리스트를 순회하며 다음 거랑 곱한다
    for i in range(N-1):
        for j in range(i+1, N):
            num = numbers[i]*numbers[j]
            final.append(num)       # 일단 리스트에 넣고
            num = str(num)          # 스트링으로 바꾸고
            for k in range(len(num)-1):
                if int(num[k]) > int(num[k+1]):     # 하나라도 단조증가를 만족 안하면
                    final.pop()     # 일단 넣은 애를 도로 빼주고 종료 -> 다음 곱으로 감
                    break
    if final:
        print(f'#{test+1}', max(final))
    else:   # 후보가 하나도 없다면 -1
        print(f'#{test+1}', -1)