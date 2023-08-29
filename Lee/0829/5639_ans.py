import sys

sys.stdin = open('5639.txt')
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

# 후위 순회할 것인데 왼쪽과 오른쪽을 구분할 것
def postorder(left, right):
    if left > right:
        return
    else:
        root = preorder[left]
        div = right + 1
        for i in range(left + 1, right + 1):
            if root < preorder[i]:
                div = i
                break
        postorder(left + 1, div - 1)
        postorder(div, right)
        print(root)


preorder = []
while True:
    try:
        preorder.append(int(input()))
    except ValueError:
        break

postorder(0, len(preorder) - 1)
