f = open("SODEP.INP", "r")
n = int(f.readline().strip())
f.close()

tong = sum(int(x) for x in str(n))

if tong % 10 == 9:
    kq = 1
else:
    kq = 0

f = open("SODEP.OUT", "w")
f.write(str(kq))
f.close()
