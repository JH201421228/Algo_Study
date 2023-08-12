a,b,c,d,e,f= map(int,input().split())

#x,y의 주어진 범위를 하나씩 다 체크하며 답 구하기
for x in range(-999,1000):
    for y in range(-999,1000):
        if (a * x + b * y) == c and (d * x + e * y) == f:
            print(x,y)









