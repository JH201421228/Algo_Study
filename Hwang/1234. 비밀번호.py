T = 10

for t in range(1, 11):
    str_n, str_num = input().split()
    str_num_list = list(str_num)

    stack = []

    for i in str_num_list:
        if len(stack) == 0:
            stack.append(i)
        elif stack[-1] != i:
            stack.append(i)
        else:
            stack.pop()
    result = "".join(stack)
    print(f'#{t} {result}')