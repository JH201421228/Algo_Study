'''
문제구상
1. X와 X의 각 자리수를 더해서 결과가 N이 나오는지 안나오는지 판단
2. X의 각 자리숫자는 while문 + 나눗셈을 이용 >> 각 자리숫자 구하는거는 그냥 str, int를 왔다갔다하면서 해도 될듯?
'''

N = int(input())
nums = []
for i in range(1,N):    #범위는 rough 하게 N까지 설정
    nums = [i]          #생성자 + 각자리숫자를 담을 리스트 >> i는 1부터 시작하므로, 생성자가 여러 개라도 첫 번째 걸리는게 가장 작은 생성자임
    A = 0
    B = 0
    while i:
        A, B = divmod(i,10)
        nums.append(B)  #각 자리 숫자 들을 nums 리스트에 담기
        i = A

    if sum(nums) == N:  #부분합이 맞다면
        print(nums[0])  #생성자 출력
        break

if sum(nums) != N:      #부분합이 없다면
    print(0)            #0 출력