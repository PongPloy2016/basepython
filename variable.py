# -*- coding: utf-8 -*-


a = 3
b = 4.92
c = "itgenius"


x = y = z = 10
j, k = 5, 15

print(x, z, y)
print(j, k)

status = True
msg = False


# ตัวแปรแสดงผลร่วมกับข้อความ

# วิธีที่ 1

print("ราคาขายต่อชิ้น", b, "บาท")

# วิธีที่ 2

print("ราคาขายต่อชิ้น %.2f บาทมีจำนวน %d ชื้น" % (b, a))

# วิธีที่ 3 format string

print(f"ราคาขายต่อชิ้น {b} บาท มีจำนวน {a} ชื้น")
