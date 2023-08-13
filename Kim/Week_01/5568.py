n = int(input())
k = int(input())


def perm(lst, n):               # 순열을 이용한 모든 경우의 수 계산
    result = []
    if n > len(lst):
        return result

    if n == 1:
        for i in lst:
            result.append([i])

    elif n > 1:
        for i in range(len(lst)):
            ans = [i for i in lst]
            ans.remove(lst[i])
            for p in perm(ans, n-1):
                result.append([lst[i]] + p)

    return result


num_lst = []
for _ in range(n):
    num_lst.append(str(input()))        # n번 입력을 통해 리스트에 카드 추가

my_lst = perm(num_lst, k)               # 모든 경우의 수 계산

lst = []
for i in my_lst:                        # 1개의 숫자로 만든 후
    lst.append(''.join(i))

print(len(set(lst)))                    # set 통해 중복제거 and 갯수 출력
