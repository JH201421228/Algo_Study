String = input()
String = String.upper()
counting = [0]*26
for i in String:
    counting[ord(i)-65] += 1
maxi = max(counting)
if counting.count(maxi) > 1:
    print('?')
else:
    a = counting.index(maxi)
    print(chr(a+65))