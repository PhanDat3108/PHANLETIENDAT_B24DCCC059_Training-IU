def tangMot(so):
    n = len(so)
    for i in range(n - 1, -1, -1):
        if so[i] < 9:
            so[i] += 1
            return so
        so[i] = 0
    return [1] + so

so = list(map(int, input("Nhập mảng: ").split()))
kq = tangMot(so)
print(kq)
