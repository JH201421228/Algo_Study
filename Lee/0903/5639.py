import sys
sys.stdin = open('5639.txt')
sys.setrecursionlimit(10**9)

# 후위 표기를 출력해야함
def postorder(node):
    if node != 0:
        postorder(left[node])
        postorder(right[node])
        print(node)

# 어떤 수가 입력 들어올 때 어디로 갈지 정해주는 함수
def splitting(R, N):
    if R <= N:
        if right[R] == 0:
            right[R] = N
        else:
            R = right[R]
            splitting(R, N)
    else:
        if left[R] == 0:
            left[R] = N
        else:
            R = left[R]
            splitting(R, N)

# 정보 입력 리스트
left = [0] * 10 ** 6
right = [0] * 10 ** 6
root = int(input())

while 1:
    try : 
        N = int(input())
        splitting(root, N)
    except EOFError:
        break

# 후위 순회
postorder(root)