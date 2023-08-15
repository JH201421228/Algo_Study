a, b, c, d, e, f = map(int, input().split())
# 연립 일차 방정식 -> 가감법 사용
# ax + by = c
# dx + ey = f
# ==============
# adx + bdy = cd
# adx + aey= af
# ==============
# (bd - ae)y = (cd - af)
# ax + by = c
# 해가 유일하므로 계수가 전부 0일 수는 없다.
if a != 0:
    y = (c * d - a * f) // (b * d - a * e)
    x = (c-b*y)//a
else:
    y = c//b
    if e != 0:
        x = (f - (c*d)//b)//e
    else:
        x = f//d
print(x, y)