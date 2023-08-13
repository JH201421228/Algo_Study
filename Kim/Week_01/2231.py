n = int(input())

ans = 1         # 1부터 시작해서 생성자 찾을 때 까지
flag = True     
while True:
    lst = [ans,]    # 자기자신 + 모든 자리 수
    temp = ans
    if temp > n:
        flag = False # n보다 커진다면 False
    while temp >= 10:   # 각 자리수 lst에 추가하는 방법
        lst.append(temp % 10)   # 10으로 나눈 나머지 추가
        temp //= 10             # 자기자신 10으로 나눈 몫
    lst.append(temp)
    
    # print(lst)        # 과정 검증용
    
    if not flag:        # 생성자 존재하지 않는다면 0 출력
        print(0)
        break

    a = sum(lst)        # lst의 합과 n이 같다면 생성자 이므로 출력
    if n == a:
        print(ans)
        break
    else:               # 위 모든 과정이 아니라면 ans 1 더한 후 과정 진행
        ans += 1