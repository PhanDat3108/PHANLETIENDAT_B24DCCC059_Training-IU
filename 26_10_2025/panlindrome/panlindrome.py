s = input("Nhập chuỗi: ")

x = ""
for c in s:
    if c.isalnum():  
        x += c.lower() 
print(x == x[::-1])
