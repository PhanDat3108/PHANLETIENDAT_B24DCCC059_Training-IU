s1 = input().strip()
s2 = input().strip()

nums1 = list(map(int, s1.split())) if s1 else []
nums2 = list(map(int, s2.split())) if s2 else []

m = len(nums1)
n = len(nums2)


if  0 <= m <= 1000 and 0 <= n <= 1000 and 1 <= m + n <= 2000 and all(-10**6 <= x <= 10**6 for x in nums1 + nums2):

    gop = sorted(nums1 + nums2)
    tong = len(gop)
    if tong % 2 == 1:
        print(float(gop[tong // 2]))
    else:
        print((gop[tong // 2 - 1] + gop[tong // 2]) / 2)
