# Giải phương trình bậc nhất: ax + b = 0

# Nhập hệ số a và b
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))

# Xử lý các trường hợp
if a == 0:
    if b == 0:
        print("Phương trình có vô số nghiệm.")
    else:
        print("Phương trình vô nghiệm.")
else:
    x = -b / a
    print(f"Nghiệm của phương trình là: x = {x}")