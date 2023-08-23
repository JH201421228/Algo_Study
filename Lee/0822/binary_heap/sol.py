import sys
sys.stdin = open('sample_input (3).txt')

Testcase = int(input())
for test in range(Testcase):
    N = int(input())
    IN = list(map(int, input().split()))        # 넣을 정보 리스트
    final = 0       # 최종 값
    tree = [0]*(N+1)    # 트리 그림
    last = 1    # 트리에 정보를 넣을 인덱스 위치

    for i in range(N):  # 정보를 순회하며 넣을 것인데
        if tree[i] == 0:        # 0이면 넣고
            tree[last] = IN[i]
        else:               # 아니면 다음에 넣고 로직 적용
            last += 1       # 넣은 인덱스 1증가시키고 바로 넣자
            tree[last] = IN[i]
            child = last    # 넣는 순간의 인덱스가 자식 인덱스
            parent = child//2   # 부모 인덱스 기록
            while parent >= 1 and tree[parent] > tree[child]:       # 최소힙이므로 부모가 더 크면 바꾼다
                tree[parent], tree[child] = tree[child], tree[parent]
                child = parent  # 한 번만 하면 되는게 아니므로 계속 확인 해준다 끝까지(그래서 parent >= 1 이 중요)
                parent = child // 2

    while N//2 != 0:
        final += tree[N//2]
        N = N//2


    print(f'#{test+1}', final)
