n = int(input())
nn = n

ans = 0

while nn > 4:
    nn -= 5
    ans += 1

while True:
    if nn % 2 == 0:
        ans += (nn // 2)
        break
    else:
        nn += 5
        ans -= 1

if n < 5 and n % 2 != 0:
    ans = -1

print(ans)