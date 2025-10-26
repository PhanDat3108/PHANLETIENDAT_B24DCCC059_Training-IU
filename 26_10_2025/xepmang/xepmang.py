a = list(map(int, input("Nhập list1: ").split()))
b = list(map(int, input("Nhập list2: ").split()))

i = j = 0
kq = []

while i < len(a) and j < len(b):
    if a[i] <= b[j]:
        kq.append(a[i])
        i += 1
    else:
        kq.append(b[j])
        j += 1

while i < len(a):
    kq.append(a[i])
    i += 1

while j < len(b):
    kq.append(b[j])
    j += 1

print(kq)
