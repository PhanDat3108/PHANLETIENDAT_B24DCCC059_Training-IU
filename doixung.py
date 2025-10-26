x = int(input())

if -2**31 <= x <= 2**31 - 1:
    if x < 0:
        print(False)
    else:
        s = str(x)
        print(s == s[::-1])
