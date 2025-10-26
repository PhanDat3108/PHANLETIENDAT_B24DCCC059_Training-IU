def Chuyen(chuoi):
    giaTri = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    tong = 0
    for i in range(len(chuoi) - 1):
        if giaTri[chuoi[i]] < giaTri[chuoi[i + 1]]:
            tong -= giaTri[chuoi[i]]
        else:
            tong += giaTri[chuoi[i]]
    tong += giaTri[chuoi[-1]]
    return tong

chuoi = input("Nhập số: ").upper()
print(Chuyen(chuoi))
