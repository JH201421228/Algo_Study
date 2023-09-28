'''
설계
- 무게의 차이를 경로의 가중치로 생각해서 풀기
1. ! a b w 들어오면  b = a + w 이므로 a -> b 로가는 간선은 w , b -> a로 가는 간선은 -w로 기록하고
2. ! a b w 가 들어올 때마다 weight_ls 를 바로바로 갱신해서 보관해두기
3. !를 입력 받을때 마다 weight_ls를 누적 및 갱신 시키고, ?를 받았을 때 b-a 무게를 통해 결과값 꺼내기

첨언.
1. 문제의 특성 상 무게 값 자체가 상대적인 값으로 주어지기 때문에, start->end로 가는 간선이 존재하면 어떤 경로로 가든 다 같은 값을 가지게 됨.

##주의 a b w 추가 시 weight_ls 갱신 방법##
1. weight_ls의 a, b 값이 모두 없는 경우 : 기본적으로 음수가 있으면 보기 싫기 때문에
-> start node = 무게가 작은 값
-> end node = 무게가 큰 값

2. weight_ls에 a, b 중 값이 하나라도 있는 경우
-> start node = 값이 존재하는 노드
-> end node = 값이 존재하지 않는 노드

3. weight_ls에 a, b 중 값이 모두 있는 경우
-> start node = 해당 노드와 연결된 값이 더 많은 노드
-> end node = 해당 노드와 연결된 값이 더 적은 노드
'''


def find_parents(x):
    if parents[x] != x:
        parents[x] = find_parents(parents[x])
    return parents[x]


def union_parents(a, b):
    a = find_parents(a)
    b = find_parents(b)
    if a < b:
        parents[b] = a
        tmp_ls[parents[a]].add(b)
    else:
        parents[a] = b
        tmp_ls[parents[b]].add(a)


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    weight_ls = [float("INF")] * (N + 1)
    parents = {}
    tmp_ls = [set() for _ in range(N + 1)]

    for i in range(N + 1):  # union-find를 위한 부모 테이블 생성
        parents[i] = i

    print(f'#{test_case}', end=" ")
    for _ in range(M):
        text = input().split()
        if text[0] == '!':
            a, b, w = int(text[1]), int(text[2]), int(text[3])

            if weight_ls[a] == float("INF") and weight_ls[b] == float("INF"):  # weight_ls의 a, b 값이 모두 없는 경우
                weight_ls[a] = 0
                weight_ls[b] = weight_ls[a] + w

            elif weight_ls[a] != float("INF") and weight_ls[b] != float("INF"):  # weight_ls의 a, b 값이 모두 있는 경우

                if len(tmp_ls[a]) < len(tmp_ls[b]):
                    x = weight_ls[a]
                    weight_ls[a] = weight_ls[b] - w

                    for i in tmp_ls[a]:
                        weight_ls[i] -= x
                else:
                    x = weight_ls[b]
                    weight_ls[b] = weight_ls[a] + w

                    for i in tmp_ls[b]:
                        weight_ls[i] -= x

            else:  # weight_ls의 a, b 값이 하나만 있는 경우
                if weight_ls[a] != float("INF"):
                    weight_ls[b] = weight_ls[a] + w
                else:
                    weight_ls[a] = weight_ls[b] - w

            union_parents(a, b)

        else:
            if (weight_ls[int(text[2])] - weight_ls[int(text[1])]) != float("INF"):
                print((weight_ls[int(text[2])] - weight_ls[int(text[1])]), end=" ")
            else:
                print("UNKNOWN", end=" ")
    print()