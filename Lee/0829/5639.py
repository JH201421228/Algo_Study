import sys
# RecursionError 가 뜨면?
sys.setrecursionlimit(10**6)
sys.stdin = open('5639.txt')

# 후위 표기를 출력해야함
def postorder(node):
    if node != 0:
        postorder(left[node])
        postorder(right[node])
        print(node)

# 어떤 수가 입력 들어올 때 어디로 갈지 정해주는 함수
def spliting(R, N):
    if R <= N:
        if right[R] == 0:
            right[R] = N
        else:
            R = right[R]
            spliting(R, N)
    else:
        if left[R] == 0:
            left[R] = N
        else:
            R = left[R]
            spliting(R, N)


left = [0] * 10**6
right = [0] * 10**6
root = int(input())

# 몇 개가 주어질지 모름
while 1:
    try:
        N = int(input())
        spliting(root, N)
    except EOFError:
        break
# 후위순회
postorder(root)


# 재귀 최적화는 어떻게 함?
# 가지 어캐 침?