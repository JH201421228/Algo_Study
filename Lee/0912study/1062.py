from itertools import combinations
import sys
sys.stdin = open('1062.txt')

N, K = map(int, input().split())
# 기본으로 들어있어야할 알파벳(5개)
base = {'a', 'n', 't', 'i', 'c'}
if K>=26:
    print(N)
    exit(0)
# 새로 고려해야할 알파벳 개수
new = K-5
# 만약 5개 보다 작다면 어느 단어도 표현 불가
if new < 0:
    print(0)
    exit(0)


words = set()       # 모든 남은 알파벳들 모음(여기서 조합 쓸 것)
rests = []          # 각 단어별 5개를 제외한 남은 알파벳들
for _ in range(N):
    word = set(input())
    words |= word
    rests.append(word-base)
words = list(words-base)
print(words)
print(rests)
final = 0
# 조합 쓸 때 n보다 r이 크거나 같아야하므로 조정
if len(words)<new:
    new = len(words)
# 남은 알파벳 중에서 new 개 골라서 조합 설정
for i in combinations(words, new):
    cnt = 0
    for j in rests:
        if len(j)>new:
            continue
        # 빈 집합을 count 한다.
        if not j-set(i):
            cnt += 1
    if final <= cnt:
        final = cnt
print(final)