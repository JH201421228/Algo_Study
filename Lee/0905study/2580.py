import sys
sys.stdin = open("2580.txt")

# i, j 좌표에 num이 들어갈 수 있는지 확인하는 함수
def check(num, i, j):
    # 행과 열을 순회했을 때 그 수가 있다면 거짓
    for k in range(9):
        if Board[i][k] == num:
            return False
        if Board[k][j] == num:
            return False
    # 박스를 확인하는 로직
    M = (i//3)*3
    N = (j//3)*3
    for m in range(M, M+3):
        for n in range(N, N+3):
            if Board[m][n] == num:
                return False
    # 전부 다 통과하면 참
    return True

'''
우리가 아는 스도쿠 풀이법 중 가장 단순한 방법 사용
예를 들어 어떤 빈 칸에 4와 9가 들어갈 수 있다면
그 자리를 4로 먼저 채워서 쭉 스도쿠를 완성해나간다.
만약 어디선가 문제가 발생하면 다시 되돌아와서 
9를 채워서 쭉 완성해나가는 형식 -> DFS를 사용하자는 생각
'''
# N을 빈 좌표들 개수로 설정해놨고 빈 칸을 채우면서 1씩 빼나갈 것이므로
# 0이 된다면 완성된다는 의미
def DFS(N):
    # 만약 스도쿠가 완성되었다면 보드를 출력하도록
    # 재귀 안에서 결론이 날 것이므로 return 대신 exit()로 강제 종료
    if N == 0:
        for i in range(9):
            print(*Board[i])
        exit(0)

    # 빈 칸에서 하나를 뽑아서 1~9 중 들어갈 수 있는지 확인(ex 4, 9)
    i, j = Blank.pop()
    for num in range(1, 10):
        # num이 들어갈 수 있다면 그 수를 먼저 넣고 쭉 진행
        # 만약 실패를 한다면 경로들에 0을 넣어서 초기화
        if check(num, i, j):
            Board[i][j] = num
            DFS(N-1)
            Board[i][j] = 0


# 스도쿠 판을 입력 받고
Board = [list(map(int, input().split())) for _ in range(9)]
# 판을 순회하며 빈 부분을 확인하여 그 인덱스들을 저장
Blank = []
for i in range(9):
    for j in range(9):
        if Board[i][j] == 0:
            Blank.append((i, j))
# 빈 부분의 길이만큼 채워나갈 것이며 다 채웠다면 종료할 것
N = len(Blank)
DFS(N)

