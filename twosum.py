def CongHaiSo(danhSachSo, mucTieu):
    chiSo = {}
    for i in range(len(danhSachSo)):
        canTim = mucTieu - danhSachSo[i]
        if canTim in chiSo:
            return [chiSo[canTim], i]
        chiSo[danhSachSo[i]] = i

danhSachSo = list(map(int, input("Nhập mảng: ").split()))
mucTieu = int(input("Nhập mục tiêu: "))

if 2 <= len(danhSachSo) <= 10**4 and all(-10**9 <= x <= 10**9 for x in danhSachSo) and -10**9 <= mucTieu <= 10**9:
    ketQua = CongHaiSo(danhSachSo, mucTieu)
    print(ketQua)
else:
    print("nhập lại")
