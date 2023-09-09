'''
설계
1. 알파벳을 K개 배운 경우를 dfs 완전탐색
2. 그 중 가장 단어를 많이 읽은 경우를 추출
'''
import sys
N, K = map(int,input().split())

if K < 5:       #기본 a,n,t,i,c 는 배우려면 K = 5 이상으 돼야 됨
    print(0)
    exit()

elif K == 26:     # 모든 알파벳을 다 배울 수 있는 경우
    print(N)
    exit()

result = 0
text_set = [set(sys.stdin.readline().rstrip()) for _ in range(N)]
alpa_check = [0] * 26

for i in ('a','n','t','i','c'):
    alpa_check[ord(i)-ord('a')] = 1
def dfs(idx,cnt):
    global result

    if cnt == K - 5: # K 만큼 다 배웠을 때 읽을 수 있는 단어 검사
        read_cnt = 0
        for text in text_set:
            flag = True
            for alpa in text:
                if not alpa_check[ord(alpa)-ord('a')]:
                    flag = False
                    break

            if flag:
                read_cnt += 1
        result = max(result,read_cnt)
        return

    for i in range(idx,26):     #알파벳을 K개 배운 경우 탐색
        if not alpa_check[i]:
            alpa_check[i] = True
            dfs(i, cnt+1)
            alpa_check[i] = False

dfs(0,0)
print(result)