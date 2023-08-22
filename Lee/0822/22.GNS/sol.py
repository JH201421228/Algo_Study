import sys
sys.stdin = open('GNS_test_input.txt')
num = {"ZRO" : 0, "ONE" : 1, "TWO" : 2, "THR" : 3, "FOR" : 4, "FIV" : 5, "SIX" : 6, "SVN" : 7, "EGT" : 8, "NIN" : 9}
num_list=list(num.keys())
Testcase = int(input())
for _ in range(Testcase):
    test, N = input().split()
    N = int(N)
    Li = list(input().split())
    final = []
    for i in Li:
        final.append(num[i])
    final.sort()
    print(test)
    for i in final:
        print(num_list[i], end=' ')