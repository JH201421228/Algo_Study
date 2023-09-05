import sys
# input = sys.stdin.readline
sys.setrecursionlimit(10**4)


def preorder_return(val, id=1, left=float('-inf'), right=float('inf')):
    # val = [50, 30, 24, 5, 28, 45, 98, 52, 60]
    # 일단 1번 idx부터, 첫값이니까 범위는 -무한대 ~ +무한대
    if not val:  # 전위 순회로 얻은 값이 없으면
        return

    # 값이 지금 넣을 노드 값인지 아닌지
    # 아니면 넣을 수 있을 곳까지 돌아가기
    num = val[0]
    if num < left or num > right:
        return

    val.pop(0)
    # 노드 딕셔너리에 값 할당
    node[id] = num

    # 왼쪽 자식 노드 처리
    c1[id] = id * 2
    preorder_return(val, c1[id], left, num)

    # 오른쪽 자식 노드 처리
    c2[id] = id * 2 + 1
    preorder_return(val, c2[id], num, right)


def postorder(node, c1, c2, id):
    if id not in node:
        return

    postorder(node, c1, c2, c1.get(id, None))
    postorder(node, c1, c2, c2.get(id, None))
    print(node[id])


val = []
while True:
    try:
        val.append(int(input().strip()))
    except EOFError:
        break
# print(val)

node = {}
c1 = {}
c2 = {}
preorder_return(val)
postorder(node, c1, c2, 1)
# print(node)
# print(c1)
# print(c2)
