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
    # R은 root 위치 N은 root 기준으로 배치할 새로운 노드
    # 새로 배치할 N이 더 크다면 오른쪽으로 들어갈 것
    if R <= N:
        # 오른쪽 자리가 비어있다면 바로 넣으면 되지만
        if right[R] == 0:
            right[R] = N
        # 비어있지 않다면 또 하위 트리로 가서 넣기를 반복해야 한다.
        else:
            R = right[R]
            splitting(R, N)
    # 새로 배치할 N이 더 작다면 왼 쪽으로 들어갈 것이며 위와 같은 로직
    else:
        if left[R] == 0:
            left[R] = N
        else:
            R = left[R]
            splitting(R, N)

# 정보 입력 리스트
left = [0] * 10 ** 6
right = [0] * 10 ** 6
root = int(input())     # 뿌리 : 최초 입력값

# 입력 총량을 주지 않으므로 try/except 처리
while 1:
    try : 
        N = int(input())
        splitting(root, N)
    except EOFError:
        break

# 후위 순회
postorder(root)